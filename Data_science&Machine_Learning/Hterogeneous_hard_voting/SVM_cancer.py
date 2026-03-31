from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC # support vetor callifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , confusion_matrix
data = load_breast_cancer()
X = data.data
Y = data.target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = SVC(kernel='rbf' , C=1 , gamma='scale')      
#rbf = radial basis function 
y_pred = model.predict(X_test)
acc = accuracy_score(y_pred, Y_test)
print(acc)

