# Assignment-7-Matplotlib
# Purpose
The purpose of this project is to create meaningful data visualizations using Matplotlib in order to analyze patterns and trends in real-world datasets. This project uses two datasets: the Iris dataset to compare physical characteristics of flower species, and a loan dataset to explore patterns in customer financial data and loan outcomes.
# Datasets Used
1. Iris Dataset:
- Loaded using sklearn (no external file required)
- Contains measurements of iris flowers

Columns include:
sepal_length, sepal_width, petal_length, petal_width, species

2. Loan Dataset:
- CSV file loaded from local machine
- Contains customer and loan-related information

Relevant columns used:
customer_income, home_ownership, Current_loan_status
# Input file requirements
Loan Dataset CSV must:
- Be properly formatted as a CSV file

Contain the following columns:
- customer_income (numeric or convertible to numeric)
- home_ownership (categorical)
- Current_loan_status (categorical)
- Not contain excessive missing or corrupted values
# Class Design
1. IrisVisualizer Class

Purpose:
Handles all visualizations related to the Iris dataset.

Attributes:

data: stores the dataset as a pandas DataFrame

Methods:

- scatter_plot():

Creates a scatter plot comparing sepal length and sepal width for each species

- petal_plot():

Creates a scatter plot comparing petal length and petal width for each species

- box_plot():

Displays a box plot showing the distribution of sepal length across species

2. LoanVisualizer Class

Purpose:
Handles all visualizations related to the loan dataset.

Attributes:

file_path: stores the location of the dataset

data: stores the dataset as a pandas DataFrame

Methods:

- loan_status_count():

Creates a bar chart showing the frequency of each loan status

- income_distribution():

Creates a histogram showing the distribution of customer income

- loan_by_home():

Creates a grouped bar chart comparing loan status across home ownership categories
# Implementation
- The Iris dataset is loaded using sklearn and converted into a pandas DataFrame
- The loan dataset is loaded using pandas read_csv()
- Customer income values are converted to numeric format
- Invalid or missing income values are removed
- Extremely large income values (outliers) are filtered out to improve visualization clarity
- Matplotlib is used to generate all visualizations
# Limitations
- The program assumes column names match exactly as expected
- Limited error handling for incorrect file paths
- Missing values are only handled for the income column
- Outlier removal is basic and may exclude valid high-income data
- Visualizations are simple and do not include advanced styling or customization
- The analysis is based only on visual trends and does not include statistical testing
