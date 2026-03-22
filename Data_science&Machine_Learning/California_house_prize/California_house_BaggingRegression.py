import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error , r2_score

#-------------------------------------------------------------------------------------------------
#STEP 1 : Load the data set
#-------------------------------------------------------------------------------------------------

df = pd.read_csv("California_housing.csv")
print(df.shape)
print(":: REgression California ::")

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
#STEP 4 : Create Base Model 
#-------------------------------------------------------------------------------------------------

Base_model = DecisionTreeRegressor(random_state=42)

#-------------------------------------------------------------------------------------------------
#STEP 5 : Creating Bagging Model
#-------------------------------------------------------------------------------------------------

Bagging_model = BaggingRegressor(estimator=Base_model, n_estimators=10 ,random_state=42)

#khutla model ghe -> desigentreeClassifier
# 10 model bantil hite,

#-------------------------------------------------------------------------------------------------
#STEP 6 : Training Dataset
#-------------------------------------------------------------------------------------------------

Bagging_model.fit(X_train , Y_train)

#-------------------------------------------------------------------------------------------------
#STEP 7 : Test Dataset
#-------------------------------------------------------------------------------------------------


y_pred = Bagging_model.predict(X_test)

#-------------------------------------------------------------------------------------------------
#STEP 8 : Accuracy Calculation 
#-------------------------------------------------------------------------------------------------

print("Meaned Sq Error" , mean_squared_error( Y_test , y_pred))
print("Value of rSq : " ,r2_score(Y_test , y_pred))

