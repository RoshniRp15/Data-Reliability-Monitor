import pandas as pd

class DataReliabilityMonitor:
    """A simple tool to check data quality issues in a dataset."""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def check_missing_values(self):
        """Return missing values per column."""
        return self.df.isnull().sum()

    def check_duplicate_rows(self):
        """Return number of duplicate rows."""
        return self.df.duplicated().sum()

    def detect_outliers_iqr(self):
        """Detect numeric outliers using the IQR method."""
        outliers = {}
        numeric_cols = self.df.select_dtypes(include=["int", "float"]).columns

        for col in numeric_cols:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            outliers[col] = self.df[(self.df[col] < lower) | (self.df[col] > upper)][col].count()

        return outliers

    def summary_report(self):
        """Generate a dictionary summary of all checks."""
        return {
            "missing_values": self.check_missing_values().to_dict(),
            "duplicate_rows": int(self.check_duplicate_rows()),
            "outliers_iqr": self.detect_outliers_iqr()
        }
