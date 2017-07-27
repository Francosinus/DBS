import csv


in_file = open("C:/Users/topsen/Desktop/CSV/morerowhashtag.csv","r") 
out_file= open("C:/Users/topsen/Desktop/CSV/edges2.csv","wb" )

reader = csv.reader(in_file,delimiter=";")
writer = csv.writer(out_file,delimiter=";")

duplicates = set()
count = 0
index = ["index"]

for row in reader:
	if row[0] not in duplicates:
		writer.writerow([index[len(index)-1],row[0]])
		duplicates.add(row[0])
		index.append(count)
		count += 1

in_file.close()
out_file.close()
