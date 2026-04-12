import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score,confusion_matrix 

df = pd.read_csv("student_performance_ml.csv")

print(df.head())
print("Shape fo the data set",df.shape)


X = (df.drop("FinalResult" ,axis = 1 ))
Y = (df["FinalResult"])

print("Feature shape :",X.shape)
print("Lable shape : ",Y.shape)

Studyhr = df["StudyHours"]
addentance = df["Attendance"]

print("Avg of StudyHours is :  " , Studyhr.mean())
print("Avg of Attendance is :  " , addentance.mean())

prev =df["PreviousScore"]

print("Max value in PreviousScore : " , prev.max())

print("-" * 40)

print("Dataset analysis")
print(df.isnull().sum())

print("*" * 40)
X_train , X_test , Y_train ,Y_test = train_test_split(X ,Y ,test_size=0.2)
model = KNeighborsClassifier()
mdoel2 = DecisionTreeClassifier()


model.fit(X_train , Y_train)
y_pred = model.predict(X_test)

print("-" * 40)
print("Accuracy  : " , accuracy_score(Y_test , y_pred))
print("Confussion matrix : ")
print(confusion_matrix(Y_test , y_pred))


mdoel2.fit(X_train , Y_train)
y_pred = mdoel2.predict(X_test)
print("Accuracy  : " , accuracy_score(Y_test , y_pred))
print("Confussion matrix : ")
print(confusion_matrix(Y_test , y_pred))





