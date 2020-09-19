# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:18:40 2020

@author: HETSHAH
"""


import pandas as pd;
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression;
from sklearn.metrics import mean_absolute_error 
from sklearn.metrics import mean_squared_error 


print("start")
iris = load_iris()

iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
target_df= pd.DataFrame(data=iris.target, columns=['species'])

def converter(specie):
    if(specie == 0):
        return 'setosa'
    elif specie == 1:
        return 'versicolor'
    else:
        return 'virginica'
    
target_df['species']=target_df['species'].apply(converter)

iris_df = pd.concat([iris_df,target_df],axis=1)

iris_df.info();

sns.pairplot(iris_df, hue= 'species')
iris_df.drop('species', axis= 1, inplace= True)
target_df = pd.DataFrame(columns= ['species'], data= iris.target)
iris_df = pd.concat([iris_df, target_df], axis= 1)


X= iris_df.drop(labels= 'sepal length (cm)', axis= 1)
y= iris_df['sepal length (cm)']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.33, random_state= 101)

lr = LinearRegression()

#train
lr.fit(X_train, y_train)

#predict
lr.predict(X_test)
pred = lr.predict(X_test)


print('Mean Absolute Error:', mean_absolute_error(y_test, pred))
print('Mean Squared Error:', mean_squared_error(y_test, pred))
print('Mean Root Squared Error:', np.sqrt(mean_squared_error(y_test, pred)))
print("stop")





import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas.util.testing as tm


data = sns.load_dataset("iris")
data.head()
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
plt.xlabel('Features')
plt.ylabel('Species')

pltX = data.loc[:, 'sepal_length']
pltY = data.loc[:,'species']
plt.scatter(pltX, pltY, color='blue', label='sepal_length')

pltX = data.loc[:, 'sepal_width']
pltY = data.loc[:,'species']
plt.scatter(pltX, pltY, color='green', label='sepal_width')

pltX = data.loc[:, 'petal_length']
pltY = data.loc[:,'species']
plt.scatter(pltX, pltY, color='red', label='petal_length')

pltX = data.loc[:, 'petal_width']
pltY = data.loc[:,'species']
plt.scatter(pltX, pltY, color='black', label='petal_width')

plt.legend(loc=4, prop={'size':8})
plt.show()

#Split the data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train the model
model = LogisticRegression()
model.fit(x_train, y_train) #Training the model

#Test the model
predictions = model.predict(x_test)
print(predictions)# printing predictions

print()# Printing new line

#Check precision, recall, f1-score
print( classification_report(y_test, predictions) )

print( accuracy_score(y_test, predictions))