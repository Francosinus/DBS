import pandas as pd
import numpy as np
import re


df=pd.read_csv("/home/franko/Iter3/new-american-election.csv", delimiter=";", names=['handle','text','original_author','time','retweet_count','favorite_count'],header=None)

df_new=df.drop(['original_author'],axis=1)#zeile entfertnt


df_new.to_csv("/home/franko/Iter3/american-election.csv",sep=';')#speichern


hashtag = pd.DataFrame(columns=['name','anzahl'])#neuer Datensatz mit name und anzahl(hauefigkeit)
df_1 = df_new[df_new['text'].str.contains("#")]#nur den inhalt aus text behalten, der rauten enthaelt
hashtag['name'] = df_1['text']


hashtag.reset_index(drop=True)#verwerfen den Index, da 2 verschiedene hashtags in einem tweet verschiedene ids haben muessen

hashi=re.compile(r"#([a-zA-Z0-9]+)")#raute soll nicht gespeichert werden

tags=[]#liste erstellen

for i in hashtag['name']:#speichert eintreage in einer liste
	tags += [hashi.findall(i)]

sethash = set()#set erstellen und mit hashtags fuellen
for l in tags:
    for i in l:
	sethash.add(i)

df_tags = pd.DataFrame(columns=['name','anzahl'])#neuer datensatz
df_tags['name'] = list(sethash)#fuellen mit hashtags


def count(hashtags): #zaehlt wie oft der hashtag vorkommt
    count = 0
    for l in tags:
        if hashtags in l:
            count += 1
    return count

df_tags.anzahl = df_tags.name.apply(count)


df_tags.to_csv('hashtags.csv',sep=';')#speichern



df_contains = pd.DataFrame(columns=['t_id','h_id'])#neuer contains datensatz

cont = df_new[df_new['text'].str.contains("#")]
cont2 = cont.drop(['handle','time','retweet_count','favorite_count'],axis=1)
cont2['text'] = tags

cont2.drop(cont2.index[len(cont2)-1])#reihe mit leerem hashtag loeschen

liste=[]#liste erstellen
for idx, x in cont2['text'].iteritems():#hashtags tweet id hinzufuegen
    for k in x:
	liste.append(idx)
liste2 = []#noch eine liste
for l in cont2['text']:#fue jeden hashtag die hashtag id einfuegen
    for m in l:
        liste2.append(df_tags[df_tags['name'] == m].index.tolist())


df_contains['h_id'] = [lis[0] for lis in liste2]#in entsprechender zeile speichern

df_contains['t_id'] = liste

df_contains.to_csv('contains.csv', sep=';')#speichern 


df_pairs = pd.DataFrame(columns=['h_id1','h_id2'])#jetzt noch paarweises auftreten 


h_id1 = []
h_id2 = []

#durch die tweet liste gehen
#fuege jeweils in listen ein
for idx,x in cont2['text'].iteritems():
    if len(x) >= 2:
        i=0
        while i<len(x):
            j=i+1
            while j<len(x):
                id1 = df_tags[df_tags['name'] == x[i]].index.tolist()
                id2 = df_tags[df_tags['name'] == x[j]].index.tolist()
                h_id1.append(id1[0])
                h_id2.append(id2[0])
		
                j += 1
	    i +=1

#listen in datensatz
df_pairs['h_id1'] = h_id1
df_pairs['h_id2'] = h_id2

df_pairs.to_csv('paare.csv',sep=';')
