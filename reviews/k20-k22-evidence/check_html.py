from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import sys,json
class P(HTMLParser):
 def __init__(self): super().__init__(); self.ids=[];self.links=[];self.img=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append(d['id'])
  if t=='a' and 'href' in d:self.links.append(d['href'])
  if t=='img':self.img.append(d)
root=Path(sys.argv[1]); pars={}; errors=[];count=0
for f in root.glob('*.html'):
 p=P();p.feed(f.read_text());pars[f]=p
 if len(p.ids)!=len(set(p.ids)): errors.append(str(f)+' duplicate IDs')
 if '??' in f.read_text(): errors.append(str(f)+' unresolved marker')
for f,p in pars.items():
 for href in p.links:
  u=urlsplit(href)
  if u.scheme or u.netloc:continue
  target=(f.parent/unquote(u.path)).resolve() if u.path else f.resolve()
  count+=1
  if not target.exists():errors.append(href+' absent')
  elif u.fragment and target in pars and unquote(u.fragment) not in pars[target].ids:errors.append(href+' absent fragment')
 for d in p.img:
  if not d.get('alt'):errors.append(str(f)+' absent image alt '+d.get('src',''))
r={'pages':len(pars),'local_links':count,'images':sum(len(p.img) for p in pars.values()),'errors':errors}
print(json.dumps(r,indent=2));assert not errors
