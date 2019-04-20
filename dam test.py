# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:01:51 2019

@author: vinay
"""
import random
class ScrappyKNN():
#    def _init_(self):
#        pass
    def fit(self, X_train, Y_train):
        self.X_train = X_train
        self.Y_train = Y_train
        
    def predict(self, x_test):
        predictions=[]
        for row in x_test:
            label = random.choice(self.Y_train)
            predictions.append(label)
            print (label)
        return predictions


damdata = data_set_for_dam

x = damdata.data
y = damdata.target

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.5)
print (x_test)
#from sklearn.neighbors  import KNeighborsClassifier
clf = ScrappyKNN()

clf = ScrappyKNN().fit(x_train, y_train)

predictions = ScrappyKNN().predict(x_test)

print (predictions)
print(y_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))
