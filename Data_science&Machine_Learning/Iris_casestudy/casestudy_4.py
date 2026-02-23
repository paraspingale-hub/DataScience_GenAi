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
#  STEP : 3 Decide independent and dependent variable
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
plt.legend()
plt.grid(True)
plt.show()

###############################################################################################################
#  STEP : 5 Sliting the data into training and testing set
###############################################################################################################

print(border)
print("STEP : 5 Sliting the data into training and testing set")
print(border)
