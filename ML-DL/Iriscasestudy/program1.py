import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical

# 1. Load and Preprocess
df = pd.read_csv("iris.csv")
X = df.drop("species", axis=1).values
y = df["species"].values

# Encode labels (Setosa, Versicolor, Virginica -> 0, 1, 2)
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)
y_onehot = to_categorical(y_encoded)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y_onehot, test_size=0.2, random_state=42)

# Feature Scaling - Critical for Deep Learning performance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 2. Build the Deep Learning Model
model = Sequential([
    Dense(16, activation='relu', input_shape=(4,)), # Input Layer + 1st Hidden
    Dropout(0.2),                                   # Regularization to prevent overfitting
    Dense(8, activation='relu'),                    # 2nd Hidden Layer
    Dense(3, activation='softmax')                  # Output Layer (3 classes)
])

model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# 3. Train the Model
print("-" * 40)
print("Training Neural Network...")
history = model.fit(X_train, y_train, epochs=100, batch_size=8, validation_split=0.1, verbose=0)

# 4. Evaluation
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {accuracy*100:.2f}%")

# 5. Visualization of Training History
plt.plot(history.history['accuracy'], label='train_accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.title('Model Accuracy Trend')
plt.legend()
plt.show()

# 6. Industrial Inference Example
sample_data = np.array([[5.1, 3.5, 1.4, 0.2]]) # Example input
scaled_sample = scaler.transform(sample_data)
prediction = model.predict(scaled_sample)
predicted_class = encoder.inverse_transform([np.argmax(prediction)])
print(f"Predicted Species: {predicted_class[0]}")