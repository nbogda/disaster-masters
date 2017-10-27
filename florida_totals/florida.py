#doin stuff in snake language

import csv
import os
import json
import datetime
from collections import defaultdict
import code
from textblob import TextBlob


date_dict = {}


#parse files

for dirs, subdirs, files in os.walk("../data/florida"):
	for fname in files:
		if fname.endswith(".csv"): 
			f = open(dirs + "/" + fname, "r")
			name = str(fname)
			csv_f = csv.reader(f)
			next(csv_f, None) #skip header
			for row in csv_f:
				post_date = str((row[1]).partition(" ")[0])
				if (post_date not in date_dict): 

					date_dict[post_date] = {}

					date_dict[post_date]["duke"] = 0 
					date_dict[post_date]["gru"] = 0
					date_dict[post_date]["keysenergy"] = 0
					date_dict[post_date]["kua"] = 0
					date_dict[post_date]["mylkld"] = 0 
					date_dict[post_date]["jea"] = 0 
					date_dict[post_date]["ocala"] = 0 
					date_dict[post_date]["ouc"] = 0 
					date_dict[post_date]["tampa"] = 0
					date_dict[post_date]["fpl"] = 0

				county = str(row[0]) 

				try:
					if "DukeEnergy" in county:
						date_dict[post_date]["duke"] += 1.0 
					if "GRU4U" in county:
						date_dict[post_date]["gru"] += 1.0 
					if "insideFPL" in county:
						date_dict[post_date]["fpl"] += 1.0 
					if "KeysEnergy" in county:
						date_dict[post_date]["keysenergy"] += 1.0 
					if "KUAdirect" in county:
						date_dict[post_date]["kua"] += 1.0 
					if "mylkldelectric" in county:
						date_dict[post_date]["mylkld"] += 1.0 
					if "NewsfromJEA" in county:
						date_dict[post_date]["jea"] += 1.0 
					if "OcalaCEP" in county:
						date_dict[post_date]["ocala"] += 1.0 
					if "OUCreliableone" in county:
						date_dict[post_date]["ouc"] += 1.0 
					if "TampaElectric" in county:
						date_dict[post_date]["tampa"] += 1.0 
				except:
					print ("Keyerror")
					
			f.close()



#put in JSON
fp = open("florida_totals.json", "w") 
json_string = json.dumps([{"post_date" : key, "company" : value, "posts" : posts} for key, value in date_dict.iteritems() for value, posts in value.iteritems()])
fp.write(json_string)
fp.close()





