#   [a,b,c,d]
# x [1,2,3,5]
# y [2,3,1,6]
# r [r,r,b,b] 
# target [x = 3 ,y = 3]


def MarvellousKNneighbourClassifier():
    
    border = '-' * 40
    data = [{'point': 'a' , 'x' : 1 , 'y' : 2 , 'label': 'Red'} ,
            {'point': 'b' , 'x' : 2 , 'y' : 3 , 'label': 'Red'} ,
            {'point': 'c' , 'x' : 3 , 'y' : 1 , 'label': 'Blue'} ,
            {'point': 'd' , 'x' : 5 , 'y' : 6 , 'label': 'Blue'} 
            ]
    print(border)
    print("Marvellous User Defined KNN Classifier")
    print(border)
    
    print(border)
    print("::Training data set::")
    print(border)
    
    for i in data:
        print(i)
    print(border)
    
    
    
def main():
    MarvellousKNneighbourClassifier()


    
if __name__ == "__main__":
    main()