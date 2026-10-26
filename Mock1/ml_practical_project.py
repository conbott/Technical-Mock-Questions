"""
Technical Round 1 - Part 3: Complete Machine Learning Project
Dataset: Scikit-Learn Breast Cancer Wisconsin Diagnostic Dataset (Real Clinical Data)
Task: Binary Classification of Malignant vs Benign Tumors
Models: Logistic Regression, Support Vector Classifier (SVC RBF), K-Nearest Neighbors (KNN)
Follows all 7 required stages in exact chronological order.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, classification_report, roc_curve, confusion_matrix
)

def run_ml_pipeline():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    vis_dir = os.path.join(base_dir, "visualizations")
    os.makedirs(vis_dir, exist_ok=True)

    print("=" * 70)
    print("STAGE 1: DATASET SELECTION AND LOADING (FROM SKLEARN.DATASETS)")
    print("=" * 70)
    
    # Load real benchmark diagnostic oncology dataset directly from sklearn
    cancer = load_breast_cancer(as_frame=True)
    df = cancer.frame.copy()
    
    # Save a local CSV copy for complete project provenance
    dataset_path = os.path.join(base_dir, "dataset.csv")
    df.to_csv(dataset_path, index=False)
    
    print(f"Dataset successfully loaded from sklearn.datasets.load_breast_cancer()")
    print(f"Local copy persisted to: {dataset_path}")
    print(f"Dataset Dimensions: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Target Classes: {cancer.target_names} (0: Malignant, 1: Benign)")
    print("\nFirst 5 Observations:")
    print(df.iloc[:5, :5])
    print("\nDataset Info Summary:")
    print(df.info())

    print("\n" + "=" * 70)
    print("STAGE 2: DATA PREPROCESSING")
    print("=" * 70)
    
    # Check for missing values
    missing_count = df.isnull().sum().sum()
    print(f"Total Missing Values in Scikit-Learn Breast Cancer Dataset: {missing_count}")
    
    # Separate features and target
    X = df.drop(columns=["target"])
    y = df["target"]
    feature_names = list(X.columns)
    
    print(f"Total Diagnostic Features: {len(feature_names)}")
    print("Preprocessing Strategy: Standard scaling (Z-score normalization) encapsulated in Pipeline to prevent data leakage.")

    print("\n" + "=" * 70)
    print("STAGE 3: EXPLORATORY DATA ANALYSIS (EDA) AND VISUALISATION")
    print("=" * 70)
    
    # 1. Target Class Distribution
    plt.figure(figsize=(6, 4))
    target_counts = y.value_counts()
    sns.barplot(x=["Malignant (0)", "Benign (1)"], y=target_counts.values, palette=["#d95f02", "#1b9e77"], hue=["Malignant (0)", "Benign (1)"], legend=False)
    plt.title("Diagnosis Distribution (0: Malignant, 1: Benign)")
    plt.ylabel("Patient Count")
    for idx, count in enumerate(target_counts.values):
        plt.text(idx, count / 2, str(count), ha="center", color="white", fontweight="bold", fontsize=12)
    plt.tight_layout()
    p1 = os.path.join(vis_dir, "target_distribution.png")
    plt.savefig(p1, dpi=150)
    plt.close()
    print(f"Saved: {p1}")

    # 2. Key Nuclear Features Scatter Plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="mean radius", y="mean texture", hue="target", palette=["#d95f02", "#1b9e77"], alpha=0.8)
    plt.title("Mean Radius vs Mean Texture by Diagnosis")
    plt.xlabel("Mean Radius")
    plt.ylabel("Mean Texture")
    plt.tight_layout()
    p2 = os.path.join(vis_dir, "radius_vs_texture.png")
    plt.savefig(p2, dpi=150)
    plt.close()
    print(f"Saved: {p2}")

    # 3. Correlation Heatmap of Primary Mean Features
    plt.figure(figsize=(8, 7))
    mean_cols = [c for c in feature_names if "mean" in c]
    corr = df[mean_cols + ["target"]].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", square=True, annot_kws={"size": 8})
    plt.title("Pearson Correlation Heatmap (Mean Nuclear Attributes)")
    plt.tight_layout()
    p3 = os.path.join(vis_dir, "correlation_heatmap.png")
    plt.savefig(p3, dpi=150)
    plt.close()
    print(f"Saved: {p3}")

    # 4. Boxplot of Mean Concave Points across Diagnoses
    plt.figure(figsize=(7, 4))
    sns.boxplot(data=df, x="target", y="mean concave points", palette=["#d95f02", "#1b9e77"], hue="target", legend=False)
    plt.xticks([0, 1], ["Malignant (0)", "Benign (1)"])
    plt.title("Distribution of Mean Concave Points across Diagnoses")
    plt.tight_layout()
    p4 = os.path.join(vis_dir, "concave_points_boxplot.png")
    plt.savefig(p4, dpi=150)
    plt.close()
    print(f"Saved: {p4}")

    print("\n" + "=" * 70)
    print("STAGE 4: FEATURE/TARGET SELECTION AND TRAIN-TEST SPLIT")
    print("=" * 70)
    
    # Stratified 80/20 train-test split to preserve diagnostic proportions
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"Training Feature Set Shape: {X_train.shape}, Testing Feature Set Shape: {X_test.shape}")
    print(f"Training Benign Ratio: {y_train.mean():.2%}, Testing Benign Ratio: {y_test.mean():.2%}")

    print("\n" + "=" * 70)
    print("STAGE 5: MODEL SELECTION AND TRAINING (DISTINCT SUITE)")
    print("=" * 70)
    
    # Defining distinct models: Logistic Regression, Support Vector Machine (RBF), K-Nearest Neighbors
    candidate_models = {
        "Logistic Regression (L2)": LogisticRegression(max_iter=1000, random_state=42),
        "Support Vector Classifier (RBF)": SVC(kernel="rbf", probability=True, C=1.0, random_state=42),
        "K-Nearest Neighbors (KNN, k=5)": KNeighborsClassifier(n_neighbors=5)
    }
    
    trained_pipelines = {}
    for name, model in candidate_models.items():
        pipeline = Pipeline([
            ("scaler", StandardScaler()),
            ("classifier", model)
        ])
        cv_auc = cross_val_score(pipeline, X_train, y_train, cv=5, scoring="roc_auc")
        pipeline.fit(X_train, y_train)
        trained_pipelines[name] = pipeline
        print(f"Trained: {name:<35} | 5-Fold CV ROC-AUC: {cv_auc.mean():.4f} (+/- {cv_auc.std():.4f})")

    print("\n" + "=" * 70)
    print("STAGE 6: MODEL EVALUATION AND INTERPRETATION")
    print("=" * 70)
    
    results = []
    plt.figure(figsize=(8, 6))
    
    for name, pipe in trained_pipelines.items():
        y_pred = pipe.predict(X_test)
        y_prob = pipe.predict_proba(X_test)[:, 1]
        
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc = roc_auc_score(y_test, y_prob)
        
        results.append({
            "Model": name,
            "Accuracy": acc,
            "Precision": prec,
            "Recall": rec,
            "F1-Score": f1,
            "ROC-AUC": roc
        })
        
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        plt.plot(fpr, tpr, label=f"{name} (AUC = {roc:.4f})")

    plt.plot([0, 1], [0, 1], 'k--', label="Random Guessing (AUC = 0.5000)")
    plt.title("ROC Curves Comparison on Held-Out Test Set")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(loc="lower right")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    roc_path = os.path.join(vis_dir, "roc_comparison.png")
    plt.savefig(roc_path, dpi=150)
    plt.close()
    print(f"Saved: {roc_path}")
    
    results_df = pd.DataFrame(results).set_index("Model")
    print("\nTest Set Clinical Benchmark Results:")
    print(results_df.round(4).to_string())
    
    best_name = results_df["ROC-AUC"].idxmax()
    print(f"\nChampion Diagnostic Model: {best_name}")
    print("\nDetailed Classification Report:")
    print(classification_report(y_test, trained_pipelines[best_name].predict(X_test), target_names=cancer.target_names))
    
    # Feature Importance / Absolute Weights from Logistic Regression
    lr_model = trained_pipelines["Logistic Regression (L2)"].named_steps["classifier"]
    coef_series = pd.Series(lr_model.coef_[0], index=feature_names).sort_values()
    top_coefs = pd.concat([coef_series.head(5), coef_series.tail(5)])
    
    plt.figure(figsize=(9, 5))
    top_coefs.plot(kind="barh", color=["#d95f02" if x < 0 else "#1b9e77" for x in top_coefs])
    plt.title("Top Diagnostic Feature Coefficients (Logistic Regression)")
    plt.xlabel("Log-Odds Coefficient Value")
    plt.tight_layout()
    imp_path = os.path.join(vis_dir, "feature_importance.png")
    plt.savefig(imp_path, dpi=150)
    plt.close()
    print(f"Saved: {imp_path}")

    # Confusion Matrix for Champion Model
    cm = confusion_matrix(y_test, trained_pipelines[best_name].predict(X_test))
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=cancer.target_names, yticklabels=cancer.target_names)
    plt.title(f"Confusion Matrix ({best_name})")
    plt.xlabel("Predicted Class")
    plt.ylabel("True Class")
    plt.tight_layout()
    cm_path = os.path.join(vis_dir, "confusion_matrix.png")
    plt.savefig(cm_path, dpi=150)
    plt.close()
    print(f"Saved: {cm_path}")

    print("\n" + "=" * 70)
    print("STAGE 7: SUMMARY & ARTIFACT GENERATION COMPLETED")
    print("=" * 70)
    print("All required 7 stages executed in exact order with zero steps skipped.")

if __name__ == "__main__":
    run_ml_pipeline()
