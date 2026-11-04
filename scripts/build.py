import json
h=open('template.html').read()
def pack(u,f):
    mu=json.load(open(u));mf=json.load(open(f))
    return json.dumps(dict(units=mu['units'],feat=mf['feat']),ensure_ascii=False,separators=(',',':'))
out=(h.replace('/*BUNDLE*/',open('bundle2.json').read()).replace('/*MH*/',pack('mh_units.json','mh_feat2.json'))
      .replace('/*KA*/',pack('ka_units.json','ka_feat2.json')).replace('/*FRAME*/',open('frame.json').read())
      .replace('/*WORLD*/',open('world/world.json').read()))
open('india-atlas.html','w').write(out)
open('preview.html','w').write('<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width"><style>[hidden]{display:none!important}</style></head><body>'+out+'</body></html>')
print(len(out)//1024,'KB')
