import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier ,plot_tree

from sklearn.metrics import classification_report , confusion_matrix , accuracy_score , ConfusionMatrixDisplay


border = "-" * 40

###############################################################################################################
#  STEP 1 : load the data set 
###############################################################################################################

print(border)
print("Step 1: Load the dataset")
print(border)

dataset = "iris.csv"
df = pd.read_csv(dataset)

print("dataset loaded successfully")

print("initial entries of the dataset : ")
print(df.head())


###############################################################################################################
#  STEP 2 : Data analysis 
###############################################################################################################

print(border)
print("Step 2: Data analysis and visualization(EDA)")
print(border)


print("Shape of the dataset : ", df.shape)
print("columns in the dataset : ", df.columns)

print("Missing valuse per colomn : ")
print(df.isnull().sum())

print("species distribution : ")
print(df['species'].value_counts())

print("statistical summary of the dataset : ")
print(df.describe())

###############################################################################################################
#  STEP : 3 Decide independent & dependent variable
###############################################################################################################

print(border)
print("STEP : 3 Decide independent and dependent variable")
print(border)

#X : independent variable (features)
#y : dependent variable (labels)

Feature_calls = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
X = df[Feature_calls] # Independent variables (features)
y = df["species"]

print("X(independent variable) shape : ", X.shape)
print("y(dependent variable) shape : ", y.shape)


###############################################################################################################
#  STEP : 4 Visualization of the data
###############################################################################################################

print(border)
print("STEP : 4 Visualization of the data")
print(border)

#scatterplot visualization of the data
plt.figure(figsize = (7,5))
for sp in df["species"].unique():
    temp = df[df["species"]== sp] #hite 3 verity peki ek verity yeti
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label = sp)
    plt.title("scatter plot of petal length vs petal width")
    plt.xlabel("petal length (cm)")
    plt.ylabel("petal width (cm)")
plt.legend()  # disply ki kaunse color kis species ko represent kar raha hai
plt.grid(True)
plt.show()

###############################################################################################################
#  STEP : 5 Sliting the data into training and testing set
###############################################################################################################

print(border)
print("STEP : 5 Sliting the data into training and testing set")
print(border)

# test size = 20% of the data
# train size = 80% of the data
#                                                      Features , lables , test size     , train size.   , shuffle the data 
X_train , X_test , y_train , y_test = train_test_split(X        , y      , test_size=0.2 ,train_size=0.8 , random_state=42)

print("data spliting activity done successfully")

print("shape of X : ", X.shape)                     #(150,4)
print("shape of X_train : ", X_train.shape)         #(120,4)   150 cha 80%.
print("shape of y_train : ", y_train.shape)         #(120,)    150 cha 80%
print("shape of X_test : ", X_test.shape)           #(30,4)    150 cha 20%
print("shape of y_test : ", y_test.shape)           #(30,)     150 cha 20%


##############################################################################################################
#  STEP : 6 Build the model
###############################################################################################################

print(border)
print("STEP : 6 Build the model")
print(border)

print("We are going to usee decision tree classifier ")

model = DecisionTreeClassifier(
    criterion= "gini", # or "entropy"
    max_depth= 3,      # maximum depth of the tree
    random_state= 42   # for reproducibility
)
print("model building activity done successfully" , model)

##############################################################################################################
#  STEP : 7 Train the model
###############################################################################################################

print(border)
print("STEP : 6 Train the model")
print(border)

model.fit(X_train , y_train) 
print("model training activity done successfully")

##############################################################################################################
#  STEP : 8 Test / Evaluate the model
###############################################################################################################

print(border)
print("STEP : 8 Test / Evaluate the model")
print(border)

y_pred = model.predict(X_test)
print("Predictions on test set: ", y_pred , "\n shape of y_pred : ", y_pred.shape)

print("Expected answer :",y_test)
print("Predicted output : ", y_pred)


