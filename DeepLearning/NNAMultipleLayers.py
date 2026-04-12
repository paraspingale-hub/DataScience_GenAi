# -----------------------------------------------
# Program : Neural Network Application with Multiple Layers
# Structure:
#   Input Layer   - 3 inputs
#   Hidden Layer  - 3 neurons with ReLU activation
#   Output Layer  - 1 neuron with Sigmoid activation
# Purpose:
#   To understand how data moves from input layer
#   to hidden layer and finally to output layer
# -----------------------------------------------

import math

# -----------------------------------------------
# Function Name : Marvellous_Relu
# Description   : ReLU Activation Function
# Use           : Commonly used in hidden layers
# -----------------------------------------------
def Marvellous_Relu(value):
    return max(0, value)

# -----------------------------------------------
# Function Name : Marvellous_Sigmoid
# Description   : Applies Sigmoid Activation Function
# Use           : Commonly used in output layer for
#                 binary classification
# -----------------------------------------------
def Marvellous_Sigmoid(value):
    return 1 / (1 + math.exp(-value))


# -----------------------------------------------
# Function Name : Marvellous_Calculate_Weighted_Sum
# Description   : Calculates weighted sum of inputs
# Formula       : z = (x1*w1 + x2*w2 + ... + xn*wn) + b
# Parameters    :
#   inputs  - List of input values
#   weights - List of weights
#   bias    - Bias value
# -----------------------------------------------
def Marvellous_Calculate_Weighted_Sum(inputs, weights, bias):
    z = sum(w * x for w, x in zip(weights, inputs)) + bias
    return z


# -----------------------------------------------
# Function Name : Marvellous_Weights_Initializer
# Description   : Initialize weights for each layer
# Parameters    :
#   weights - List of weights
# -----------------------------------------------
def Marvellous_Weights_Initializer(weights):
    weights = []
    for i in range(len(weights)):
        weights.append([round(random.uniform(-1, 1), 2)
                        for _ in range(inputs_count)])
    return weights


# -----------------------------------------------
# Function Name : Marvellous_Process_Hidden_Layer
# Description   : Processing of neurons of hidden layer
# Parameters    :
#   inputs        - Input values from input layer
#   hidden_weights - Weights for hidden layer neurons
#   hidden_biases  - Bias for hidden neurons
# -----------------------------------------------
def Marvellous_Process_Hidden_Layer(inputs, hidden_weights, hidden_biases):
    print("\n***********************************************")
    print("*  Hidden Layer Processing  *")
    print("***********************************************\n")

    hidden_output = []

    for i in range(len(hidden_weights)):
        print(f"---- Step 1 : Hidden Neuron {i+1} Calculation ----")

        # Calculate weighted sum for this neuron
        current_weights = hidden_weights[i]
        current_bias    = hidden_biases[i]

        z = Marvellous_Calculate_Weighted_Sum(inputs, current_weights, current_bias)

        print(f"  Step 1 : z = Weighted Sum = {z:.4f}")

        # Apply ReLU activation
        activated_output = Marvellous_Relu(z)

        print(f"  Step 2 : ReLU Activation(z) = ReLU({z:.4f}) = {activated_output:.4f}")
        print(f"  Output from Hidden Neuron {i+1} : {activated_output:.4f}\n")

        hidden_output.append(activated_output)

    return hidden_output


# -----------------------------------------------
# Function Name : Marvellous_Process_Output_Layer
# Description   : Processes outputs, output weights, output bias
# Parameters    :
#   hidden_outputs - Multiple knowledge values from last hidden layer
#   output_weights - Connecting weights of output neuron
#   output_bias    - Bias for output neuron
# -----------------------------------------------
def Marvellous_Process_Output_Layer(hidden_outputs, output_weights, output_bias):
    print("\n***********************************************")
    print("*  OUTPUT LAYER  *")
    print("***********************************************\n")

    for i in range(len(hidden_outputs)):
        print(f"  Hidden Output {i+1} : {hidden_outputs[i]:.4f}")

    # Calculate weighted sum for the output layer
    z = Marvellous_Calculate_Weighted_Sum(hidden_outputs, output_weights, output_bias)

    print(f"\n  Step 1 : Weighted Sum z = {z:.4f}")

    # Apply Sigmoid activation for output
    final_output = Marvellous_Sigmoid(z)

    print(f"  Step 2 : Sigmoid({z:.4f}) = {final_output:.4f}")
    print(f"\n  FINAL OUTPUT = {final_output:.4f}")

    return final_output


# -----------------------------------------------
# Function Name : Marvellous_Display_Network_Summary
# Description   : Summarizes final output of network
# -----------------------------------------------
def Marvellous_Display_Network_Summary(inputs, final_output):
    print("\n***********************************************")
    print("*  NETWORK SUMMARY  *")
    print("***********************************************\n")

    if final_output >= 0.5:
        print("  Final Result : Positive Class")
    else:
        print("  Final Result : Negative Class")


# -----------------------------------------------
# Function Name : Marvellous_ANN_Forward_Pass
# Description   : Calculates forward pass of ANN
# -----------------------------------------------
def Marvellous_ANN_Forward_Pass(inputs):
    print("\n========== INPUT LAYER ==========\n")

    # Hidden layer weights and biases
    hidden_weights = [
        [0.2, -0.4, 0.6],   # Neuron 1
        [0.5,  0.3, -0.2],  # Neuron 2
        [-0.1, 0.8, 0.4]    # Neuron 3
    ]

    hidden_biases = [0.1, -0.2, 0.3]

    # Output Layer: weights and bias
    output_weights = [0.7, -0.5, 0.4]
    output_bias    = 0.1

    # Process hidden layer
    hidden_output = Marvellous_Process_Hidden_Layer(inputs, hidden_weights, hidden_biases)

    # Process output layer
    final_output = Marvellous_Process_Output_Layer(hidden_output, output_weights, output_bias)

    # Process output
    output_loss = Marvellous_Display_Network_Summary(inputs, final_output)

    return final_output


# -----------------------------------------------
# Function Name : main
# Description   : Entry point of program
# -----------------------------------------------
def main():
    print("\n========== MARVELLOUS ANN FORWARD PASS ==========\n")

    # For single input values and test different outputs
    inputs = [1.0, 2.0, 3.0]

    # Starter
    Marvellous_ANN_Forward_Pass(inputs)


if __name__ == "__main__":
    main()