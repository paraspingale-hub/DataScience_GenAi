'''
Assignment 2: The Impact of K in KNN
Problem Statement:
The value of K plays an important role in the KNN algorithm. Write a Python program that demonstrates how 
prediction changes when K changes.

Dataset:
Use the same dataset as Assignment 1:

A: (1, 2) → Red

B: (2, 3) → Red

C: (3, 1) → Blue

D: (6, 5) → Blue

Tasks:
Predict the class of the same new point (e.g., X=2, Y=2) using:

K = 1

K = 3

K = 5 (Note: Since the dataset only has 4 points, K=5 would typically include the entire dataset plus a placeholder or error depending on implementation).

Expected Output:

Plaintext
Prediction Results

K = 1 → Red
K = 3 → Red
K = 5 → Blue
Analysis Task:
Explain why the prediction changes when K increases.

'''
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

X = np.array([[1, 2], [2, 3], [3, 1], [6, 5]])
y = np.array(['Red', 'Red', 'Blue', 'Blue'])

x_train , X_test , Y_train , Y_test  = train_test_split(X ,y)
for k in range(0 , 3):
    model = KNeighborsClassifier()
    model.fit(X , y )
    y_pred = model.prkedict(Y_test)
    print(f"Value of K is :{k}Predication of the k model : {y_pred}")
    

