"""Exact illustrative flow balances; no measured link or clock evidence."""
from fractions import Fraction as F
import json
nominal=F(192750000);fast=nominal*(1+F(20,1000000))
fixed=nominal;link=F(240000000);headroom=F(131072)
r={'nominal_Bps':float(nominal),'producer_Bps':float(fast),
   'fixed_consumer_Bps':float(fixed),'clocked_excess_Bps':float(fast-fixed),
   'clocked_fill_s':float(headroom/(fast-fixed)),'link_spare_Bps':float(link-fast)}
assert r['clocked_excess_Bps']==3855 and r['link_spare_Bps']==47246145
# A distinct discrete fluid balance verifies the direction and accumulated bytes.
qfixed=headroom;qlink=headroom
for _ in range(34):
    qfixed+=fast-fixed;qlink=max(F(0),qlink+fast-link)
assert qfixed==262142 and qlink==0
r['fixed_occupancy_at34s_B']=float(qfixed);r['link_occupancy_at34s_B']=float(qlink)
print(json.dumps(r,indent=2))
