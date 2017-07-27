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

reader = csv.reader(inpute,delimiter=";")
output = csv.writer(output,delimiter=";")

media_liste = []
for row in reader:
	event = row[1].lower() 
	event = re.findall(r'\b\S*ebate\S*\b' ,event) or re.findall(r'\b\S*rnc\S*\b' ,event) or
	re.findall(r'\b\S*dnc\S*\b' ,event) \
	or re.findall(r'\b\S*dems\S*\b' ,event) \
	or re.findall(r'\b\S*day\S*\b' ,event) \
	or re.findall(r'\b\S*convention\S*\b' ,event)

	if event:
		print event
		output.writerow(event)
	#media_liste.append(event)   

inpute.close()
