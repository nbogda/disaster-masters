
import csv
import os
import json
import datetime
from collections import defaultdict
import code


date_dict = {}

#parse files

community = 0
globalwarming = 0
government = 0
poweroutage = 0
utility = 0
temp = 0
hurricane = 0
monopoly = 0
storm = 0
flood = 0
trust = 0
poor = 0
damage = 0
disaster = 0
homes = 0

for dirs, subdirs, files in os.walk("../../data/florida"):
	for fname in files:
		if fname.endswith(".csv"): 
			f = open(dirs + "/" + fname, "r")
			csv_f = csv.reader(f)
			next(csv_f, None) #skip header
			for row in csv_f:
				post_date = str((row[1]).partition(" ")[0])
				if (post_date not in date_dict): 
					date_dict[post_date] = {}
					date_dict[post_date]["community"] = 0 #
					date_dict[post_date]["climate"] = 0 #
					date_dict[post_date]["outage"] = 0 #
					date_dict[post_date]["temperature"] = 0 #
					date_dict[post_date]["trust"] = 0 #
					date_dict[post_date]["poor"] = 0 #
					date_dict[post_date]["inequality"] = 0 #
					date_dict[post_date]["utility"] = 0
					date_dict[post_date]["hurricane"] = 0 #
					date_dict[post_date]["monopoly"] = 0 #
					date_dict[post_date]["flood"] = 0 #
					date_dict[post_date]["storm"] = 0 #
					date_dict[post_date]["disaster"] = 0 #
					date_dict[post_date]["government"] = 0 #
					date_dict[post_date]["damage"] = 0 #
					date_dict[post_date]["home"] = 0 #
#					date_dict[post_date]["power"] = 0 #
				keyword = str(row[4])
			#	try:
					#here's yer keywordz 
				if "community" in keyword.lower() or "communities" in keyword.lower() or "small towns" in keyword.lower() or "rural" in keyword.lower():
					date_dict[post_date]["community"] += 1
					community += 1
				if "global warming" in keyword.lower() or "climate change" in keyword.lower() or "greenhouse gases" in keyword.lower():
					date_dict[post_date]["climate"] += 1
					globalwarming += 1
				if "power outage" in keyword.lower() or "breakout" in keyword.lower() or "electricity" in keyword.lower():
					date_dict[post_date]["outage"] += 1
					poweroutage += 1
				if "temperature" in keyword.lower() or "heat" in keyword.lower() or "temp " in keyword.lower():
					date_dict[post_date]["temperature"] += 1
					temp += 1
				if "trust" in keyword.lower():
					date_dict[post_date]["trust"] += 1
					trust += 1
				if "low income" in keyword.lower() or "poor" in keyword.lower() or "poverty" in keyword.lower() or "impoverished" in keyword.lower():
					date_dict[post_date]["poor"] += 1
					poor += 1
				if "government" in keyword.lower():
					date_dict[post_date]["government"] += 1
					government += 1
				if "hurricane" in keyword.lower():
					date_dict[post_date]["hurricane"] += 1
					hurricane += 1
				if "disaster" in keyword.lower() or "crisis" in keyword.lower():
					date_dict[post_date]["disaster"] += 1
					disaster += 1
				if "monopoly" in keyword.lower() or "control" in keyword.lower():
					date_dict[post_date]["monopoly"] += 1
					monopoly += 1
				if "utilities" in keyword.lower() or "utility companies" in keyword.lower() or "utility" in keyword.lower():
					date_dict[post_date]["utility"] += 1
					utility += 1
				if "flood" in keyword.lower() or "heavy rain" in keyword.lower():
					date_dict[post_date]["flood"] += 1
					flood += 1
				if "stormy weather" in keyword.lower() or "storm" in keyword.lower():
					date_dict[post_date]["storm"] += 1
					storm += 1
				if "damage" in keyword.lower():
					date_dict[post_date]["damage"] += 1
					damage += 1
				if "house" in keyword.lower() or "home" in keyword.lower() or "houses" in keyword.lower() or "homes" in keyword.lower():
					homes += 1
					date_dict[post_date]["home"] += 1
			#	if "power" in keyword.lower() or "power grid" in keyword.lower():
			#		date_dict[post_date]["power"] += 1
				
			#	except:
			#		print ("")

			f.close()


print date_dict["2017-09-12"]["home"], "homes"
print date_dict["2017-09-12"]["hurricane"], "hurricane"
print date_dict["2017-09-12"]["damage"], "damage"
print date_dict["2017-09-12"]["outage"], "outage"




#put in JSON
fp = open("florida_freq.json", "w") 
json_string = json.dumps([{"post_date" : key, "keyword" : value, "posts" : n_posts} for key, value in date_dict.iteritems() for value, n_posts in value.iteritems()])
fp.write(json_string)
fp.close()





