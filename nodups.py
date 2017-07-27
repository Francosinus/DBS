import csv


in_file = open("C:/Users/topsen/Desktop/CSV/onerowhashtag.csv","r") 
out_file= open("C:/Users/topsen/Desktop/CSV/noduplicates.csv","wb" )

reader = csv.reader(in_file,delimiter=";")
writer = csv.writer(out_file,delimiter=";")

duplicates = set()

for row in reader:
	if row[0] not in duplicates:
		writer.writerow([row[0]])
		duplicates.add(row[0])

in_file.close()
out_file.close()
