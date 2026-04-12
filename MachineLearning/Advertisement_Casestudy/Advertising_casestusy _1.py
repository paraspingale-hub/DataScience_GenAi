import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score


def MarvellousAdvertise(DataPath):
    
    border = "-"*40
    #----------------------------STEP 1 : LOAD DATASET---------------------------------------#
    print(border)
    print("Loading the dataset")
    df = pd.read_csv(DataPath)
    print(border)
    
    print("Few records form the dataset : " )
    print(df.head())
    #----------------------------STEP 2 : REMOVE UNWANTED COLUMS------------------------------#
    
    print(border)
    print("rmove the unwanted coloums ")
    print("Shape of data after cleaaning :" , df.shape)
    if 'unnamed: 0' in df.columns:
        df.drop(columns=['uunamed: 0'] , inplace=true)
        
    print("Shape of data after cleaaning :" , df.shape)
    
    print("Clean data set is : " )
    print(df.head)
    
    print(border)
    
    #--------------------------------STEP 3 : CHECK MISSING VALUES-------------------------------#
    
    print(border)
    print("Total missing values : \n")
    print(df.isnull().sum())
    print(border)
    
    

    #--------------------------------STEP 4 : DISPLAY STATISTICAL SUMMATY-------------------------#
    print(border)
    print("Display Statistical summary ")
    print(border)
    print(df.describe())
    
    
    #--------------------------------STEP 5 : DISPLAY COOREALTIONS BETWEEN COLMS -----------------#
    
    print(border)
    print("Display coorealtionsbtween the colms ")
    print(border)
    
    print("coorealtion matrix:")
    print(df.corr())
    
    
    #--------------------------STEP 6 : SPLIT DATASET INTO INDEPENDENT & DEPENDENT-----------------#
    
    print(border)
    print("SPLIT DATASET INTO INDEPENDENT & DEPENDENT")
    print(border)
    
    X = df[['TV' , 'radio' ,'newspaper']]
    Y = df['sales']
    
    print("Shape of independent variables: " ,X.shape)
    
    print("Shape of dependent variables: " ,Y.shape)
    
    #--------------------------------STEP 7 : SPLIT DATASET FOR TRAIN &TESTING-----------------#
    print(border)
    print("SPLIT DATASET FOR TRAINING & TESTING")
    print(border)
    
    X_train , X_test , Y_train , Y_test = train_test_split(X ,Y , test_size=0.2 ,random_state=42)
    
    print("X_train shape : " ,X_train.shape)
    print("X_test shape : " ,X_test.shape)
    print("Y_train shape : " ,Y_train.shape)
    print("Y_test shape : " ,Y_test.shape)
    
    
    #----------------------------------------STEP 8 : MODEL CREATION & TRAINING----------------------------#
    print(border)
    print("MODEL CREATION & TRAINING")
    print(border)
    
    model = LinearRegression()
    model.fit(X_train , Y_train)
    
    #----------------------------------------STEP 9 : MODEL TESTING----------------------------#
    print(border)
    print("MODEL TESTING")
    print(border)
    
    
    print("Model testting is done")
    
    y_pred = model.predict(X_test)
    
    #----------------------------------------STEP 10 : MODEL EVALUATION----------------------------#
    print(border)
    print("MODEL EVALUATION")
    print(border)
    
    #claculations 
    MSE = mean_squared_error(Y_test , y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test , y_pred)
    
    print("Mean Squared error :" ,MSE)
    print("root maean sq error : ",RMSE)
    print("R sr value : ",R2)
    
    
    #----------------------------------------STEP 11 : MODEL COEFFICIENT----------------------------#
    print(border)
    print("MODEL COEFFICIENT")
    print(border)
    for column , value in zip(X.columns , model.coef_):
        print(f"{column} : {value}")
        
    print("Intercept : " , model.intercept_)
    
    #----------------------------------------STEP 12 :COMPARE THE ACTUAL & PRED VALUES----------------------------#
    print(border)
    print("COMPARE THE ACTUAL & PRED VALUES")
    print(border)
    
    
    result = pd.DataFrame({'Actual sale' : Y_test.values ,
                          "Predicted sale" : y_pred})
    
    print(result.head())
    
    
    
    
        
    
    
    
    
    
    
    




def main():
    MarvellousAdvertise("Advertising.csv")
    
if __name__ == "__main__" :
    main()


