import json
# Census 2011 district figures (2011 boundaries: 35 districts; Palghar was part of Thane)
# key(map dtname): (id, current English name, marathi, 2011 name if different, division, HQ, pop, growth, sexratio, literacy, density)
D = [
 ("Thane","thane","Thane","ठाणे",None,"KK","Thane",11060148,36.01,886,84.53,1157),
 ("Pune","pune","Pune","पुणे",None,"PN","Pune",9429408,30.37,915,86.15,603),
 ("Mumbai Suburban","mumsub","Mumbai Suburban","मुंबई उपनगर",None,"KK","Bandra",9356962,8.29,860,89.91,20980),
 ("Nashik","nashik","Nashik","नाशिक",None,"NS","Nashik",6107187,22.30,934,82.31,393),
 ("Nagpur","nagpur","Nagpur","नागपूर",None,"NG","Nagpur",4653570,14.40,951,88.39,470),
 ("Ahmadnagar","ahmednagar","Ahilyanagar","अहिल्यानगर","Ahmadnagar","NS","Ahilyanagar",4543159,12.44,939,79.05,266),
 ("Solapur","solapur","Solapur","सोलापूर",None,"PN","Solapur",4317756,12.16,938,77.02,290),
 ("Jalgaon","jalgaon","Jalgaon","जळगाव",None,"NS","Jalgaon",4229917,14.86,925,78.20,360),
 ("Kolhapur","kolhapur","Kolhapur","कोल्हापूर",None,"PN","Kolhapur",3876001,10.01,957,81.51,504),
 ("Aurangabad","aurangabad","Chhatrapati Sambhajinagar","छत्रपती संभाजीनगर","Aurangabad","AU","Chhatrapati Sambhajinagar",3701282,27.76,923,79.02,366),
 ("Nanded","nanded","Nanded","नांदेड",None,"AU","Nanded",3361292,16.86,943,75.45,319),
 ("Mumbai","mumcity","Mumbai City","मुंबई शहर",None,"KK","Mumbai",3085411,-7.57,832,89.21,19652),
 ("Satara","satara","Satara","सातारा",None,"PN","Satara",3003741,6.93,988,82.87,287),
 ("Amravati","amravati","Amravati","अमरावती",None,"AM","Amravati",2888445,10.79,951,87.38,237),
 ("Sangli","sangli","Sangli","सांगली",None,"PN","Sangli",2822143,9.24,966,81.48,329),
 ("Yavatmal","yavatmal","Yavatmal","यवतमाळ",None,"AM","Yavatmal",2772348,12.78,952,82.82,204),
 ("Raigarh","raigad","Raigad","रायगड",None,"KK","Alibag",2634200,19.31,959,83.14,368),
 ("Buldana","buldhana","Buldhana","बुलढाणा",None,"AM","Buldhana",2586258,15.85,934,83.40,268),
 ("Bid","beed","Beed","बीड",None,"AU","Beed",2585049,19.61,916,76.99,242),
 ("Latur","latur","Latur","लातूर",None,"AU","Latur",2454196,17.97,928,77.26,343),
 ("Chandrapur","chandrapur","Chandrapur","चंद्रपूर",None,"NG","Chandrapur",2204307,6.43,961,80.01,193),
 ("Dhule","dhule","Dhule","धुळे",None,"NS","Dhule",2050862,20.08,946,72.80,285),
 ("Jalna","jalna","Jalna","जालना",None,"AU","Jalna",1959046,21.46,937,71.52,254),
 ("Parbhani","parbhani","Parbhani","परभणी",None,"AU","Parbhani",1836086,20.19,947,73.34,295),
 ("Akola","akola","Akola","अकोला",None,"AM","Akola",1813906,11.27,946,88.05,320),
 ("Osmanabad","osmanabad","Dharashiv","धाराशिव","Osmanabad","AU","Dharashiv",1657576,11.50,924,78.44,219),
 ("Nandurbar","nandurbar","Nandurbar","नंदुरबार",None,"NS","Nandurbar",1648295,25.66,978,64.38,277),
 ("Ratnagiri","ratnagiri","Ratnagiri","रत्नागिरी",None,"KK","Ratnagiri",1615069,-4.82,1122,82.18,197),
 ("Gondiya","gondia","Gondia","गोंदिया",None,"NG","Gondia",1322507,10.14,999,84.95,253),
 ("Wardha","wardha","Wardha","वर्धा",None,"NG","Wardha",1300774,5.18,946,86.99,206),
 ("Bhandara","bhandara","Bhandara","भंडारा",None,"NG","Bhandara",1200334,5.65,982,83.76,294),
 ("Washim","washim","Washim","वाशिम",None,"AM","Washim",1197160,17.34,930,83.25,244),
 ("Hingoli","hingoli","Hingoli","हिंगोली",None,"AU","Hingoli",1177345,19.27,942,78.17,244),
 ("Gadchiroli","gadchiroli","Gadchiroli","गडचिरोली",None,"NG","Gadchiroli",1072942,10.58,982,74.36,74),
 ("Sindhudurg","sindhudurg","Sindhudurg","सिंधुदुर्ग",None,"KK","Oros",849651,-2.21,1036,85.56,163),
]
units=[]
for r in D:
    k,i,en,mr,old,z,hq,pop,gr,sr,lit,den=r
    a=pop/den
    units.append(dict(id=i,en=en,mr=mr,old=old,type="District",zone=z,cap=hq,pop=pop,gr=gr,sr=sr,lit=lit,den=den,area=int(round(a,-1))))
print(len(units), sum(u['pop'] for u in units), sum(u['area'] for u in units))
key={r[0]:r[1] for r in D}
json.dump(dict(units=units,key=key),open('mh_units.json','w'),ensure_ascii=False)
