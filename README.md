# 📊 Data Reliability Monitor – Analytics Readiness Framework

A production-style data quality monitoring toolkit designed to identify and surface critical data issues before they impact analytics, reporting, or downstream ML systems.  
This project simulates how modern data teams detect and resolve data quality risks to ensure trust, reliability, and decision readiness.

---

## 🔎 Project Overview

Organizations depend on clean, reliable, and timely data to make decisions.  
Even simple issues like missing values, duplicates, or schema inconsistencies can:

- Break dashboards  
- Distort KPIs  
- Mislead business decisions  
- Cause pipeline failures  

The **Data Reliability Monitor** provides a modular and extensible framework for:

✔ Detecting data anomalies  
✔ Surfacing quality issues early  
✔ Ensuring datasets are analytics-ready  
✔ Supporting BI, reporting, and machine learning workflows  

---

## 🧠 Key Capabilities

### 🔹 1. Missing Value Detection  
Identifies columns with null or incomplete data.

### 🔹 2. Duplicate Record Detection  
Flags repeated entries that can skew aggregates.

### 🔹 3. Outlier Identification (IQR Method)  
Detects numeric anomalies that may represent erroneous data.

### 🔹 4. Summary Quality Report  
Generates a consolidated report for easy validation.

### 🔹 5. Extensible Python Class Design  
Easily extend with new checks like:
- Schema validation  
- Data type checks  
- Business rule validation  

---

## 📁 Project Structure
data-reliability-monitor/
│
├── data/ # Input datasets (raw/processed)
├── src/ # Source code for data quality checks
│ └── data_checks.py
├── notebooks/ # Demo & analysis notebooks
│ └── data_reliability_demo.ipynb
├── reports/ # Auto-generated quality reports
└── README.md # Project documentation


---

## 🚀 Technologies & Tools

- Python  
- Pandas  
- NumPy  
- Jupyter Notebook  
- VS Code  
- (Optional) Power BI / Tableau for insights visualization  

---

## 🧪 How to Use

```python
import pandas as pd
from src.data_checks import DataReliabilityMonitor

df = pd.read_csv("your_dataset.csv")

monitor = DataReliabilityMonitor(df)
report = monitor.summary_report()

print(report)

Produces output like:

{
  "missing_values": {"age": 1, "salary": 0},
  "duplicate_rows": 2,
  "outliers_iqr": {"score": 1}
}

📓 Demo Notebook

A complete interactive demonstration is available in:

notebooks/data_reliability_demo.ipynb


The notebook includes:

Sample dataset

Code execution

Visualization of findings

Explanation of each check

🎯 Why This Project Matters

This project demonstrates real skills required for Data Analyst & BI roles:

✔ Understanding of data quality frameworks
✔ Clean Python coding practices
✔ Ability to build reusable analytics tools
✔ Familiarity with data validation workflows
✔ Awareness of pipeline readiness
✔ Professional documentation & structure

👩‍💻 About Me

I am an aspiring Data Analyst passionate about data quality, analytics engineering, and building reliable data systems.
I enjoy creating practical projects that ensure data accuracy, automation, and business decision readiness.

This project reflects my ability to design production-style tools and apply analytical thinking to real-world data problems.

📬 Contact
Linkdln: www.linkedin.com/in/roshnipremani
Email: Roshnipremani49@gmail.com
