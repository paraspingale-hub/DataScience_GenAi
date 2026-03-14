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
    print(df.shape())
    
    print("\nColoums name : ")
    print(df.columns.tolist())
    
    print("\nMissing value in the dataset")
    print(df.isnull().sum())
    
    
    
    


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