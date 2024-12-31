import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency

class ABHypothesisTester:
    def __init__(self, data_path):
        """
        Initialize the tester with the dataset path.
        """
        try:
            self.data = pd.read_csv(
                data_path, 
                sep='|',  # Pipe-separated file
                low_memory=False  # Avoid mixed-type warnings
            )
        except Exception as e:
            print(f"Error loading dataset: {e}")
            raise
    
    def select_kpi(self, kpi):
        """
        Select the Key Performance Indicator (KPI).
        """
        if kpi not in self.data.columns:
            raise ValueError(f"KPI '{kpi}' not found in dataset.")
        self.kpi = kpi
        print(f"KPI selected: {self.kpi}")

    def segment_data(self, feature, group_a, group_b):
        """
        Segment the data into two groups based on the feature.
        """
        if feature not in self.data.columns:
            raise ValueError(f"Feature '{feature}' not found in dataset.")
        
        self.group_a = self.data[self.data[feature] == group_a]
        self.group_b = self.data[self.data[feature] == group_b]
        
        if len(self.group_a) == 0 or len(self.group_b) == 0:
            raise ValueError(f"One of the groups (A or B) is empty. Check your feature values.")
        
        print(f"Data segmented on '{feature}': Group A = {group_a}, Group B = {group_b}")

    def test_hypothesis(self):
        """
        Conduct statistical testing on the KPI for the two groups.
        """
        if not hasattr(self, 'kpi') or not hasattr(self, 'group_a') or not hasattr(self, 'group_b'):
            raise AttributeError("Ensure KPI is selected and data is segmented before testing.")
        
        # Determine if the KPI is numerical or categorical
        if pd.api.types.is_numeric_dtype(self.data[self.kpi]):
            # Conduct t-test for numerical KPI
            stat, p_value = ttest_ind(self.group_a[self.kpi], self.group_b[self.kpi], equal_var=False)
        else:
            # Conduct chi-squared test for categorical KPI
            contingency_table = pd.crosstab(self.group_a[self.kpi], self.group_b[self.kpi])
            stat, p_value, _, _ = chi2_contingency(contingency_table)
        
        self.p_value = p_value
        self.stat = stat

    def analyze_results(self):
        """
        Analyze the results of the hypothesis test.
        """
        if not hasattr(self, 'p_value') or not hasattr(self, 'stat'):
            raise AttributeError("Hypothesis test not conducted.")
        
        result = (
            f"Fail to reject the null hypothesis. p-value: {self.p_value:.5f}, stat: {self.stat:.5f}"
            if self.p_value >= 0.05 else
            f"Reject the null hypothesis. p-value: {self.p_value:.5f}, stat: {self.stat:.5f}"
        )
        return result
