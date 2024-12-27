import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class InsuranceDataAnalysis:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        # Load dataset from the .txt file, assuming `|` as delimiter
        self.data = pd.read_csv(self.file_path, delimiter='|')

    def convert_data_types(self):
        # Convert data types for proper analysis
        self.data['TransactionMonth'] = pd.to_datetime(self.data['TransactionMonth'], errors='coerce')
        num_cols = ['TotalPremium', 'TotalClaims', 'SumInsured', 'CalculatedPremiumPerTerm']
        for col in num_cols:
            self.data[col] = pd.to_numeric(self.data[col], errors='coerce')

    def summarize_data(self):
        # Descriptive statistics for numerical features
        desc_stats = self.data.describe()
        print("Descriptive Statistics:\n", desc_stats)

        # Check for missing values
        missing = self.data.isnull().sum()
        print("\nMissing Values per Column:\n", missing)

    def univariate_analysis(self):
        # Histograms for numerical data
        num_cols = ['TotalPremium', 'TotalClaims', 'SumInsured', 'CalculatedPremiumPerTerm']
        for col in num_cols:
            # Calculate basic statistics
            mean = self.data[col].mean()
            median = self.data[col].median()
            std_dev = self.data[col].std()

            # Display textual insights
            print(f"\nUnivariate Analysis for {col} (Numerical):")
            print(f"Mean: {mean}")
            print(f"Median: {median}")
            print(f"Standard Deviation: {std_dev}")
            print(f"Skewness: {self.data[col].skew()}")
            print(f"Kurtosis: {self.data[col].kurt()}")

            # Histogram plot
            plt.figure(figsize=(8, 4))
            sns.histplot(self.data[col], kde=True, bins=30)
            plt.title(f'Distribution of {col}')
            plt.show()

        # Bar chart for categorical columns
        cat_cols = ['CoverCategory', 'CoverType', 'Country', 'Province']
        for col in cat_cols:
            # Calculate frequency of categories
            value_counts = self.data[col].value_counts()

            # Display textual insights
            print(f"\nUnivariate Analysis for {col} (Categorical):")
            print(f"Number of unique categories: {self.data[col].nunique()}")
            print("Top categories with counts:")
            print(value_counts.head(5))

            # Bar chart plot
            plt.figure(figsize=(8, 4))
            value_counts.plot(kind='bar', color='skyblue')
            plt.title(f'Frequency of {col}')
            plt.show()


    def bivariate_analysis(self): 
        # Correlation matrix for numerical columns
        num_cols = ['TotalPremium', 'TotalClaims', 'SumInsured', 'CalculatedPremiumPerTerm']
        correlation_matrix = self.data[num_cols].corr()
        
        # Print the correlation matrix
        print("Correlation Matrix:")
        print(correlation_matrix)
        
        # Plot the correlation matrix heatmap
        plt.figure(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.show()
        
        # Scatter plot for TotalPremium vs TotalClaims
        plt.figure(figsize=(8, 6))
        scatter_plot = sns.scatterplot(data=self.data, x='TotalPremium', y='TotalClaims', hue='Province')
        plt.title('TotalPremium vs TotalClaims by Province')
        plt.show()
        
        # Print a summary of insights from the scatter plot
        print("\nScatter Plot Insights:")
        print(f"Scatter plot displays the relationship between 'TotalPremium' and 'TotalClaims', categorized by 'Province'.")
        print(f"Number of provinces visualized: {self.data['Province'].nunique()}")
        print(f"Data points visualized: {len(self.data)}")

    def outlier_detection(self):
        # Box plots for numerical columns
        num_cols = ['TotalPremium', 'TotalClaims', 'SumInsured', 'CalculatedPremiumPerTerm']
        for col in num_cols:
            # Calculate basic statistics
            q1 = self.data[col].quantile(0.25)  # First quartile
            q3 = self.data[col].quantile(0.75)  # Third quartile
            iqr = q3 - q1                        # Interquartile range
            lower_bound = q1 - 1.5 * iqr         # Lower bound for outliers
            upper_bound = q3 + 1.5 * iqr         # Upper bound for outliers

            # Identify potential outliers
            outliers = self.data[(self.data[col] < lower_bound) | (self.data[col] > upper_bound)][col]

            # Display textual insights
            print(f"\nOutlier Detection for {col}:")
            print(f"Q1 (25th percentile): {q1}")
            print(f"Q3 (75th percentile): {q3}")
            print(f"IQR (Interquartile Range): {iqr}")
            print(f"Lower Bound for Outliers: {lower_bound}")
            print(f"Upper Bound for Outliers: {upper_bound}")
            print(f"Number of potential outliers: {len(outliers)}")
            if not outliers.empty:
                print(f"Sample outliers:\n{outliers.head()}")
            # Box plot visualization
            plt.figure(figsize=(8, 4))
            sns.boxplot(x=self.data[col])
            plt.title(f'Outlier Detection for {col}')
            plt.show()

    def summarize_geography_trends(self):
        # Grouping data by Province and analyzing trends
        province_summary = self.data.groupby('Province')[['TotalPremium', 'TotalClaims']].mean().sort_values(by='TotalPremium', ascending=False)
        print("\nProvince Trends (Mean TotalPremium and TotalClaims):\n", province_summary)

        # Plotting province trends
        province_summary.plot(kind='bar', figsize=(12, 6), color=['#1f77b4', '#ff7f0e'])
        plt.title('Average TotalPremium and TotalClaims by Province')
        plt.ylabel('Mean Values')
        plt.show()
