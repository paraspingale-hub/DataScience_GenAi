from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier

# STEP 1: Load data set
data = load_breast_cancer()
X = data.data
Y = data.target

print("Shape of X : ", X.shape)
print("Y Shape   : ", Y.shape)
 
# STEP 2: Split the data set 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# STEP 3: Create and Train Base Models
model_Dt = DecisionTreeClassifier(random_state=42)
model_Lr = LogisticRegression(max_iter=5000) # Increased max_iter for convergence
model_Knn = KNeighborsClassifier(n_neighbors=5)

model_Dt.fit(X_train, Y_train)
model_Lr.fit(X_train, Y_train)
model_Knn.fit(X_train, Y_train)

# STEP 4: Predict using X_test (The Fix)

pred_lr = model_Lr.predict(X_test)
pred_Dt = model_Dt.predict(X_test)
pred_Knn = model_Knn.predict(X_test)

# STEp. 5 : Hard voting classification 

hard_model = VotingClassifier(
    estimators=[
        ('lr',model_Lr),
        ('Dt',model_Dt),
        ('knn',model_Knn)],
    voting='hard'
)

hard_model.fit(X_train , Y_train)
pred_hard = hard_model.predict(X_test)
acc_hard = accuracy_score(pred_hard , Y_test)
print("Accuracy of Hard Voting : " , acc_hard)


