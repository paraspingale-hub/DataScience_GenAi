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
#  STEP 2 : Data analysis and visualization(EDA) 
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