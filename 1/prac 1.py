# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:19:50 2020

@author: HETSHAH
"""


import csv
import pandas as pd
import requests
import lxml.html as lh

#read from csv
print('csv output')
with open('data.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)
        
print()
print()
print('excel output')
#read from excel
df = pd.read_excel (r'book1.xlsx')
print (df)



print()
print()

#read online

url='http://coredogs.com/lesson/web-page-tables.html'
page = requests.get(url)
doc = lh.fromstring(page.content)
tr_elements = doc.xpath('//tr')



tr_elements = doc.xpath('//tr')
col=[]
i=0

#getting the table headings
print('heading names')
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    print('%d:"%s"'%(i,name))
    col.append((name,[]))
    

#storing the data
for j in range(1,len(tr_elements)):
    T=tr_elements[j]
    i=0
    for t in T.iterchildren():
        data=t.text_content() 
        col[i][1].append(data)
        i+=1
        
print()
print('table parsed')
Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)
print(df.head())

print()
print( 'selecting dog breed with medium size')
print(df[df.Size == 'Medium'].Dog)

print()
print( 'selecting dog breed with name size more than 5')
print(df[df.Dog.str.len() >=5].Dog)


print()
print( 'selecting distinct dog breed sizes')
print(df.Size.unique())

print()
print( 'insert a row - Sunny, small, pug')
df = df.append({'Dog': 'Sunny', 'Size': 'Small', 'Breed':'pug'}, ignore_index=True)
print(df)


print()
print( 'delete  a row - with dog CC')
df= df[df.Dog != 'CC']
print(df)
