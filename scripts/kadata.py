import json
# map dtname: (id, name, marathi, division, HQ, pop, growth, sexratio, literacy, density)  Census 2011, 30 districts
D=[
("Bangalore","blrurban","Bengaluru Urban","बंगळूरु शहर","BL","Bengaluru",9621551,47.18,916,87.67,4381),
("Belagavi","belagavi","Belagavi","बेळगाव","BG","Belagavi",4779661,13.41,973,73.48,356),
("Mysuru","mysuru","Mysuru","म्हैसूर","MY","Mysuru",3001127,13.63,985,72.79,476),
("Tumakuru","tumakuru","Tumakuru","तुमकूर","BL","Tumakuru",2678980,3.65,984,75.14,253),
("Kalaburagi","kalaburagi","Kalaburagi","कलबुर्गी","KB","Kalaburagi",2566326,18.01,971,64.85,234),
("Ballari","ballari","Ballari","बळ्ळारी","KB","Ballari",2452595,20.99,983,67.43,290),
("Vijayapura","vijayapura","Vijayapura","विजापूर","BG","Vijayapura",2177331,20.50,960,67.15,207),
("Dakshina Kannada","dkannada","Dakshina Kannada","दक्षिण कन्नड","MY","Mangaluru",2089649,10.11,1020,88.57,430),
("Davanagere","davanagere","Davanagere","दावणगेरे","BL","Davanagere",1945497,8.63,972,75.74,328),
("Raichur","raichur","Raichur","रायचूर","KB","Raichur",1928812,15.51,1000,59.56,228),
("Bagalkote","bagalkote","Bagalkote","बागलकोट","BG","Bagalkote",1889752,14.40,989,68.82,288),
("Dharwad","dharwad","Dharwad","धारवाड","BG","Dharwad",1847023,15.13,971,80.00,434),
("Mandya","mandya","Mandya","मंड्या","MY","Mandya",1805769,2.38,995,70.40,364),
("Hassan","hassan","Hassan","हासन","MY","Hassan",1776421,3.18,1010,76.07,261),
("Shivamogga","shivamogga","Shivamogga","शिवमोग्गा","BL","Shivamogga",1752753,6.71,998,80.45,207),
("Bidar","bidar","Bidar","बीदर","KB","Bidar",1703300,13.37,956,70.51,313),
("Chitradurga","chitradurga","Chitradurga","चित्रदुर्ग","BL","Chitradurga",1659456,9.33,974,73.71,197),
("Haveri","haveri","Haveri","हावेरी","BG","Haveri",1597668,11.02,950,77.40,331),
("Kolar","kolar","Kolar","कोलार","BL","Kolar",1536401,10.77,979,74.39,386),
("Uttara Kannada","ukannada","Uttara Kannada","उत्तर कन्नड","BG","Karwar",1437169,6.17,979,84.06,140),
("Koppal","koppal","Koppal","कोप्पळ","KB","Koppal",1389920,16.21,986,68.09,250),
("Chikkaballapura","chikkaballapura","Chikkaballapura","चिक्कबळ्ळापूर","BL","Chikkaballapura",1255104,9.23,972,69.76,296),
("Udupi","udupi","Udupi","उडुपी","MY","Udupi",1177361,5.85,1094,86.24,329),
("Yadgir","yadgir","Yadgir","यादगीर","KB","Yadgir",1174271,22.81,989,51.83,223),
("Chikkamagaluru","chikkamagaluru","Chikkamagaluru","चिक्कमगळूर","MY","Chikkamagaluru",1137961,-0.26,1008,79.25,158),
("Ramanagara","ramanagara","Ramanagara","रामनगर","BL","Ramanagara",1082636,5.05,976,69.22,308),
("Gadag","gadag","Gadag","गदग","BG","Gadag",1064570,9.54,982,75.12,229),
("Chamarajanagara","chamarajanagara","Chamarajanagara","चामराजनगर","MY","Chamarajanagara",1020791,5.73,993,61.43,181),
("Bengaluru Rural","blrrural","Bengaluru Rural","बंगळूरु ग्रामीण","BL","Bengaluru",990923,16.45,946,77.93,431),
("Kodagu","kodagu","Kodagu","कोडगू","MY","Madikeri",554519,1.09,1019,82.61,135),
]
units=[dict(id=r[1],en=r[2],mr=r[3],old=None,type="District",zone=r[4],cap=r[5],pop=r[6],gr=r[7],sr=r[8],lit=r[9],den=r[10],area=int(round(r[6]/r[10],-1))) for r in D]
print(len(units), sum(u['pop'] for u in units), sum(u['area'] for u in units))
key={r[0]:r[1] for r in D}
json.dump(dict(units=units,key=key),open('ka_units.json','w'),ensure_ascii=False)
