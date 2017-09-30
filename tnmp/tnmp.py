#for mainstream media only

import csv
import os
import json
import datetime
from collections import defaultdict
from textblob import TextBlob
import code


date_dict = {}
counter_dict = {}

#parse files

for dirs, subdirs, files in os.walk("."):
	for fname in files:
		if fname.endswith(".csv"): 
			f = open(dirs + "/" + fname, "r")
			csv_f = csv.reader(f)
			next(csv_f, None) #skip header
			for row in csv_f:
				post_date = str((row[1]).partition(" ")[0])
				if (post_date not in date_dict): 
					date_dict[post_date] = {}
					date_dict[post_date] = 0.0
					counter_dict[post_date] = {}
					counter_dict[post_date] = 0
				keyword = str(row[4])
				keyword = unicode(keyword, errors = "ignore")
				analysis = TextBlob(keyword)
				sentiment = analysis.sentiment.polarity
				try:
					date_dict[post_date] += sentiment
					counter_dict[post_date] += 1
				except:
					print ("Keyerror")

			f.close()


#get the average sentiment for that day
for p in date_dict.keys():
	date_dict[p] /= counter_dict[p]

#put in JSON
fp = open("tnmp.json", "w") 
json_string = json.dumps([{"post_date" : key, "sentiment" : value, "posts" : counter_dict[key]} for key, value in date_dict.iteritems()])
fp.write(json_string)
fp.close()





