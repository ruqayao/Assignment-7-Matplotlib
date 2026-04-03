#Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

#Class for Iris Dataset Visualization
class IrisVisualizer:

    def __init__(self):
        #Load iris dataset from sklearn
        iris = load_iris()

        #Convert to pandas DataFrame
        self.data = pd.DataFrame(iris.data, columns=iris.feature_names)

        #Rename columns to match code
        self.data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

        #Add species column
        self.data['species'] = iris.target
        self.data['species'] = self.data['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    def scatter_plot(self):
        #Scatter plot: Sepal Length vs Sepal Width
        species = self.data['species'].unique()

        for sp in species:
            subset = self.data[self.data['species'] == sp]
            plt.scatter(subset['sepal_length'], subset['sepal_width'], label=sp)

        plt.title("Sepal Length vs Width (Iris)")
        plt.xlabel("Sepal Length")
        plt.ylabel("Sepal Width")
        plt.legend()
        plt.show()

    def petal_plot(self):
        #Scatter plot: Petal Length vs Petal Width
        species = self.data['species'].unique()

        for sp in species:
            subset = self.data[self.data['species'] == sp]
            plt.scatter(subset['petal_length'], subset['petal_width'], label=sp)

        plt.title("Petal Length vs Width (Iris)")
        plt.xlabel("Petal Length")
        plt.ylabel("Petal Width")
        plt.legend()
        plt.show()

    def box_plot(self):
        #Box plot for sepal length by species
        self.data.boxplot(column='sepal_length', by='species')
        plt.title("Sepal Length Distribution by Species")
        plt.suptitle("")  #Remove default title
        plt.xlabel("Species")
        plt.ylabel("Sepal Length")
        plt.show()


#Class for Loan Dataset Visualization
class LoanVisualizer:

    def __init__(self, file_path):
        #Store dataset path
        self.file_path = file_path
        #Load dataset
        self.data = pd.read_csv(file_path)
        #Convert income to numeric
        self.data['customer_income'] = pd.to_numeric(self.data['customer_income'], errors='coerce')
        #Remove invalid values
        self.data = self.data.dropna(subset=['customer_income'])
        #Remove extreme outliers
        self.data = self.data[self.data['customer_income'] < 200000]
        
    def loan_status_count(self):
        #Bar plot of loan status
        counts = self.data['Current_loan_status'].value_counts()

        counts.plot(kind='bar')
        plt.title("Loan Status Counts")
        plt.xlabel("Loan Status")
        plt.ylabel("Count")
        plt.show()


    def income_distribution(self):
        #Histogram of customer income
        self.data['customer_income'].plot(kind='hist', bins=20)

        plt.title("Customer Income Distribution")
        plt.xlabel("Income")
        plt.ylabel("Frequency")
        plt.show()


    def loan_by_home(self):
        #Loan status grouped by home ownership
        grouped = pd.crosstab(self.data['home_ownership'], self.data['Current_loan_status'])
        grouped.plot(kind='bar')

        plt.title("Loan Status by Home Ownership")
        plt.xlabel("Home Ownership")
        plt.ylabel("Count")
        plt.show()

#Main Execution
def main():
    #Iris dataset
    iris = IrisVisualizer()

    iris.scatter_plot()
    iris.petal_plot()
    iris.box_plot()

    #Loan dataset
    loan = LoanVisualizer("LoanDataset - LoansDatasest.csv")

    loan.loan_status_count()
    loan.income_distribution()
    loan.loan_by_home()


#Run program
if __name__ == "__main__":
    main()

#Loan Data Analysis:

#The loan status bar chart shows the distribution of different loan outcomes, allowing us to see which statuses occur most frequently. 
#This helps identify whether loans are more commonly approved, rejected, or fall into another category. 
#The income distribution histogram reveals that most customers fall within a lower to middle income range, with fewer individuals earning very high incomes. 
#This creates a right-skewed distribution, indicating that high-income customers are less common. 
#Additionally, the grouped bar chart comparing home ownership and loan status suggests that individuals with certain types of home ownership (such as owning or renting) may experience different loan outcomes. 
#This implies that home ownership could be a factor influencing loan decisions, possibly due to its connection to financial stability. 
#Overall, these visualizations highlight trends in customer income and suggest that both income level and home ownership may play a role in loan status outcomes.