import matplotlib.pyplot as plt
import seaborn as sns 
def main():
    #generally used to detect outliers in the data
    sns.boxplot(x = [10,20,30,110] , color = 'orange')
     
    plt.show()
if __name__ == "__main__":
    main()
    
    
    