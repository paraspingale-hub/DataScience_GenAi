import numpy as np
#------------------------------------------------------------------------------------------------------
#                   STEP 1 : Define input feature 
#these are the input coming to the neuron(x1 x2 x3)
#Example : could be marks pixel valuse or any other feature
#------------------------------------------------------------------------------------------------------

inputs = np.array([2.0 , 3.0 , 4.0])


#------------------------------------------------------------------------------------------------------
#                   STEP 2 : Define weights
#Each input has coorusponding weights(w1 w2 w3)
#------------------------------------------------------------------------------------------------------

weights = np.array([0.5 , 0.3 , 0.2])



#------------------------------------------------------------------------------------------------------
#                   STEP 3 : Define Bais
#bais is an additional parameter that helps shift the output
#it allows the model to fit data better
#------------------------------------------------------------------------------------------------------

bais = 1.0

#--------------------------------------------------
#STEP 4 : Calculate Weighted Sum (Z)
#--------------------------------------------------
#Formula:
#Z = (x1w1 + x2w2 + x3*w3) + bias
#Using numpy dot product for efficient calculation


weighted_sum = np.dot(inputs, weights) + bais


#Manual calculation:
#(2.0 * 0.5) + (3.0 * 0.3) + (4.0 * 0.2) + 1.0
#= 1.0 + 0.9 + 0.8 + 1.0 = 3.7

# STEP 5: Activation Function (ReLU)
#
# ReLU (Rectified Linear Unit):
# If value > 0 -> return value
# If value <= 0 -> return 0
def relu(x):
  return max(0, x)
#
# STEP 6: Final Output
#
# Pass the weighted sum through activation function
output = relu(weighted_sum)
#
# STEP 7: Display Results
#
print("Inputs :", inputs)
print("Weights :", weights)
print("Bias :", bais)
print("Weighted Sum (Z):", weighted_sum)
print("Final Output :", output)
