"""
PROBLEM STATEMENT:
Write a Python program that classifies a new data point using the K-Nearest Neighbors (KNN) algorithm. 
The algorithm should be implemented manually without using any machine learning library.

THE PROGRAM SHOULD:
1. Calculate Euclidean distance
2. Sort distances
3. Select K nearest neighbors
4. Predict the class based on majority voting

DATASET:
+-------+---+---+-------+
| Point | X | Y | Label |
+-------+---+---+-------+
|   A   | 1 | 2 | Red   |
|   B   | 2 | 3 | Red   |
|   C   | 3 | 1 | Blue  |
|   D   | 6 | 5 | Blue  |
+-------+---+---+-------+

TASKS:
1. Accept X and Y coordinates of a new point from the user.
2. Compute Euclidean distance from all dataset points.
3. Sort the distances.
4. Select K = 3 nearest neighbors.
5. Predict the class label.

INPUT FORMAT:
Enter X coordinate: 2
Enter Y coordinate: 2

EXPECTED OUTPUT:
Nearest Neighbors:
A - Distance: 1.0
B - Distance: 1.0
C - Distance: 1.41

Predicted Class: Red
"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# 1. Dataset
X = np.array([[1, 2], [2, 3], [3, 1], [6, 5]])
y = np.array(['Red', 'Red', 'Blue', 'Blue'])

print(f"{'K Value':<10} | {'Accuracy Score':<15}")
print("-" * 30)

# 2. Loop to find accuracy for each K
# We test the model on the same data it was trained on (Training Accuracy)
for k in range(1, 5):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X, y)
    
    # Generate predictions for the whole dataset
    y_pred = knn.predict(X)
    
    # Calculate accuracy: (Correct Predictions / Total Predictions)
    score = accuracy_score(y, y_pred)
    
    print(f"{k:<10} | {score * 100:>14.1f}%")