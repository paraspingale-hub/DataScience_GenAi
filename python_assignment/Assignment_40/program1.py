import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# 1. Load the dataset
df = pd.read_csv('student_performance_ml.csv')

# --- TASK 9: Feature Engineering ---
# Create a new column 'PerformanceIndex'
df['PerformanceIndex'] = (df['StudyHours'] * 2) + df['Attendance']

# Define features (including the new column) and target
X = df[['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours', 'PerformanceIndex']]
y = df['FinalResult']

# --- TASK 7: Comparing Random States ---
states = [0, 10, 42]
print("--- Task 7: Random State Comparison ---")
for s in states:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=s)
    temp_model = DecisionTreeClassifier()
    temp_model.fit(X_train, y_train)
    acc = accuracy_score(y_test, temp_model.predict(X_test))
    print(f"Testing Accuracy with random_state={s}: {acc * 100:.2f}%")

# --- TASK 10: Training with max_depth=None (Check for Overfitting) ---
# Using random_state=42 for consistency
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
dt_model = DecisionTreeClassifier(max_depth=None, random_state=42)
dt_model.fit(X_train, y_train)

train_acc = accuracy_score(y_train, dt_model.predict(X_train))
test_acc = accuracy_score(y_test, dt_model.predict(X_test))

print("\n--- Task 10: Accuracy Results ---")
print(f"Training Accuracy: {train_acc * 100:.2f}%")
print(f"Testing Accuracy: {test_acc * 100:.2f}%")

# --- TASK 8: Decision Tree Visualization ---
plt.figure(figsize=(20,10))
plot_tree(dt_model, feature_names=X.columns, class_names=['Fail', 'Pass'], filled=True, rounded=True)
plt.title("Decision Tree Visualization")
plt.show()