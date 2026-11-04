import fs from 'fs'; import * as d3 from 'd3-geo';
const g=JSON.parse(fs.readFileSync('mh_simp.json'));
const key=JSON.parse(fs.readFileSync('mh_units.json')).key;
const W=600; const proj=d3.geoIdentity().reflectY(true).fitWidth(W-20,g);
const path0=d3.geoPath(proj); const b=path0.bounds(g); const H=Math.ceil(b[1][1]-b[0][1])+20;
proj.fitExtent([[10,10],[W-10,H-10]],g);
const path=d3.geoPath(proj).digits(1);
const feat=g.features.map(f=>{const n=f.properties.dtname; const u= n==='Palghar'?'thane':key[n]; if(!u) throw n;
 return {k:n,u,lab:n==='Palghar'?'Palghar':null,mr:n==='Palghar'?'पालघर':null,
 note:n==='Palghar'?'Palghar district was carved out of Thane in 2014. In the 2011 Census it was part of Thane, so the figures shown are for undivided Thane.':(n==='Thane'?'Includes present-day Palghar district (separated in 2014).':null),
 d:path(f),c:path.centroid(f).map(v=>+v.toFixed(1))}});
fs.writeFileSync('mh_feat.json',JSON.stringify({H,feat}));
console.log(H, feat.length, (JSON.stringify(feat).length/1024|0)+'KB');
