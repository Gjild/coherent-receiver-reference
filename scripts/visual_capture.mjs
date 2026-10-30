// Private DevTools-pipe capture for visual_inspection.py; Node built-ins only.
import {spawn} from 'node:child_process';
import fs from 'node:fs';

const [browser, url, output, widthText, heightText, waitText] = process.argv.slice(2);
const width = Number(widthText), height = Number(heightText), waitMs = Number(waitText);
const args = ['--headless', '--remote-debugging-pipe',
  `--user-data-dir=${output}/profile`, `--window-size=${width},${height}`, 'about:blank'];
fs.writeFileSync(`${output}/browser-command.json`, JSON.stringify({browser, args}, null, 2)+'\n');
const child = spawn(browser, args, {stdio: ['ignore', 'inherit', 'inherit', 'pipe', 'pipe']});
let buffer = '', sequence = 0;
const pending = new Map();
const exited = new Promise(resolve => child.on('exit', (code, signal) => resolve({code, signal})));
child.on('error', error => { for (const request of pending.values()) request.reject(error); pending.clear(); });
child.stdio[4].on('data', chunk => {
  buffer += chunk.toString();
  let end;
  while ((end = buffer.indexOf('\0')) >= 0) {
    const raw = buffer.slice(0, end); buffer = buffer.slice(end + 1);
    if (!raw) continue;
    const message = JSON.parse(raw), request = pending.get(message.id);
    if (request) { pending.delete(message.id); request.resolve(message); }
  }
});
async function call(method, params = {}, sessionId) {
  const id = ++sequence;
  let timer;
  const message = await new Promise((resolve, reject) => {
    pending.set(id, {resolve, reject});
    timer = setTimeout(() => { pending.delete(id); reject(new Error(`Timed out: ${method}`)); }, Math.max(10000, waitMs));
    child.stdio[3].write(JSON.stringify({id, method, params, ...(sessionId ? {sessionId} : {})})+'\0');
  }).finally(() => clearTimeout(timer));
  if (message.error) throw new Error(`${method}: ${JSON.stringify(message.error)}`);
  return message.result;
}
try {
  const version = await call('Browser.getVersion');
  const {targetId} = await call('Target.createTarget', {url: 'about:blank'});
  const {sessionId} = await call('Target.attachToTarget', {targetId, flatten: true});
  await call('Page.enable', {}, sessionId);
  await call('Emulation.setDeviceMetricsOverride', {width, height, deviceScaleFactor: 1, mobile: false}, sessionId);
  const navigation = await call('Page.navigate', {url}, sessionId);
  if (navigation.errorText) throw new Error(`Navigation failed: ${navigation.errorText}`);
  const deadline = Date.now() + Math.max(3000, waitMs);
  let ready;
  do {
    ready = await call('Runtime.evaluate', {expression: '({url:location.href,state:document.readyState})', returnByValue: true}, sessionId);
    if (ready.result.value.url === url && ready.result.value.state === 'complete') break;
    if (Date.now() > deadline) throw new Error(`Page not ready: ${JSON.stringify(ready)}`);
    await new Promise(resolve => setTimeout(resolve, 50));
  } while (true);
  const document = await call('Runtime.evaluate', {expression: `(async () => {
    if (globalThis.MathJax?.startup?.promise) await MathJax.startup.promise;
    await document.fonts.ready;
    await Promise.all([...document.images].map(i => i.decode().catch(() => {})));
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
    return {url:location.href,title:document.title,readyState:document.readyState,
      viewport:[innerWidth,innerHeight],mathElements:document.querySelectorAll('.math').length,
      mathjaxContainers:document.querySelectorAll('mjx-container').length,
      images:[...document.images].map(i=>({src:i.getAttribute('src'),complete:i.complete,width:i.naturalWidth,height:i.naturalHeight}))};
  })()`, awaitPromise: true, returnByValue: true}, sessionId);
  if (document.exceptionDetails) throw new Error(`Page readiness error: ${JSON.stringify(document.exceptionDetails)}`);
  const metrics = await call('Page.getLayoutMetrics', {}, sessionId);
  const size = metrics.cssContentSize;
  const clip = {x: 0, y: 0, width: Math.ceil(size.width), height: Math.ceil(size.height), scale: 1};
  if (clip.width * clip.height > 100000000 || clip.height > 32767) throw new Error('Page exceeds bounded capture size; use bounded sections.');
  fs.writeFileSync(`${output}/page.json`, JSON.stringify({version,document:document.result.value,metrics,clip}, null, 2)+'\n');
  const shot = await call('Page.captureScreenshot', {format: 'png', captureBeyondViewport: true, clip}, sessionId);
  fs.writeFileSync(`${output}/image.png`, Buffer.from(shot.data, 'base64'));
  await call('Browser.close');
  const status = await exited;
  fs.writeFileSync(`${output}/browser-exit.json`, JSON.stringify(status)+'\n');
  console.log(JSON.stringify({capture:'OK',...status,clip}));
  if (status.code !== 0) process.exitCode = 1;
} catch (error) {
  console.error(String(error)); process.exitCode = 1;
} finally {
  if (child.exitCode === null && child.signalCode === null) {
    child.kill('SIGTERM');
    const timer = setTimeout(() => child.kill('SIGKILL'), 1000);
    await exited; clearTimeout(timer);
  }
}
