import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score , confusion_matrix , classification_report

#-------------------------------------------------------------------------------------------------
#STEP 1 : Load the data set
#-------------------------------------------------------------------------------------------------

df = pd.read_csv("breast_cancer.csv")
print(df.shape)
print(":: Adaboosting Classification ::")

#-------------------------------------------------------------------------------------------------
#STEP 2 : Split the Data
#-------------------------------------------------------------------------------------------------

X = (df.drop("target" ,axis = 1 ))
Y = (df["target"])

#-------------------------------------------------------------------------------------------------
#STEP 3 : Split for testing an training 
#-------------------------------------------------------------------------------------------------

X_train , X_test , Y_train ,Y_test = train_test_split(X ,Y ,test_size=0.2)

#-------------------------------------------------------------------------------------------------
#STEP 4 : Create Boodting Model // adaboost // serial modeling
#-------------------------------------------------------------------------------------------------

Boost_model = AdaBoostClassifier(random_state=42 , n_estimators=400 , learning_rate=1.0)

#-------------------------------------------------------------------------------------------------
#STEP 5 : Training Dataset
#-------------------------------------------------------------------------------------------------

Boost_model.fit(X_train , Y_train)

#-------------------------------------------------------------------------------------------------
#STEP 6 : Test Dataset
#-------------------------------------------------------------------------------------------------

y_pred = Boost_model.predict(X_test)

#-------------------------------------------------------------------------------------------------
#STEP 7 : Accuracy Calculation 
#-------------------------------------------------------------------------------------------------

print("Boosting Accuracy  : " , accuracy_score(Y_test , y_pred))
print("Confussion matrix : ")
print(confusion_matrix(Y_test , y_pred))
