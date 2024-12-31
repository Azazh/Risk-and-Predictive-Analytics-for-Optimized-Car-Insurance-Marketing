# **Risk and Predictive Analytics for Car Insurance**

## **Table of Contents**
- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
- [Key Tasks](#key-tasks)
  - [Exploratory Data Analysis](#exploratory-data-analysis)
  - [Model Development](#model-development)
  - [A/B Hypothesis Testing](#a-b-hypothesis-testing)
- [Key Insights](#key-insights)
- [Tools and Libraries](#tools-and-libraries)
- [Setup and Execution](#setup-and-execution)
- [Future Enhancements](#future-enhancements)



## **Project Overview**
This project leverages an insurance dataset to analyze and model key factors influencing car insurance risk, profitability, and customer segmentation. The tasks include exploratory data analysis (EDA), predictive modeling, and hypothesis testing to inform business decisions and optimize marketing strategies.



## **Dataset Description**
The dataset includes policy details, client demographics, geographical data, and vehicle attributes. Notable features:
- **Policy Details**: PolicyID, TransactionDate, TransactionMonth.
- **Client Information**: Gender, MaritalStatus, Citizenship, Province.
- **Vehicle Details**: Make, Model, VehicleAge, CubicCapacity, Kilowatts.



## **Key Tasks**

### **Exploratory Data Analysis**
- **Objective**: Identify patterns, correlations, and key drivers influencing insurance costs.
- **Insights**: Histograms, scatter plots, and heatmaps highlighted significant relationships between features like vehicle age and premium costs.

### **Model Development**
#### **Data Preparation**
- **Data Cleaning**: Handled missing values and outliers.
- **Feature Engineering**: Created derived features such as `CalculatedPremiumPerTerm`.
- **Data Splitting**: Train-test split (80-20).

#### **Model Building**
Developed and compared the following models:
- **Linear Regression**
- **Random Forest**
- **XGBoost**

#### **Model Evaluation**
Metrics used:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R-squared (R²)

**Performance Summary**:
- **Random Forest**: Best performance with an R² of 0.305.
- **XGBoost**: Comparable with an R² of 0.317.
- **Linear Regression**: Baseline with lower performance.

#### **Model Interpretability**
Feature importance was visualized for Random Forest and XGBoost, revealing key drivers such as `CalculatedPremiumPerTerm` and `PolicyID`.

### **A/B Hypothesis Testing**
#### **Objective**
Test differences in risk and profitability across categories such as provinces, zip codes, and gender.

#### **Methodology**
- Selected KPI: **TotalClaims**.
- Groups:
  - Province (e.g., Gauteng vs. Western Cape).
  - Gender (e.g., Women vs. Men).
- Statistical Tests: T-tests and Chi-squared tests.
- **Result**: Null hypotheses were largely not rejected, indicating no significant differences in tested metrics.



## **Key Insights**
- **Premium Drivers**: `CalculatedPremiumPerTerm` and `PolicyID` consistently ranked as top predictive features.
- **Risk Patterns**: Statistical tests suggest limited variability in risk across certain demographics.
- **Model Efficacy**: Ensemble methods (Random Forest and XGBoost) significantly outperformed linear models in predicting insurance metrics.



## **Tools and Libraries**
- **Python Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `xgboost`.
- **Statistical Testing**: T-tests, Chi-squared tests via `scipy`.



## **Setup and Execution**
1. Clone the repository:
   ```bash
   git clone https://github.com/YourRepo/RiskAnalytics.git
   ```
2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the analysis:
   ```bash
   python analysis_script.py
   ```



## **Future Enhancements**
- Incorporate advanced feature selection techniques.
- Implement clustering to identify high-risk customer segments.
- Extend hypothesis testing to additional variables for deeper insights.



