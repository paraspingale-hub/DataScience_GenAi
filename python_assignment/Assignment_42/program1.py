#implementing linear regression manually

import numpy as np 

#Loading dataset 
x = [1.0,2.0,3.0,4.0,5.0]
y = [3.0,4.0,2.0,4.0,5.0]

# Calculate means
x_mean = np.mean(x)
y_mean = np.mean(y)

print(f"Mean of x = {x_mean} Meand of y = {y_mean}")

# Calculate slope numerator and denominator
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean)**2)
slope = numerator / denominator

print(f"Slope of the given data = {slope}")

#calculating the intercept 
intercept = y_mean - slope * x_mean
print(intercept)



