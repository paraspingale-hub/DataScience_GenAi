import pandas as pd 
import numpy as np

import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix , accuracy_score



#----------------------------------------------------------------------------------------------------------------
#
#   Funcation name :    Displayinfo
#   DEscription :   Used to display the formated title 
#   Parameter : String(title)
#   Return : None
#   Date : 3 - 14 - 26
#   Author: Paras Rahul Pingale
#
#----------------------------------------------------------------------------------------------------------------
def DisplayInfo(title):
    print("\n")
    print("=" * 80)
    print(title)
    print("=" * 80)
    


#----------------------------------------------------------------------------------------------------------------
#
#   Funcation name :    Showdata
#   DEscription :       It shows the basic information about the dataset
#   Parameter :         df
#                       df -> pandas dataframe object 
#                       message 
#                       message -> Heading text to display 
#   Return :            None
#   Date :              3 - 14 - 26
#   Author:             Paras Rahul Pingale
#
#----------------------------------------------------------------------------------------------------------------

def showdata(df, message):
    DisplayInfo(message)
    print("First 5 rows of data set")
    print(df.head())
    
    print("\nshape of the Dataset ")
    print(df.shape)
    
    print("\nColoums name : ")
    print(df.columns.tolist())
    
    print("\nMissing value in the dataset")
    print(df.isnull().sum())
    
    

#----------------------------------------------------------------------------------------------------------------
#
#   Funcation name :    cleantitanicdata
#   DEscription :       It does preprocessing
#                       It removes uneccessories columns 
#                       It handles missing values 
#                       It conversta text to numetric format
#                       It does encoding to catagorical columns 
#   Return :            df -> pandas dataframe 
#                       df -> Clean pandas dtafram
#   Date :              3 - 14 - 26
#   Author:             Paras Rahul Pingale
#
#----------------------------------------------------------------------------------------------------------------
def CleanTitanicdata(df):
    DisplayInfo(df)
    print(df.head())

    # Remove unnecessary colms 
    
    drop_col = ["Passengerid" , "zero" ,"Name" ,"Cabin"]
    exesisting_col = [col for col in drop_col if col in df.columns]                     #inline usecase 
    print("\n colms to be droped ")
    print(exesisting_col)
    
    #drop the unwanted clms
    
    df =  df.drop(columns = exesisting_col)
    
    DisplayInfo(df)
    print(df.head())
    
    #handle age columns 
    
    if "Age" in df.columns:
        print("Age column before filling missing values ")
        print(df["Age"].head(10))
        df["Age"] = (pd.to_numeric(df["Age"]))
        age_median =df["Age"].median()
        
        #replace missing values
        
        df["Age"] = df["Age"].fillna(age_median)
        
        print("\nage columns after precosessing ")
        print(df["Age"].head(10))
        
        
        #handle fare columns
        
        if "Fare" in df.columns:
            print("Fare columns before precorcessing")
            print(df["Fare"].head(10))
            
            fare_median = df["Fare"].median()
            
            print("\n median of fare column is: " ,fare_median)
            # Replace missing values 
            
            df["Fare"] = df["Fare"].fillna(fare_median)
            
            #Handling Embared columns
            
            if "Embarked" in df.columns:
                print("\n embarked  columns after precosessing ")
                print(df["Embarked"].head(10))
                #covert the data into string format 
                df["Embarked"] = df["Embarked"].astype(str).str.strip()
                
                #Remove the missing values 
                
                df["Embarked"] = df["Embarked"].replace(['nan','none',''],np.nan)
                embarked_mode = df["Embarked"].mode()[0]
                print("Mode of embarked column")
                print(embarked_mode)
                df["Embarked"] = df["Embarked"].fillna(embarked_mode)
                print("Embarked column after preprocessing")
                
            # handle sex column 
            if "Embarked" in df.columns:
                print("\n embarked  columns after precosessing ")
                print(df["Sex"].head(10))
                #covert the data into string format 
                df["Sex"] = df["Sex"].astype(str).str.strip()
                
            
            DisplayInfo("Data after preprocessing")
            print(df.head())
            print("Missing values after prepeocessing")
            
            print(df.isnull().sum())
            
    return df


#----------------------------------------------------------------------------------------------------------------
#
#   Funcation name :    MarvellousTitanicLogistics
#   DEscription :       This is the main pipeline controller 
#                       Tt loads the dataset , shows the rae data ,it preprocess the dataset nd train the model 
#   Parameter :         Datapath of dataset file 
#   Return :            None
#   Date :              3 - 14 - 26
#   Author:             Paras Rahul Pingale
#
#----------------------------------------------------------------------------------------------------------------

def MarvellousTitanicLogistics(datapath):
    DisplayInfo("Loading the data set")
    df = pd.read_csv(datapath)
    showdata(df , "Initial Dataset")
    df = CleanTitanicdata(df)
    
    


#----------------------------------------------------------------------------------------------------------------
#
#   Funcation name : Main
#   DEscription : Staring point of the code
#   Parameter : None
#   Return : None
#   Date : 3 - 14 - 26
#   Author: Paras Rahul Pingale
#
#----------------------------------------------------------------------------------------------------------------

def main ():
    MarvellousTitanicLogistics("MarvellousTitanicDataset.csv")
    




if __name__ == "__main__":
    main()