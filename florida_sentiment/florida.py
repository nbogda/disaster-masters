#doin stuff in snake language

import csv
import os
import json
import datetime
from collections import defaultdict
import code
from textblob import TextBlob


date_dict = {}
sent_dict = {}


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
					sent_dict[post_date] = {}

					date_dict[post_date]["duke"] = 1.0 
					date_dict[post_date]["gru"] = 1.0
					date_dict[post_date]["keysenergy"] = 1.0 
					date_dict[post_date]["kua"] = 1.0
					date_dict[post_date]["mylkld"] = 1.0 
					date_dict[post_date]["jea"] = 1.0 
					date_dict[post_date]["ocala"] = 1.0 
					date_dict[post_date]["ouc"] = 1.0 
					date_dict[post_date]["tampa"] = 1.0
					date_dict[post_date]["fpl"] = 1.0

					sent_dict[post_date]["duke"] = 0.0 
					sent_dict[post_date]["gru"] = 0.0
					sent_dict[post_date]["fpl"] = 0.0
					sent_dict[post_date]["keysenergy"] = 0.0 
					sent_dict[post_date]["kua"] = 0.0 
					sent_dict[post_date]["mylkld"] = 0.0 
					sent_dict[post_date]["jea"] = 0.0
					sent_dict[post_date]["ocala"] = 0.0 
					sent_dict[post_date]["ouc"] = 0.0
					sent_dict[post_date]["tampa"] = 0.0 
				
				#get the sentiment of a tweet
				keyword = str(row[4])
				keyword = unicode(keyword, errors = "ignore")
				analysis = TextBlob(keyword)
				sentiment = analysis.sentiment.polarity

				#get the utility company associated with the tweet
				county = str(row[0]) 

				try:
					if "DukeEnergy" in county:
						date_dict[post_date]["duke"] += 1.0 
						sent_dict[post_date]["duke"] += sentiment
					if "GRU4U" in county:
						date_dict[post_date]["gru"] += 1.0 
						sent_dict[post_date]["gru"] += sentiment
					if "insideFPL" in county:
						date_dict[post_date]["fpl"] += 1.0 
						sent_dict[post_date]["fpl"] += sentiment
					if "KeysEnergy" in county:
						date_dict[post_date]["keysenergy"] += 1.0 
						sent_dict[post_date]["keysenergy"] += sentiment
					if "KUAdirect" in county:
						date_dict[post_date]["kua"] += 1.0 
						sent_dict[post_date]["kua"] += sentiment
					if "mylkldelectric" in county:
						date_dict[post_date]["mylkld"] += 1.0 
						sent_dict[post_date]["mylkld"] += sentiment
					if "NewsfromJEA" in county:
						date_dict[post_date]["jea"] += 1.0 
						sent_dict[post_date]["jea"] += sentiment
					if "OcalaCEP" in county:
						date_dict[post_date]["ocala"] += 1.0 
						sent_dict[post_date]["ocala"] += sentiment
					if "OUCreliableone" in county:
						date_dict[post_date]["ouc"] += 1.0 
						sent_dict[post_date]["ouc"] += sentiment
					if "TampaElectric" in county:
						date_dict[post_date]["tampa"] += 1.0 
						sent_dict[post_date]["tampa"] += sentiment
				except:
					print ("Keyerror")
					
			f.close()

#get the average sentiment per day
for p in sent_dict.keys():
	sent_dict[p]["duke"] /= date_dict[p]["duke"]
	sent_dict[p]["gru"] /= date_dict[p]["gru"]
	sent_dict[p]["fpl"] /= date_dict[p]["fpl"]
	sent_dict[p]["keysenergy"] /= date_dict[p]["keysenergy"]
	sent_dict[p]["kua"] /= date_dict[p]["kua"]
	sent_dict[p]["mylkld"] /= date_dict[p]["mylkld"]
	sent_dict[p]["jea"] /= date_dict[p]["jea"]
	sent_dict[p]["ocala"] /= date_dict[p]["ocala"]
	sent_dict[p]["ouc"] /= date_dict[p]["ouc"]
	sent_dict[p]["tampa"] /= date_dict[p]["tampa"]



#put in JSON
fp = open("florida_sent.json", "w") 
json_string = json.dumps([{"post_date" : key, "company" : value, "sentiment" : sentiment, "posts" : date_dict[key][value]} for key, value in sent_dict.iteritems() for value, sentiment in value.iteritems()])
fp.write(json_string)
fp.close()





