#   [a,b,c,d]
# x [1,2,3,5]
# y [2,3,1,6]
# r [r,r,b,b] 
# target [x = 3 ,y = 3]

import numpy as np 
import math 


def euclidean_distance(P1,P2):
    ans = math.sqrt((P1['x'] - P2['x'])**2 + (P1['y'] - P2['y'])**2)
    return ans


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
    
    
    print(border)
    new_point = {'x' : 3 , 'y' : 3}

    #Distance calculation
    for d in data :
        d['distance'] = euclidean_distance(d , new_point)
        
        
    print(border)
    print("Calculated distance are after sorting : ")
    print(border)
    Sorted_data = sorted(data , key = lambda item : item['distance'])
    
    for d in Sorted_data :
        print(d)
        
    k = 3 
    
    nearest = Sorted_data[:k]                   # first 3 data points are nearest points
    
    print(border)
    print("Nearest points are : ")
    print(border)
    
    for d in nearest:
        print(d)
        
        
        # majority voting
        
    votes = {}
    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label , 0 ) +1
        
    print(border)
    print("Voting result : " )
    print(border)
    
    
    for d in votes:
        print(f"Name : {d} , Number of votes  : {votes[d]}")
        
    print(border)
    
    
    #calulate the max votes 
    
    maximum = max(votes , key = votes.get)
    print(f"predicted label for new point is : {maximum}")
    
    

        
        
def main():
    MarvellousKNneighbourClassifier()

if __name__ == "__main__":
    main()