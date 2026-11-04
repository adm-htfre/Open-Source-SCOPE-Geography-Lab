import fs from 'fs'; import * as d3 from 'd3-geo';
const india=JSON.parse(fs.readFileSync('simp.json'));
const W=6000, AR=672/600;
const proj=d3.geoIdentity().reflectY(true).fitWidth(W,india);
const path=d3.geoPath(proj).digits(0);
const b=path.bounds(india);
function box(bb,padFrac){ // pad then expand to aspect AR (h/w)
  let [x0,y0]=bb[0],[x1,y1]=bb[1]; let w=x1-x0,h=y1-y0; const p=Math.max(w,h)*padFrac;
  x0-=p;y0-=p;x1+=p;y1+=p; w=x1-x0;h=y1-y0;
  if(h/w<AR){const nh=w*AR; y0-=(nh-h)/2; h=nh;} else {const nw=h/AR; x0-=(nw-w)/2; w=nw;}
  return [x0,y0,w,h].map(v=>Math.round(v));
}
const out={vb:{india:box(b,0.015)}};
// india features
const bundle=JSON.parse(fs.readFileSync('bundle.json'));
const byK=Object.fromEntries(india.features.map(f=>[f.properties.STNAME_SH,f]));
bundle.feat.forEach(f=>{const g=byK[f.k]; f.d=path(g); f.c=path.centroid(g).map(Math.round);});
fs.writeFileSync('bundle2.json',JSON.stringify(bundle));
for (const [st,simp,feat] of [['mh','mh_simp.json','mh_feat.json'],['ka','ka_simp.json','ka_feat.json']]){
  const g=JSON.parse(fs.readFileSync(simp)); const F=JSON.parse(fs.readFileSync(feat));
  const byN=Object.fromEntries(g.features.map(x=>[x.properties.dtname,x]));
  F.feat.forEach(f=>{const x=byN[f.k]; f.d=path(x); f.c=path.centroid(x).map(Math.round);});
  out.vb[st]=box(path.bounds(g),0.05);
  fs.writeFileSync(st+'_feat2.json',JSON.stringify({feat:F.feat}));
}
// Kavaratti point
const R=6378137, lon=72.642, lat=10.566;
out.ld=proj([R*lon*Math.PI/180, R*Math.log(Math.tan(Math.PI/4+lat*Math.PI/360))]).map(Math.round);
fs.writeFileSync('frame.json',JSON.stringify(out)); console.log(out);
for (const f of ['bundle2.json','mh_feat2.json','ka_feat2.json']) console.log(f,(fs.statSync(f).size/1024|0)+'KB');
