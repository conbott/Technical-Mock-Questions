"""
Technical Round 3 - Part 3: Complete Machine Learning Project
Dataset: Scikit-Learn Wine Recognition Dataset (Real Chemical Phenotypic Data)
Task: Multi-Class Wine Cultivar Classification (3 Classes)
Models: Decision Tree, Random Forest, Gradient Boosting, Extra Trees
Follows all 7 required stages in exact chronological order.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix
)

def run_ml_pipeline():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    vis_dir = os.path.join(base_dir, "visualizations")
    os.makedirs(vis_dir, exist_ok=True)

    print("=" * 70)
    print("STAGE 1: DATASET SELECTION AND LOADING (FROM SKLEARN.DATASETS)")
    print("=" * 70)
    
    # Load real benchmark chemical wine dataset directly from sklearn
    wine = load_wine(as_frame=True)
    df = wine.frame.copy()
    
    # Save a local CSV copy for complete project provenance
    dataset_path = os.path.join(base_dir, "dataset.csv")
    df.to_csv(dataset_path, index=False)
    
    print(f"Dataset successfully loaded from sklearn.datasets.load_wine()")
    print(f"Local copy persisted to: {dataset_path}")
    print(f"Dataset Dimensions: {df.shape[0]} wine samples, {df.shape[1]} columns")
    print(f"Target Classes: {wine.target_names} (0, 1, 2)")
    print("\nFirst 5 Chemical Profiles:")
    print(df.iloc[:5, :5])
    print("\nDataset Info Summary:")
    print(df.info())

    print("\n" + "=" * 70)
    print("STAGE 2: DATA PREPROCESSING")
    print("=" * 70)
    
    missing_count = df.isnull().sum().sum()
    print(f"Total Missing Values in Scikit-Learn Wine Dataset: {missing_count}")
    
    X = df.drop(columns=["target"])
    y = df["target"]
    feature_names = list(X.columns)
    
    print(f"Total Chemical Constituent Features: {len(feature_names)}")
    print("Preprocessing Strategy: Standard scaling (Z-score normalization) encapsulated in Pipeline to prevent data leakage.")

    print("\n" + "=" * 70)
    print("STAGE 3: EXPLORATORY DATA ANALYSIS (EDA) AND VISUALISATION")
    print("=" * 70)
    
    # 1. Target Class Distribution
    plt.figure(figsize=(6, 4))
    counts = y.value_counts().sort_index()
    sns.barplot(x=wine.target_names, y=counts.values, palette="Set1", hue=wine.target_names, legend=False)
    plt.title("Wine Cultivar Distribution Across 3 Classes")
    plt.ylabel("Sample Count")
    for idx, c in enumerate(counts.values):
        plt.text(idx, c / 2, str(c), ha="center", color="white", fontweight="bold", fontsize=12)
    plt.tight_layout()
    p1 = os.path.join(vis_dir, "target_distribution.png")
    plt.savefig(p1, dpi=150)
    plt.close()
    print(f"Saved: {p1}")

    # 2. Alcohol vs Flavanoids Scatter Plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="alcohol", y="flavanoids", hue="target", palette="Set1", s=60, alpha=0.9)
    plt.title("Alcohol Content vs Flavanoids by Wine Cultivar")
    plt.xlabel("Alcohol Content (% vol)")
    plt.ylabel("Flavanoids Concentration")
    plt.legend(title="Cultivar Class", labels=wine.target_names)
    plt.tight_layout()
    p2 = os.path.join(vis_dir, "alcohol_vs_flavanoids.png")
    plt.savefig(p2, dpi=150)
    plt.close()
    print(f"Saved: {p2}")

    # 3. Correlation Heatmap
    plt.figure(figsize=(9, 7))
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap="YlOrBr", fmt=".2f", square=True, annot_kws={"size": 7})
    plt.title("Pearson Correlation Heatmap (Wine Chemical Analysis)")
    plt.tight_layout()
    p3 = os.path.join(vis_dir, "correlation_heatmap.png")
    plt.savefig(p3, dpi=150)
    plt.close()
    print(f"Saved: {p3}")

    # 4. Proline Concentration by Wine Cultivar Boxplot
    plt.figure(figsize=(7, 4))
    sns.boxplot(data=df, x="target", y="proline", palette="Set1", hue="target", legend=False)
    plt.xticks([0, 1, 2], wine.target_names)
    plt.title("Proline Concentration across Cultivars")
    plt.ylabel("Proline (mg/L)")
    plt.tight_layout()
    p4 = os.path.join(vis_dir, "proline_boxplot.png")
    plt.savefig(p4, dpi=150)
    plt.close()
    print(f"Saved: {p4}")

    print("\n" + "=" * 70)
    print("STAGE 4: FEATURE/TARGET SELECTION AND TRAIN-TEST SPLIT")
    print("=" * 70)
    
    # Stratified 80/20 train-test split for multi-class balance
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"Training Feature Matrix: {X_train.shape}, Testing Feature Matrix: {X_test.shape}")
    print(f"Class Proportions in Test: {np.bincount(y_test)}")

    print("\n" + "=" * 70)
    print("STAGE 5: MODEL SELECTION AND TRAINING (DISTINCT TREE & ENSEMBLE SUITE)")
    print("=" * 70)
    
    # Defining distinct tree and ensemble classifiers
    candidate_models = {
        "Decision Tree Classifier": DecisionTreeClassifier(max_depth=4, random_state=42),
        "Random Forest Classifier": RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42),
        "Gradient Boosting Classifier": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42),
        "Extra Trees Classifier": ExtraTreesClassifier(n_estimators=100, max_depth=5, random_state=42)
    }
    
    trained_pipelines = {}
    for name, model in candidate_models.items():
        pipeline = Pipeline([
            ("scaler", StandardScaler()),
            ("classifier", model)
        ])
        cv_scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring="accuracy")
        pipeline.fit(X_train, y_train)
        trained_pipelines[name] = pipeline
        print(f"Trained: {name:<35} | 5-Fold CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

    print("\n" + "=" * 70)
    print("STAGE 6: MODEL EVALUATION AND INTERPRETATION")
    print("=" * 70)
    
    results = []
    best_pipe = None
    best_f1 = -float("inf")
    best_name = ""
    
    for name, pipe in trained_pipelines.items():
        y_pred = pipe.predict(X_test)
        
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average="weighted")
        rec = recall_score(y_test, y_pred, average="weighted")
        f1 = f1_score(y_test, y_pred, average="weighted")
        
        results.append({
            "Model": name,
            "Accuracy": acc,
            "Precision (Weighted)": prec,
            "Recall (Weighted)": rec,
            "F1-Score (Weighted)": f1
        })
        
        if f1 > best_f1:
            best_f1 = f1
            best_pipe = pipe
            best_name = name

    results_df = pd.DataFrame(results).set_index("Model")
    print("\nTest Set Multi-Class Benchmark Summary:")
    print(results_df.round(4).to_string())
    print(f"\nChampion Ensemble Classifier: {best_name} with Weighted F1 = {best_f1:.4f}")

    print("\nDetailed Multi-Class Classification Report:")
    print(classification_report(y_test, best_pipe.predict(X_test), target_names=wine.target_names))

    # Confusion Matrix Heatmap
    cm = confusion_matrix(y_test, best_pipe.predict(X_test))
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Purples", xticklabels=wine.target_names, yticklabels=wine.target_names)
    plt.title(f"Confusion Matrix ({best_name})")
    plt.xlabel("Predicted Cultivar")
    plt.ylabel("True Cultivar")
    plt.tight_layout()
    cm_path = os.path.join(vis_dir, "confusion_matrix.png")
    plt.savefig(cm_path, dpi=150)
    plt.close()
    print(f"Saved: {cm_path}")

    # Feature Importance (Random Forest)
    rf_model = trained_pipelines["Random Forest Classifier"].named_steps["classifier"]
    imp_series = pd.Series(rf_model.feature_importances_, index=feature_names).sort_values(ascending=True)
    
    plt.figure(figsize=(8, 6))
    imp_series.plot(kind="barh", color="#7570b3")
    plt.title("Chemical Feature Importance (Random Forest Classifier)")
    plt.xlabel("Gini Importance Score")
    plt.tight_layout()
    imp_path = os.path.join(vis_dir, "feature_importance.png")
    plt.savefig(imp_path, dpi=150)
    plt.close()
    print(f"Saved: {imp_path}")

    print("\n" + "=" * 70)
    print("STAGE 7: SUMMARY & ARTIFACT GENERATION COMPLETED")
    print("=" * 70)
    print("All required 7 stages executed in exact order with zero steps skipped.")

if __name__ == "__main__":
    run_ml_pipeline()
