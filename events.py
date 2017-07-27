import stringdist
import csv
import re
import random
import ast
from os import path
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pylab import *

inpute = open("C:/Users/topsen/Desktop/CSV/hashtagnew.csv","r")
output = open("C:/Users/topsen/Desktop/CSV/Event.csv","wb")
#output2 = open("C:/Users/topsen/Desktop/CSV/Shorts.txt","wb")
#output3 = open("C:/Users/topsen/Desktop/CSV/Events.txt","wb")

#media_tags = ["CNN","MSNBC","Fox","rt","NBC"]
reader = csv.reader(inpute,delimiter=";")
output = csv.writer(output,delimiter=";")
#output2 = txt.writer(output2)
#output3 = txt.writer(outpu3)
media_liste = []
for row in reader:
	event = row[1].lower() 
	event = re.findall(r'\b\S*ebate\S*\b' ,event) or re.findall(r'\b\S*rnc\S*\b' ,event) or re.findall(r'\b\S*dnc\S*\b' ,event) \
	or re.findall(r'\b\S*dems\S*\b' ,event) \
	or re.findall(r'\b\S*day\S*\b' ,event) \
	or re.findall(r'\b\S*convention\S*\b' ,event)
	#event= re.sub(r'#',r'',event)
	if event:
		print event
		output.writerow(event)
	#media_liste.append(event)   

#matches = []

#word= "Trump"

#for word in media_liste:
 #       regex = r'' + re.escape(word)
   #     match = re.search(regex, word)
  #      if match:
    #        matches.append(word)
 

#print matches
#output.close()
inpute.close()