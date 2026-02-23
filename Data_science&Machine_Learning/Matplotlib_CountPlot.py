import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1. Correctly load the CSV file into a DataFrame
dataset = "iris.csv"
df = pd.read_csv(dataset)  

# 2. Set up the figure size
plt.figure(figsize=(6, 4)) 

# 3. Create the count plot (using 'species' instead of 'Category')
sns.countplot(x='species', data=df)

# 4. Add title and display the plot
plt.title('Count Plot of Iris Species')
plt.show()