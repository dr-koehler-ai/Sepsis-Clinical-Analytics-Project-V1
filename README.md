# Sepsis Risk Analysis Dashboard (V1)

A first patient-level exploratory data analysis of ICU time-series data to investigate clinical differences between Sepsis and Non-Sepsis patients.

Built using Python, Pandas, Seaborn, and real-world clinical data.


## Overview

This project analyzes ICU patient data to explore clinical differences between patients who develop sepsis and those who do not.

The goal is to build a **clean, interpretable, patient-level clinical analytics pipeline** using real-world hospital data.

---

## Objectives

- Identify patients with and without sepsis
- Handle missing clinical data
- Aggregate time-series ICU data into patient-level features
- Compare physiological patterns between groups
- Visualize clinically relevant differences

---

## Dataset

The dataset contains ICU time-series measurements from the the PhysioNet/Computing in Cardiology Challenge 2019 including:

- Vital signs (HR, MAP, Resp, O2Sat, Temp)
- Laboratory values (Lactate, WBC, Creatinine)
- Patient denographics (Age, Gender)
- Sepsis label (binary outcome over time)

Each row represents one hour of a patient's ICU stay.

---

## Methodology

### 1. Data Cleaning
- Removal of highly incomplete variables (>90% missing values)
- Retention of clinically relevant variables

### 2. Feature Engineering
- Aggregation of time-series data into patient-level features:
  - Mean values (e.g. HR_mean, MAP_mean)
  - Extreme values (e.g. Lactate_max)

### 3. Outcome Definition
- A patient is defined as **Sepsis-positive** if at least one timestamp shows SepsisLabel = 1.

### 4. Analysis
- Comparison of Sepsis vs Non-Sepsis patients
- Visual aggregation of physiological differences

---

## Key Findings

Sepsis patients show:

- Higher heart rate (HR)
- Lower mean arterial pressure (MAP)
- Elevated lactate levels
- Increased creatinine levels

These findings align with known clinical patterns of septic shock and organ dysfunction.

---

## Discussion

This analysis demonstrates that even simple patient-level aggregation of ICU time-series data can reveal clinically meaningful differences between Sepsis and Non-Sepsis patients.

The observed patterns are consistent with clinical knowledge of sepsis pathophysiology:

- Distributive shock with a systemic shift of fluids to the tissue leads to an increased heart reflecting compensatory cardiovascular stress.
- Reduced mean arterial pressure is consistent with reduced vessel fluids.
- Elevated lactate levels indicate tissue hypoperfusion and anaerobic metabolism.
- Increased creatinine suggests early signs of renal dysfunction in severe cases.

### Limitations

- Temporal dynamics are not modeled (loss of time-series information through aggregation before- and after diagnosing sepsis).
- Aggregated statistics (mean/max/min) may conceal clinically relevant pattern changes before and after sepsis onset.
- No predictive modeling is performed in this V1 version.
- Missing data handling is simplified and may introduce bias.

### Clinical Relevance

Despite its simplicity, this analysis provides a clear and interpretable overview of physiological differences associated with sepsis. It serves as a foundation for more advanced data science, predictive modeling and time-series analysis in future work (V2).

---

## Visualizations

The project includes:

- Boxplots of key clinical variables
- Patient-level summary statistics
- Heatmap comparing group-level means

---

## Interpretation

The analysis demonstrates that even simple aggregation of ICU time-series data can reveal clinically meaningful differences between sepsis and non-sepsis patients.

---

## Tools Used

- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- KaggleHub

---

## Future Work (V2 ideas)

- Time-to-sepsis prediction modeling
- Machine learning classification
- Temporal feature engineering
- Risk scoring system
