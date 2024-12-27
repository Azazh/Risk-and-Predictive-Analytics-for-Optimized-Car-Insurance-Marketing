
# **Exploratory Data Analysis on Insurance Dataset**

## **Table of Contents**
- [Project Overview](#project-overview)  
- [Dataset Description](#dataset-description)  
- [Key Insights](#key-insights)  
- [Features Analyzed](#features-analyzed)  
- [Data Visualizations](#data-visualizations)  
- [Tools and Libraries Used](#tools-and-libraries-used)  
- [Setup and Execution](#setup-and-execution)  
- [Future Improvements](#future-improvements)  
- [Acknowledgments](#acknowledgments)  



## **Project Overview**  
This project involves performing an **Exploratory Data Analysis (EDA)** on an insurance dataset to uncover insights and patterns that help understand key factors influencing insurance charges. The main objective of this analysis is to identify trends, correlations, and other important features that may inform decision-making or predictive modeling.  


## **Dataset Description**  
The dataset provides comprehensive information about insurance policies, transactions, client details, client locations, and vehicles insured. Below are the key features included in the dataset:

### **Policy Details**
- **UnderwrittenCoverID**: Unique identifier for the underwritten cover.  
- **PolicyID**: Unique identifier for the policy.  
- **TransactionDate**: Date of the transaction.  
- **TransactionMonth**: Month of the transaction.  

### **Client Information**
- **IsVATRegistered**: Indicates whether the client is registered for VAT.  
- **Citizenship**: Client's nationality.  
- **LegalType**: Legal entity type of the client (e.g., individual, company).  
- **Title**: Title of the client (e.g., Mr., Mrs., Dr.).  
- **Language**: Preferred language of the client.  
- **Bank**: Bank associated with the client's account.  
- **AccountType**: Type of bank account (e.g., savings, current).  
- **MaritalStatus**: Marital status of the client (e.g., single, married).  
- **Gender**: Gender of the client.  

### **Client Location**
- **Country**: Country of residence.  
- **Province**: Province of residence.  
- **PostalCode**: Client's postal code.  
- **MainCrestaZone**: Primary Cresta zone for insurance purposes.  
- **SubCrestaZone**: Subzone under the main Cresta zone.  

### **Vehicle Details**
- **ItemType**: Type of item insured (e.g., car).  
- **Mmcode**: Manufacturer and model code of the vehicle.  
- **VehicleType**: Type of vehicle (e.g., SUV, sedan).  
- **RegistrationYear**: Year of vehicle registration.  
- **Make**: Manufacturer of the vehicle.  
- **Model**: Specific model of the vehicle.  
- **Cylinders**: Number of engine cylinders.  
- **CubicCapacity**: Engine size in cubic capacity.  
- **Kilowatts**: Vehicle's power in kilowatts.  
- **BodyType**: Type of vehicle body (e.g., hatchback, sedan).  
- **NumberOfDoors**: Number of doors on the vehicle.  
- **VehicleIntroDate**: Date when the vehicle was introduced to the market.  
- **CustomValueEstimate**: Estimated value of vehicle customizations.  
- **AlarmImmobiliser**: Indicates whether the vehicle has an alarm or immobilizer system.  
- **TrackingDevice**: Indicates whether the vehicle is equipped with a tracking device.  
- **CapitalOutstanding**: Outstanding capital amount for the insured vehicle.  
- **NewVehicle**: Whether the vehicle is new or pre-owned.  
- **WrittenOff**: Indicates if the vehicle has been written off.  
- **Rebuilt**: Indicates if the vehicle has been rebuilt.  
- **Converted**: Indicates if the vehicle has been converted (e.g., for different use).  

## **Key Insights**  



## **Features Analyzed**  
- **Univariate Analysis** 
- **Bivariate Analysis** 
- **Multivariate Analysis**


## **Data Visualizations**  
- **Histograms**: Age, BMI, and charges distributions.  
- **Boxplots**: Charges across smoker status and regions.  
- **Scatter Plots**: Correlations between charges and age/BMI.  
- **Heatmap**: Correlation matrix of numerical features.  


## **Tools and Libraries Used**  
- **Python**  
  - `pandas`: For data manipulation and cleaning.  
  - `numpy`: For numerical computations.  
  - `matplotlib` and `seaborn`: For data visualization.  



## **Setup and Execution**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Azazh/Risk-and-Predictive-Analytics-for-Optimized-Car-Insurance-Marketing.git
     

2. Install the required libraries:  
   ```bash
   pip install -r requirements.txt

3. Run the EDA script:  
   ```bash
   python insuranceEda.ipynb
     

4. View the outputs (graphs, tables, and insights) in the console or saved output directory.  



## **Future Improvements**  
- Extend the analysis to include predictive modeling using regression techniques.  
- Investigate feature engineering for improving data insights.  
- Apply clustering to identify groups of individuals with similar insurance costs.  



## **Acknowledgments**  
Special thanks to 10-acadaemy for providing the data and to the open-source Python community for the amazing libraries and tools.  



