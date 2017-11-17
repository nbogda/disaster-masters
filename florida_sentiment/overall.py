#doin stuff in snake language

import csv
import os
import json
import datetime
from collections import defaultdict
import code
from textblob import TextBlob


date_dict = {}


date_dict["duke"] = {} 
date_dict["gru"] = {}
date_dict["keysenergy"] = {} 
date_dict["kua"] = {}
date_dict["mylkld"] = {}
date_dict["jea"] = {}
date_dict["ocala"] = {} 
date_dict["ouc"] = {}
date_dict["tampa"] = {}
date_dict["fpl"] = {}


date_dict["duke"]["positive"] = 0 
date_dict["duke"]["neutral"] = 0 
date_dict["duke"]["negative"] = 0 
date_dict["gru"]["positive"] = 0
date_dict["gru"]["neutral"] = 0
date_dict["gru"]["negative"] = 0
date_dict["keysenergy"]["positive"] = 0
date_dict["keysenergy"]["neutral"] = 0
date_dict["keysenergy"]["negative"] = 0
date_dict["kua"]["positive"] = 0
date_dict["kua"]["neutral"] = 0
date_dict["kua"]["negative"] = 0
date_dict["mylkld"]["positive"] = 0
date_dict["mylkld"]["neutral"] = 0
date_dict["mylkld"]["negative"] = 0
date_dict["jea"]["positive"] = 0
date_dict["jea"]["neutral"] = 0
date_dict["jea"]["negative"] = 0
date_dict["ocala"]["positive"] = 0 
date_dict["ocala"]["neutral"] = 0 
date_dict["ocala"]["negative"] = 0 
date_dict["ouc"]["positive"] = 0
date_dict["ouc"]["neutral"] = 0
date_dict["ouc"]["negative"] = 0
date_dict["tampa"]["positive"] = 0
date_dict["tampa"]["neutral"] = 0
date_dict["tampa"]["negative"] = 0
date_dict["fpl"]["positive"] = 0
date_dict["fpl"]["neutral"] = 0
date_dict["fpl"]["negative"] = 0


positive = 0
negative = 0
neutral = 0


for dirs, subdirs, files in os.walk("../data/florida"):
	for fname in files:
		if fname.endswith(".csv"): 
			f = open(dirs + "/" + fname, "r")
			name = str(fname)
			csv_f = csv.reader(f)
			next(csv_f, None) #skip header
			for row in csv_f:

				
				#get the sentiment of a tweet
				keyword = str(row[4])
				keyword = unicode(keyword, errors = "ignore")
				analysis = TextBlob(keyword)
				sentiment = analysis.sentiment.polarity
				sentiment_val = ""
				if (sentiment <= -0.1):
					sentiment_val = "negative"
					negative += 1
				if (sentiment > -0.1 and sentiment < 0.1):
					sentiment_val = "neutral"
					neutral += 1
				if (sentiment >= 0.1):
					sentiment_val = "positive"
					positive += 1
				
				
				#get the utility company associated with the tweet
				county = str(row[0]) 

				
				if "DukeEnergy" in county:
					date_dict["duke"][sentiment_val] += 1.0  
				if "GRU4U" in county:
					date_dict["gru"][sentiment_val] += 1.0 
				if "insideFPL" in county:
					date_dict["fpl"][sentiment_val] += 1.0 
				if "KeysEnergy" in county:
					date_dict["keysenergy"][sentiment_val] += 1.0 
				if "KUAdirect" in county:
					date_dict["kua"][sentiment_val] += 1.0 
				if "mylkldelectric" in county:
					date_dict["mylkld"][sentiment_val] += 1.0 
				if "NewsfromJEA" in county:
					date_dict["jea"][sentiment_val] += 1.0 
				if "OcalaCEP" in county:
					date_dict["ocala"][sentiment_val] += 1.0 
				if "OUCreliableone" in county:
					date_dict["ouc"][sentiment_val] += 1.0 
				if "TampaElectric" in county:
					date_dict["tampa"][sentiment_val] += 1.0 
					
			f.close()


print positive, negative, neutral


#put in JSON
#fp = open("florida_sent.json", "w") 
#json_string = json.dumps([{"post_date" : key, "company" : value, "sentiment" : sentiment, "posts" : date_dict[key][value]} for key, value in sent_dict.iteritems() for value, sentiment in value.iteritems()])
#fp.write(json_string)
#fp.close()





