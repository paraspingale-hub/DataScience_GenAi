import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn_Selection import train_test_split

from sklearn.tree import DecisionTreeClassifier ,plot_tree

from sklearn.metrics import classification_report , confusion_matrix , accuracy_score , ConfusionMatrixDisplay


border = "-" * 40

###############################################################################################################
#  STEP 1 : load the data set 
###############################################################################################################



print(border)
print("Step 1: Load the dataset")

dataset = iris.csv
df = pd.read_csv(dataset)

print("dataset loaded successfully")

print("initial entries of the dataset : ")
print(df.head())
