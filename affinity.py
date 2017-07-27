import numpy as np
import sklearn.cluster
import distance
import csv

inpute = open("/home/franko/DBS Projekt/noduplicates.csv","r")
reader=csv.reader(inpute, delimiter=";")
output=open("/home/franko/DBS Projekt/cluster.csv", "w")
writer= csv.writer(output)
column= []
for row in reader:
	column.append(row[0])
  

words = np.asarray(column) #zum indizieren der Liste
lev = -1*np.array([[distance.levenshtein(w1,w2) for w1 in words] for w2
in words])#levenshtein distanz vergleich mit allen woertern

ap = sklearn.cluster.AffinityPropagation(affinity="precomputed", damping=0.5)#aehnlich wie kmeans
ap.fit(lev)
for cluster_id in np.unique(ap.labels_):
    exemplar = words[ap.cluster_centers_indices_[cluster_id]]
    cluster = np.unique(words[np.nonzero(ap.labels_==cluster_id)])
    cluster_str = ", ".join(cluster)
    writer.writerow([" - *%s:* %s" % (exemplar, cluster_str)])
    print(" - *%s:* %s" % (exemplar, cluster_str))



