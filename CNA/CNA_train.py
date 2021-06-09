# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 20:27:48 2021

@author: Asus
"""
import pandas as pd

adr = r"C:\Users\Asus\Desktop\genxmutasyonxhastalık analizi\CNA\cna.csv"
data = pd.DataFrame(pd.read_csv(adr))

#%% convert dtpye for labeling

data = data.astype("string")

#%% merge the data x and y

x_cols = data.drop(columns = ["Primary histology"])
# x_cols = data.iloc[:,:5]
# y_cols = data.iloc[:,5:] # kromozom için eğitmek istersek
y_cols = pd.DataFrame(data["Primary histology"])

#%% auto label encoding 


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

x_cols = x_cols.apply(le.fit_transform)
y_cols = y_cols.apply(le.fit_transform)

# lab = y_label.head(100)
# a = le.inverse_transform([4])
# a[0]

#%% concat encoded columns for training

final_df = pd.concat([x_cols, y_cols], axis = 1)

#%%  *** your ml code here ***
#%% KNN algorithm

from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn import metrics

X_train, X_test, y_train, y_test =train_test_split(x_cols, y_cols, test_size=.25, random_state=17)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
print(clf)

# knn evaluate
y_pred= clf.predict(X_test)
y_expect = y_test

print(metrics.classification_report(y_expect, y_pred))

# knn save model

import joblib
  
# Save the model as a pickle in a file
joblib.dump(clf, 'CNA-knn-primHist.pkl')

#%% #%% random forest algorithm

from sklearn.model_selection import train_test_split 
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, y_train, y_test =train_test_split(x_cols, y_cols, test_size=.25, random_state=17)

classifier = RandomForestClassifier(n_estimators=200, random_state=0)



classifier.fit(X_train, y_train)

# random forest evaluate
yy_pred = classifier.predict(X_test)
print(metrics.classification_report(y_test, yy_pred))

#  random forest save model
import joblib
  
# Save the model as a pickle in a file
joblib.dump(classifier, 'CNA-rforest-primHist.pkl')

#%% naive bayes algorithm

from sklearn.naive_bayes import CategoricalNB

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(x_cols, y_cols, test_size=.25, random_state=17)

CatNB = CategoricalNB()
CatNB.fit(X_train, y_train)

y_expect = y_test
y_pred = CatNB.predict(X_test)

print(accuracy_score(y_expect, y_pred))

print(metrics.classification_report(y_expect, y_pred))


# naive bayes save model

import joblib
  
# Save the model as a pickle in a file
joblib.dump(CatNB, 'CNA-naiveBayes-primHist.pkl')


#%% logistic regression algorithm

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(x_cols, y_cols, test_size=.25, random_state=17)

LogReg = LogisticRegression(solver='liblinear',multi_class='ovr', random_state=200)
LogReg.fit(X_train, y_train)

# Log Reg evaluate 
from sklearn.metrics import classification_report

y_pred = LogReg.predict(X_test)
print(classification_report(y_test, y_pred))

print('Training accuracy:', LogReg.score(X_train, y_train))
print('Test accuracy:', LogReg.score(X_test, y_test))

# Log reg save model
import joblib
  
# Save the model as a pickle in a file
joblib.dump(LogReg, 'CNA-LogReg-primHist.pkl')

#%% primary histology tahmininde accuracy'ler; 

# KNN = %
# Random forest = %
# naive bayes = %
# logistic reg = %

#%% cheomosome için ??

