import matplotlib.pyplot as plt
import seaborn as sns 
def main():
    
    #linear relationship between two variables(Features)
    sns.scatterplot(x = [1,2,3], y = [3,1,4], color = 'orange')
     
    plt.show()
if __name__ == "__main__":
    main()