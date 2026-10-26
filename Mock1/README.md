# Technical Round 1 — Data Science & Machine Learning Project

**Project Name:** Clinical Breast Cancer Diagnostic Classification Engine  
**Dataset Source:** `sklearn.datasets.load_breast_cancer` (Wisconsin Diagnostic Dataset)  
**Repository Name:** `Technical round 1`  
**Candidate Submission for Magnate Academy Technical Assessment**

---

## 📌 Executive Summary
This repository contains the complete end-to-end Machine Learning pipeline developed for **Technical Round 1**. The goal is to accurately classify cell nuclei biopsies as either **Malignant** ($0$) or **Benign** ($1$) using real clinical diagnostic measurements loaded directly from `sklearn.datasets`. All 7 required assessment stages have been executed strictly in chronological order without omission.

---

## 🏗️ Project Architecture & Workflow Stages

```mermaid
flowchart LR
    A["Stage 1: Dataset Loading (sklearn.datasets)"] --> B["Stage 2: Data Preprocessing"]
    B --> C["Stage 3: Exploratory Data Analysis"]
    C --> D["Stage 4: Feature/Target Split"]
    D --> E["Stage 5: Model Selection & Training"]
    E --> F["Stage 6: Evaluation & Interpretation"]
    F --> G["Stage 7: Documentation & Artifacts"]
```

### Stage 1: Dataset Selection and Loading
- **Dataset Source:** `sklearn.datasets.load_breast_cancer(as_frame=True)`.
- **Sample Size:** 569 patients, 30 continuous nuclear morphological features.
- **Features Captured:**
  - Mean, Standard Error, and "Worst" (mean of 3 largest values) for 10 attributes: `radius`, `texture`, `perimeter`, `area`, `smoothness`, `compactness`, `concavity`, `concave points`, `symmetry`, and `fractal dimension`.
  - Target: Binary diagnosis (`0 = Malignant` [212 cases], `1 = Benign` [357 cases]).
  - Local persistence: [`dataset.csv`](file:///c:/Users/con1k/Documents/datascience_course/Technical%20Round%20Mock%20Questions/Mock1/dataset.csv).

### Stage 2: Data Preprocessing
- **Missing Value Handling:** Verified 0 missing entries in the clinical benchmark dataset.
- **Leak-Free Transformation Pipeline:** Applied `StandardScaler` inside scikit-learn `Pipeline` to ensure all 30 features have zero mean and unit variance without data leakage across folds.

### Stage 3: Exploratory Data Analysis & Visualisations
Visualizations generated in [`visualizations/`](file:///c:/Users/con1k/Documents/datascience_course/Technical%20Round%20Mock%20Questions/Mock1/visualizations/):
1. `target_distribution.png`: Class balance between Malignant and Benign diagnoses.
2. `radius_vs_texture.png`: Scatter plot mapping cell nucleus radius against texture showing distinct cluster boundaries.
3. `correlation_heatmap.png`: Pearson correlation matrix among nuclear mean attributes.
4. `concave_points_boxplot.png`: Distribution comparison of concave points across tumor classes.

### Stage 4: Feature/Target Selection & Train-Test Split
- **Feature Matrix ($X$):** 30 clinical predictors.
- **Target Vector ($y$):** Binary diagnosis.
- **Splitting Strategy:** Stratified 80% Training ($N = 455$), 20% Testing ($N = 114$) with `random_state=42`.

### Stage 5: Model Selection and Training
Three distinct model architectures evaluated via 5-fold cross-validation:
1. **Logistic Regression ($L_2$ Regularized):** Highly interpretable linear log-odds classifier.
2. **Support Vector Classifier (SVC with RBF Kernel):** Non-linear maximum-margin hyperplane separator.
3. **K-Nearest Neighbors (KNN, $k=5$):** Non-parametric instance-based classifier.

### Stage 6: Model Evaluation and Interpretation
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-Score, and ROC-AUC.
- **Performance Summary:**

| Model | Test Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression ($L_2$)** | **0.9825** | **0.9861** | **0.9861** | **0.9861** | **0.9954** |
| **Support Vector Classifier (RBF)** | 0.9825 | 0.9861 | 0.9861 | 0.9861 | 0.9950 |
| **K-Nearest Neighbors ($k=5$)** | 0.9561 | 0.9589 | 0.9722 | 0.9655 | 0.9788 |

- **Key Insights:**
  - `worst concave points`, `worst perimeter`, and `worst radius` are the most influential predictors separating malignant from benign tumors.
  - Logistic Regression achieved champion performance with **$98.25\%$ accuracy** and **$0.9954$ ROC-AUC**.

---

## 🚀 How to Run the Project
```bash
# Run practical pipeline
python ml_practical_project.py

# Run Python coding solutions
python python_coding_solutions.py
```
