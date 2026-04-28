import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder

# 1. Creating the dataset
x = np.array([['sunny' , 'hot'],
             ['sunny' , 'hot'],
             ['overcast' , 'hot'],
             ['rainy' , 'mild'],
             ['rainy' , 'cool'],
             ['rainy' , 'cool'],
             ['overcast' , 'cool'],
             ['sunny' , 'mild'],
             ['sunny' , 'cool'],
             ['rainy' , 'mild']])

y = np.array(['no','no','yes','yes','yes','no','yes','no','yes','yes'])

# 2. Encoding categorical data into numbers
# Models can't process strings, so we convert "sunny" -> 2, "hot" -> 0, etc.
le = LabelEncoder()
x_encoded = np.zeros(x.shape)

for i in range(x.shape[1]):
    x_encoded[:, i] = le.fit_transform(x[:, i])

y_encoded = le.fit_transform(y)

# 3. Splitting the data
# We use the encoded versions (numbers) instead of the original strings
x_train, x_test, y_train, y_test = train_test_split(x_encoded, y_encoded, test_size=0.2, random_state=42)

# 4. Training the model
model = KNeighborsClassifier(n_neighbors=3) # Set neighbors to 3 for small datasets
model.fit(x_train, y_train)

# 5. Making predictions
# Pass the TEST FEATURES, not the test labels
pred = model.predict(x_test)

# 6. Evaluation
# Compare the predictions against the actual true labels
acc = accuracy_score(y_test, pred)
# For F1, we specify the average type since it's a binary/small set
f1 = f1_score(y_test, pred)

print(f"Accuracy: {acc * 100}%")
print(f"F1 Score: {f1}")