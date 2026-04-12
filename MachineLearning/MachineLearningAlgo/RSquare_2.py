from sklearn.metrics import r2_score
def main ():
    y_actual = [3,4,2,4,5]                              #Y
    y_predicted = [2.8 , 3.2 , 3.6 , 4.0 , 4.4]         #yp
    
    r2 = r2_score(y_actual , y_predicted)
    
    print("Actual values : " ,y_actual)
    print("Predicted values : " ,y_predicted)
    print("R Sqr values : " , r2)
    
    
    



if __name__ == "__main__":
    main()