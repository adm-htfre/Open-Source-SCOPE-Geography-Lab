import json
# Census of India 2011 (final Primary Census Abstract). Units are the 35 States/UTs as they stood in 2011.
# id, name, marathi, type, zone, population, male, female, sexratio, literacy, growth(2001-11 %), area km2, capital
U = [
 ("jk","Jammu & Kashmir","जम्मू आणि काश्मीर","State","N",12541302,6640662,5900640,889,67.16,23.64,222236,"Srinagar / Jammu"),
 ("hp","Himachal Pradesh","हिमाचल प्रदेश","State","N",6864602,3481873,3382729,972,82.80,12.94,55673,"Shimla"),
 ("pb","Punjab","पंजाब","State","N",27743338,14639465,13103873,895,75.84,13.89,50362,"Chandigarh"),
 ("ch","Chandigarh","चंदीगड","UT","N",1055450,580663,474787,818,86.05,17.19,114,"Chandigarh"),
 ("uk","Uttarakhand","उत्तराखंड","State","C",10086292,5137773,4948519,963,78.82,18.81,53483,"Dehradun (winter), Gairsain (summer)"),
 ("hr","Haryana","हरियाणा","State","N",25351462,13494734,11856728,879,75.55,19.90,44212,"Chandigarh"),
 ("dl","Delhi","दिल्ली","UT","N",16787941,8987326,7800615,868,86.21,21.21,1483,"New Delhi"),
 ("rj","Rajasthan","राजस्थान","State","N",68548437,35550997,32997440,928,66.11,21.31,342239,"Jaipur"),
 ("up","Uttar Pradesh","उत्तर प्रदेश","State","C",199812341,104480510,95331831,912,67.68,20.23,240928,"Lucknow"),
 ("br","Bihar","बिहार","State","E",104099452,54278157,49821295,918,61.80,25.42,94163,"Patna"),
 ("sk","Sikkim","सिक्कीम","State","NE",610577,323070,287507,890,81.42,12.89,7096,"Gangtok"),
 ("ar","Arunachal Pradesh","अरुणाचल प्रदेश","State","NE",1383727,713912,669815,938,65.38,26.03,83743,"Itanagar"),
 ("nl","Nagaland","नागालँड","State","NE",1978502,1024649,953853,931,79.55,-0.58,16579,"Kohima"),
 ("mn","Manipur","मणिपूर","State","NE",2570390,1290171,1280219,992,76.94,24.50,22327,"Imphal"),
 ("mz","Mizoram","मिझोराम","State","NE",1097206,555339,541867,976,91.33,23.48,21081,"Aizawl"),
 ("tr","Tripura","त्रिपुरा","State","NE",3673917,1874376,1799541,960,87.22,14.84,10486,"Agartala"),
 ("ml","Meghalaya","मेघालय","State","NE",2966889,1491832,1475057,989,74.43,27.95,22429,"Shillong"),
 ("as","Assam","आसाम","State","NE",31205576,15939443,15266133,958,72.19,17.07,78438,"Dispur"),
 ("wb","West Bengal","पश्चिम बंगाल","State","E",91276115,46809027,44467088,950,76.26,13.84,88752,"Kolkata"),
 ("jh","Jharkhand","झारखंड","State","E",32988134,16930315,16057819,948,66.41,22.42,79716,"Ranchi"),
 ("od","Odisha","ओडिशा","State","E",41974218,21212136,20762082,979,72.87,14.05,155707,"Bhubaneswar"),
 ("cg","Chhattisgarh","छत्तीसगड","State","C",25545198,12832895,12712303,991,70.28,22.61,135192,"Raipur"),
 ("mp","Madhya Pradesh","मध्य प्रदेश","State","C",72626809,37612306,35014503,931,69.32,20.35,308252,"Bhopal"),
 ("gj","Gujarat","गुजरात","State","W",60439692,31491260,28948432,919,78.03,19.28,196244,"Gandhinagar"),
 ("dd","Daman & Diu","दमण आणि दीव","UT","W",243247,150301,92946,618,87.10,53.76,111,"Daman"),
 ("dn","Dadra & Nagar Haveli","दादरा आणि नगर हवेली","UT","W",343709,193760,149949,774,76.24,55.88,491,"Silvassa"),
 ("mh","Maharashtra","महाराष्ट्र","State","W",112374333,58243056,54131277,929,82.34,15.99,307713,"Mumbai (Nagpur – winter)"),
 ("ap","Andhra Pradesh","आंध्र प्रदेश","State","S",84580777,42442146,42138631,993,67.02,10.98,275045,"Hyderabad (in 2011)"),
 ("ka","Karnataka","कर्नाटक","State","S",61095297,30966657,30128640,973,75.36,15.60,191791,"Bengaluru"),
 ("ga","Goa","गोवा","State","W",1458545,739140,719405,973,88.70,8.23,3702,"Panaji"),
 ("ld","Lakshadweep","लक्षद्वीप","UT","S",64473,33123,31350,946,91.85,6.30,32,"Kavaratti"),
 ("kl","Kerala","केरळ","State","S",33406061,16027412,17378649,1084,94.00,4.91,38852,"Thiruvananthapuram"),
 ("tn","Tamil Nadu","तमिळनाडू","State","S",72147030,36137975,36009055,996,80.09,15.61,130060,"Chennai"),
 ("py","Puducherry","पुदुच्चेरी","UT","S",1247953,612511,635442,1037,85.85,28.08,490,"Puducherry"),
 ("an","Andaman & Nicobar Islands","अंदमान आणि निकोबार बेटे","UT","S",380581,202871,177710,876,86.63,6.86,8249,"Port Blair (Sri Vijaya Puram)"),
]
units=[]
for u in U:
    d=dict(id=u[0],en=u[1],mr=u[2],type=u[3],zone=u[4],pop=u[5],male=u[6],female=u[7],sr=u[8],lit=u[9],gr=u[10],area=u[11],cap=u[12])
    assert d['male']+d['female']==d['pop'], d['en']
    d['den']= round(d['pop']/d['area'])
    units.append(d)
