from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree

import matplotlib.pyplot as plt

 
def main():
    iris = load_iris()
    x = iris.data
    y = iris.target
    
    x_train , x_test ,y_train , y_test = train_test_split (x , y , test_size=0.2 )
    model = DecisionTreeClassifier()
    model.fit(x_train , y_train)
    
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test , y_pred)
    
    print("Accuracy:" , accuracy)
    
    # Visualize the decision tree
    
    plt.figure(figsize=(12, 8))
    plot_tree(model , filled = True , feature_names = iris.feature_names , class_names = iris.target_names )
    
    
    plt.title("Decision Tree Visualization")
    plt.show()
    
    

if __name__ == "__main__":
    main()