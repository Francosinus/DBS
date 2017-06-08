from bs4 import BeautifulSoup
import requests
import csv
import collections
import re

def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj


def main():

	fobj = open('heise.csv', 'w')      # open file
	csvw = csv.writer(fobj, delimiter = ';')# create csv writer, set delimiter to ;

	for page in range (0,4,1):

		url_heise= "https://www.heise.de/thema/https?seite="

		content = getPage(url_heise+str(page)+" ").find_all("header")
	 
		for t in range(2,32,1):
			temp_content = content[t].string
			if temp_content != None:
				temp_content = temp_content.encode("utf8")
				csvw.writerow([temp_content])
				#print (temp_content)

	fobj.close()  

	words= re.findall('\w+', open('heise.csv').read(),re.UNICODE)
	print collections.Counter(words).most_common(3)

if __name__ == '__main__':
    main()


