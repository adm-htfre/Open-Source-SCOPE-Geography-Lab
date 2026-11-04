import fs from 'fs'; import * as d3 from 'd3-geo';
const [,,simp,unitsF,out]=process.argv;
const g=JSON.parse(fs.readFileSync(simp)); const key=JSON.parse(fs.readFileSync(unitsF)).key;
const W=600; const proj=d3.geoIdentity().reflectY(true).fitWidth(W-20,g);
const b=d3.geoPath(proj).bounds(g); const H=Math.ceil(b[1][1]-b[0][1])+20;
proj.fitExtent([[10,10],[W-10,H-10]],g); const path=d3.geoPath(proj).digits(1);
const feat=g.features.map(f=>{const n=f.properties.dtname, u=key[n]; if(!u) throw n;
 return {k:n,u,lab:null,mr:null,note:n==='Ballari'?'In 2020 Vijayanagara district was carved out of Ballari. In the 2011 Census it was part of Ballari, so these figures are for undivided Ballari.':null,d:path(f),c:path.centroid(f).map(v=>+v.toFixed(1))}});
fs.writeFileSync(out,JSON.stringify({H,feat})); console.log(H,feat.length,(JSON.stringify(feat).length/1024|0)+'KB');
