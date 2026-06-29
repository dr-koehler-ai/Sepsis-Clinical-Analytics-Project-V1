# Clinical Sepsis Analytics Dashboard (V1)
# =======================================

import kagglehub
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import os


# =========================
# 1. Load Data
# =========================
def load_data():

    dataset_path = kagglehub.dataset_download(
        "salikhussaini49/prediction-of-sepsis"
    )

    dataset_file = Path(dataset_path) / "Dataset.csv"
    df = pd.read_csv(dataset_file)

    print("\nShape:", df.shape)
    print("Patients:", df["Patient_ID"].nunique())

    return df


# =========================
# 2. Clean Data
# =========================
def clean_data(df):

    missing = df.isnull().mean().sort_values(ascending=False)

    clinical_rel_col = [
        'HR', 'Temp', 'MAP', 'Resp',
        'Creatinine', 'Lactate', 'WBC',
        'Platelets', 'O2Sat'
    ]

    good_cols = missing[missing < 0.9].index
    final_cols = list(set(good_cols) | set(clinical_rel_col))

    df_clean = df[final_cols]

    return df_clean


# =========================
# 3. Aggregate Patients
# =========================
def aggregate_patients(df):

    df_agg = df.groupby("Patient_ID").agg({
        "HR": ["mean", "max"],
        "O2Sat": ["mean", "min"],
        "Temp": ["mean", "min", "max"],
        "MAP": ["mean", "min"],
        "Resp": ["mean", "max"],
        "Lactate": ["mean", "max"],
        "WBC": ["mean", "max"],
        "Creatinine": "max",
        "Age": "first",
        "Gender": "first",
        "SepsisLabel": "max"
    })

    df_agg.columns = [
        f"{col[0]}_{col[1]}" if isinstance(col, tuple) else col
        for col in df_agg.columns
    ]

    df_agg = df_agg.rename(columns={"SepsisLabel_max": "SepsisPatient"})

    print("\nFinal dataset shape:", df_agg.shape)

    return df_agg


# =========================
# 4. Visualization
# =========================
def plot_results(df):

    os.makedirs("figures", exist_ok=True)

    features_to_plot = [
        ("HR_mean", "Heart Rate"),
        ("MAP_mean", "MAP"),
        ("Lactate_max", "Lactate"),
        ("Creatinine_max", "Creatinine")
    ]

    for feature, label in features_to_plot:
        plt.figure()
        sns.boxplot(data=df, x="SepsisPatient", y=feature)
        plt.title(f"{label}: Sepsis vs Non-Sepsis")
        plt.savefig(f"figures/boxplot_{feature}.png", dpi=300)
        plt.show()

    # Heatmap summary
    features = ["HR_mean", "MAP_mean", "Lactate_max", "Creatinine_max"]

    comparison_df = pd.DataFrame({
        "Non_Sepsis": df[df["SepsisPatient"] == 0][features].mean(),
        "Sepsis": df[df["SepsisPatient"] == 1][features].mean()
    })

    plt.figure(figsize=(8, 5))
    sns.heatmap(comparison_df, annot=True, cmap="Reds", fmt=".2f")
    plt.title("Clinical Profile: Sepsis vs Non-Sepsis")
    plt.savefig("figures/heatmap.png", dpi=300)
    plt.show()


# =========================
# 5. Main Pipeline
# =========================
def main():

    df = load_data()
    df_clean = clean_data(df)
    df_agg = aggregate_patients(df_clean)
    plot_results(df_agg)


if __name__ == "__main__":
    main()
