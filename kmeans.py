import numpy as np
import sklearn.cluster
import distance
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import matplotlib.pyplot as plt
import pandas as pd

#wir lesen die hashtags aus iteration 2 ein, diese csv enthaelt alle vorkommenden hashtags(also mit duplikaten)<-wichtig, da vectorizer die haeufigkeit analysiert
df=pd.read_csv("/home/franko/Iter3/hash.csv", names=['name'], delimiter=';')

#zunaechst werden die hashtags in einer liste gespeichert
column = []
for i in df['name']:
    for j in i.split():
        if j not in column:
           column.append(j)


vectorizer = TfidfVectorizer(lowercase=True) #vectorisiert text string zu numerisch

X = vectorizer.fit_transform(column)#analysiert die haeufigkeit der auftretenden hashtags und erstellt eine Matrix

truncated = TruncatedSVD(n_components=2, n_iter=10).fit_transform(X)#SVD reduziert die Anzahl der Dimensionen

#hier wird die Anzahl der Dimensionen nochmal auf 2 reduziert (fuer plot notwendig)
tsne = TSNE(n_components=2, random_state=3).fit_transform(truncated)
print(tsne)


cluster=9#wir bestimmen die anzahl der cluster
km = KMeans(n_clusters=cluster).fit_predict(tsne)#kmeans wird auf die haeufigkeitsmatrix mit 2 dimensionen angewendet 

#wir erstellen einen 2 dimensionalen plot der unseren k-means darstellt
plt.scatter(tsne[:, 0], tsne[:, 1], c=km)

#wir erstellen ein dictionary und lassen uns die cluster anzeigen
clusters = {
    0: [], 1: [], 2:[], 3: [], 4: [], 5: [], 6: [], 7:[], 8: [], 9:[],
}
for i, cluster in enumerate(km):
    clusters[cluster].append(df.ix[i, 'name'])

print(clusters)

plt.show()








