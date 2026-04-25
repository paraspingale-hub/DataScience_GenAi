#implementing linear regression manually 

#Loading dataset 
x = [1.0,2.0,3.0,4.0,5.0]
y = [3.0,4.0,2.0,4.0,5.0]

#Calculating mean of 'x' 
MeanX = sum(x) / len(x)
print(MeanX) 

#Calculating mean of 'y'
MeanY = sum(y) / len(y)
print(MeanY)

#Calculating slope
sumX = 0
for i in x : 
    
    xCalculations = i - MeanX
    sumX = sumX + xCalculations
print(sumX)


sumY = 0
for i in y :
    yCalculation = i - MeanY
    sumY = sumY + yCalculation
print(sumY)
    
slope = (sumX * sumY) 
print(slope)
