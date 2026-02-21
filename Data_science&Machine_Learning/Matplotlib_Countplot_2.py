import matplotlib.pyplot as plt
import seaborn as sns 
def main():
    
    sns.countplot(x = ["C","C","C++","JAVA","Python","JavaScript","Golang","R","PHP","swift"])
     
    plt.show()
if __name__ == "__main__":
    main()