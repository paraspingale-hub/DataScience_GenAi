import pandas as pd
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score ,confusion_matrix , classification_report
from sklearn.preprocessing import StandardScaler



def marvellouscasestudy(datapath):
    border = "-" * 40
    
    # STEP 1 : LOAD THE DATASET FORM CSV FILE
    print(border)
    print("STEP 1 : LOAD THE DATASET FORM CSV FILE")
    print(border)
    
    df = pd.read_csv(datapath)
    
    print(border)
    print("Some entried form the dataset")
    print(df.head())
    print(border)
    
    
     # STEP 2 : Clean the dataset 
     
    print(border)
    print("STEP 2 : Clean the dataset ")
    print(border)
    
    df.dropna(inplace= True)
    
    print("totla records. : " ,df.shape[0])         #print no of rows 
    print("Total colomns : " ,df.shape[1])          #print no of col
    
    # STEP 3 : Seprate independent and Dependent variables
     
    print(border)
    print("STEP 3 : Seprate independent and Dependent variables")
    print(border)
    
    
    X = df.drop(columns=['Class'])
    Y = df['Class']
    
    print("Shapeof X : ") 
    print(X.shape)
    
    print("Shapeof Y : ")
    print(Y.shape)
    
    
    # STEP 4 : Split the dataset for training and testing
     
    print(border)
    print("STEP 4 : Split the dataset for training and testing")
    print(border)
    
    X_train ,X_test ,Y_train, Y_test = train_test_split(X ,Y , test_size=0.2 ,random_state=42,stratify=Y)
    
    print(border)
    print("Information of traing ans testing data")
    print("X_train :" ,X_train.shape)
    print("X_test :" ,X_test.shape)
    print("Y_train :" ,Y_train.shape)
    print("Y_test :" ,X_test.shape)
    
    
    
    # STEP 5 : Feature Scaling
     
    print(border)
    print("STEP 5 : Feature Scaling")
    print(border)
    
    scaler = StandardScaler()
    
    #independent variable scalling
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)
    
    print("FEature scalling is done")
    
    # STEP 6 : Explore the multiple values of K in KNN algorithm 
    
    #Hyper parameter tuning(K)
    accuracy_scores = []
    k_values =range(1,21)
    
    for k in k_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled , Y_train)
        y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test , y_pred)
        accuracy_scores.append(accuracy)
        
    print(border)
    print("accuracy report of all k values ")

    for values in accuracy_scores:
        print(values)
    print(border)
        
        
    # STEP 7 : graph plotting 
    
    print(border)
    print("TEP 7 : graph plotting ")    
    print(border)
    
    plt.figure(figsize=(8,5))
    plt.plot(k_values ,accuracy_scores,marker = 'o')
    plt.title("K values vs accuracy")
    plt.grid(True)
    plt.xticks(list(k_values))
    plt.show()
    
    
    # STEP 8 :best value of k 
     
    print(border)
    print("STEP 8 :best value of k ")
    print(border)
    
    best_k = list(k_values)[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of k is:", best_k)
    
    
    # STEP 9 : Built final model using the best value of K
     
    print(border)
    print("STEP 9 : Built final model using the best value of K")
    print(border)
    
    final_model = KNeighborsClassifier(n_neighbors=best_k)
    final_model.fit(X_train_scaled , Y_train)
    y_pred = final_model.predict(X_test_scaled)
    
    
    # STEP 10 :Calculate final Accuracy
     
    print(border)
    print("STEP 10 :Calculate final Accuracy")
    print(border)
    
    Accu_score = accuracy_score(Y_test , y_pred)
    print("Accuracy o fthe  model is : " , Accu_score)
    
    
    # STEP 11 : display confusion matrix 
     
    print(border)
    print("STEP 11 : display confusion matrix ")
    print(border)
    
    cm = confusion_matrix(Y_test , y_pred)
    print(cm)
    
    # STEP 12 : Display classification report 
     
    print(border)
    print("STEP 12 : Display classification report ")
    print(border)
    
    print(classification_report(Y_test , y_pred))
    

        
def main():
    border = "-" * 40
    
    print(border)
    print("Wine Classifire uning KNN")
    print(border)
    
    "WinePredictor.csv"
    marvellouscasestudy("WinePredictor.csv")



if __name__ == "__main__":
    main()