for d in units:
    if d['id']=='jk': d['den']=124  # Census computes J&K density on area under Indian administration (1,01,387 km²)
print(len(units), sum(d['pop'] for d in units), sum(d['area'] for d in units))
# map feature name -> (unit id, today's label, today's mr label, note)
F = {
 'Jammu & Kashmir':('jk',None,None,'Since 2019 a Union Territory. In 2011 it was one State that also included Ladakh.'),
 'Ladakh':('jk','Ladakh','लडाख','Became a separate Union Territory in 2019. In the 2011 Census it was part of Jammu & Kashmir, so the figures shown are for the combined State.'),
 'Telangana':('ap','Telangana','तेलंगणा','Formed in 2014 from Andhra Pradesh. In the 2011 Census it was part of Andhra Pradesh, so the figures shown are for undivided Andhra Pradesh.'),
 'Andhra Pradesh':('ap',None,None,'Telangana was separated from Andhra Pradesh in 2014. Figures are for undivided Andhra Pradesh (2011).'),
 'Daman & Diu':('dd',None,None,'Merged with Dadra & Nagar Haveli into one Union Territory in 2020.'),
 'Dadra & Nagar Haveli':('dn',None,None,'Merged with Daman & Diu into one Union Territory in 2020.'),
 'Andaman & Nicobar':('an',None,None,None),
}
paths=json.load(open('paths.json'))
names={d['en']:d['id'] for d in units}
feat=[]
for k,v in paths.items():
    if k in F: uid,lab,labmr,note=F[k]
    else:
        uid=names.get(k) or {'Odisha':'od'}.get(k); lab=labmr=note=None
    assert uid, k
    feat.append(dict(k=k,u=uid,lab=lab,mr=labmr,note=note,d=v['d'],c=v['c']))
assert {f['u'] for f in feat}=={d['id'] for d in units}
json.dump(dict(units=units,feat=feat),open('bundle.json','w'),ensure_ascii=False,separators=(',',':'))
