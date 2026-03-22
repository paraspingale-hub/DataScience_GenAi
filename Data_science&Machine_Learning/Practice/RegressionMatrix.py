import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


data = fetch_california_housing()

X = data['data']
Y = data['target']

X_train ,Y_train ,X_test,Y_test = train_test_split(X ,Y,test_size=0.2)

reg = LinearRegression()
forest = RandomForestRegressor()

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
reg.fit(X_train , Y_train)
forest.fit(X_train , Y_train)


