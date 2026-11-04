import json,csv
geo=json.load(open('w_geo.json'))
def rd(fn,cast=float,yr=False):
    o={}
    for l in open(fn):
        p=l.split()
        if not p: continue
        if p[0]=='WLD': o['WLD']=float(p[-1]); continue
        o[p[0]]=(cast(p[1]),int(p[2])) if yr else cast(p[1])
    return o
area=rd('area.txt',int); gdp=rd('gdp.txt',int,True); le=rd('le.txt'); urb=rd('urban.txt'); frs=rd('forest.txt')
pop={}
for r in csv.DictReader(open('pop.csv')):
    c=r['Country Code']; y=int(r['Year'])
    if r['Value'] and (c not in pop or y>pop[c][1]): pop[c]=(int(float(r['Value'])),y)
fix={'KOS':'XKX'}
CONT={'Asia':'AS','Africa':'AF','Europe':'EU','North America':'NA','South America':'SA','Oceania':'OC'}
mr_over={'IND':'भारत','USA':'अमेरिका','GBR':'युनायटेड किंगडम','CHN':'चीन','PAK':'पाकिस्तान','BGD':'बांगलादेश','NPL':'नेपाळ','LKA':'श्रीलंका','BTN':'भूतान','MMR':'म्यानमार','AFG':'अफगाणिस्तान','JPN':'जपान','RUS':'रशिया','AUS':'ऑस्ट्रेलिया','DEU':'जर्मनी','FRA':'फ्रान्स','BRA':'ब्राझील','CAN':'कॅनडा'}
units=[]; seen=set()
shapeK={f['k'] for f in geo['feat']}
for k,p in geo['P'].items():
    iso=fix.get(k, p['iso'] if p['iso']!='-99' else k)
    if iso in seen or iso not in pop or iso not in area: continue
    cont=p['cont'] if p['cont'] in CONT else {'MDV':'Asia','MUS':'Africa','SYC':'Africa'}.get(iso)
    if not cont: continue
    seen.add(iso)
    pp,py=pop[iso]; ar=area[iso]
    g=gdp.get(iso)
    units.append(dict(id=iso,k=k,en=p['en'],mr=mr_over.get(iso,p['hi'] or p['en']),type='Country',zone=CONT[cont],
        pop=pp,popY=py,area=ar,den=round(pp/ar,1),le=round(le[iso],1) if iso in le else None,
        gdp=g[0] if g else None,gdpY=g[1] if g else None,urb=urb.get(iso),frs=frs.get(iso),
        dot=None if k in shapeK else p['c'], cap=''))
missing=[c for c in area if c not in seen]
print(len(units),'units; WB countries not on map:',missing)
print('dots:',[u['en'] for u in units if u['dot']])
tot=sum(u['pop'] for u in units); print('pop sum',tot)
gw=[(u['gdp'],u['pop']) for u in units if u['gdp']]
avg=dict(den=round(tot/sum(u['area'] for u in units),1),le=le['WLD'],urb=urb['WLD'],frs=frs['WLD'],gdp=round(sum(a*b for a,b in gw)/sum(b for a,b in gw)))
print(avg)
feat=[]
for f in geo['feat']:
    iso=fix.get(f['k'], f['iso'] if f['iso']!='-99' else f['k'])
    feat.append(dict(k=f['k'],u=iso if iso in seen else None,en=f['en'],mr=f['hi'],d=f['d'],lab=None,note=None))
json.dump(dict(units=units,feat=feat,sphere=geo['sphere'],W=geo['W'],H=geo['H'],avg=avg),open('world.json','w'),ensure_ascii=False,separators=(',',':'))
import os; print(os.path.getsize('world.json')//1024,'KB')
