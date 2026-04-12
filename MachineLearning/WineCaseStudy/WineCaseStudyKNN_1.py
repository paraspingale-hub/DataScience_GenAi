import pandas as pd
import matplotlib as plt


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score ,confusion_matrix , classification_report


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
    
    
     
    
    



def main():
    border = "-" * 40
    
    print(border)
    print("Wine Classifire uning KNN")
    print(border)
    
    "WinePredictor.csv"
    marvellouscasestudy("WinePredictor.csv")


if __name__ == "__main__":
    main()