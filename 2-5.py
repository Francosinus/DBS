import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()

df= pd.read_csv("/home/franko/Iter3/zeit.csv",names=['anzahl','zeit','name'], delimiter=';',index_col=False)
df_new=pd.DataFrame()
lst = df['name'].str.split().tolist()
df_new['name']= [item[0] for item in lst]
df_new['zeit']=df['zeit']
df_new['anzahl']=df['anzahl']


inpute = raw_input("Hashtag: ")
tabl=df_new[df_new['name']==inpute]
#print(tabl)


if tabl['name'].tolist() != []:
  anzahl=tabl['anzahl'].tolist()
  zeit=tabl['zeit'].tolist()
  y=np.arange(len(zeit))
  figure=plt.figure()
  plt.bar(y, anzahl,color='r')
  plt.xticks(y, zeit, rotation=90)
  plt.xlabel('Datum')
  plt.ylabel('Hashtag')
  plt.show()

else:
  print ("Exisitiert nicht")
