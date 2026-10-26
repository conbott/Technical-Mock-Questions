# Technical Round Mock Questions & Solutions

Comprehensive solutions, runnable Python scripts, end-to-end Machine Learning pipelines using real `sklearn.datasets`, and complete SQL interview question sets prepared for Data Science Technical Assessment Rounds (Magnate Academy).

---

## Repository Structure

```
.
├── Mock1/
│   ├── TECHNICAL ROUND 1 .pdf        # Original assessment document
│   ├── SOLUTIONS_MOCK1.md            # Complete theoretical & practical solutions
│   ├── python_coding_solutions.py    # Python coding tasks (Fibonacci, String Manipulation, etc.)
│   ├── ml_practical_project.py       # End-to-end ML project (Breast Cancer Diagnostic Classification)
│   ├── dataset.csv                   # Persisted real dataset from sklearn.datasets.load_breast_cancer
│   ├── README.md                     # Dedicated project documentation
│   └── visualizations/               # EDA charts, correlation matrix, ROC curves, confusion matrix
│
├── Mock2/
│   ├── Technical round 2.pdf         # Original assessment document
│   ├── SOLUTIONS_MOCK2.md            # Complete theoretical & practical solutions
│   ├── python_coding_solutions.py    # Python coding tasks (Extrema, Non-repeating char, Anagram, etc.)
│   ├── ml_practical_project.py       # End-to-end ML project (California Housing Valuation Regression)
│   ├── dataset.csv                   # Persisted real dataset from sklearn.datasets.fetch_california_housing
│   ├── README.md                     # Dedicated project documentation
│   └── visualizations/               # EDA charts, regression fit, coefficients, residuals
│
├── Mock3/
│   ├── Technical round 3.pdf         # Compiled 5-page PDF of all question pages
│   ├── SOLUTIONS_MOCK3.md            # Complete theoretical & practical solutions (Python, ML, DL, NLP, GenAI)
│   ├── python_coding_solutions.py    # Python coding tasks (Char frequency, 2nd largest, Two sum, Palindrome)
│   ├── ml_practical_project.py       # End-to-end ML project (Wine Cultivar Multi-Class Classification)
│   ├── dataset.csv                   # Persisted real dataset from sklearn.datasets.load_wine
│   ├── README.md                     # Dedicated project documentation
│   └── visualizations/               # EDA charts, confusion matrix, Gini feature importance
│
└── SQL_Mock/
    ├── SQL Interview Questions.pdf   # Original assessment PDF (150 SQL questions)
    ├── SOLUTIONS_SQL_MOCK.md         # Comprehensive master answers for all 150 SQL questions
    └── sql_queries_reference.sql     # Practical SQL DDL schemas, window functions, and analytics queries
```

---

## Overview of Technical Rounds

### 1. [Mock 1 — Binary Classification](Mock1/)
* **Focus Areas:** Python Fundamentals (Fibonacci, String Manipulation, Loops without `if`, Primality, Longest Word), Python Theory, Core Machine Learning Principles.
* **Practical Project:** Clinical Breast Cancer Diagnosis using `sklearn.datasets.load_breast_cancer` (569 samples, 30 features).
* **Models Trained:** Logistic Regression ($L_2$), Support Vector Classifier (SVC with RBF Kernel), K-Nearest Neighbors (KNN).
* **Champion Model:** Logistic Regression ($98.25\%$ Test Accuracy, $0.9954$ ROC-AUC).

### 2. [Mock 2 — Continuous Econometric Regression](Mock2/)
* **Focus Areas:** Python Coding (Min/Max, Non-repeating Character, Anagram without `sorted()`, Dict Merging, Missing Number), ML Diagnostics (Overfitting/Underfitting, Voting, Boosting vs Bagging), Deep Learning & NLP Fundamentals.
* **Practical Project:** California Housing Price Valuation using `sklearn.datasets.fetch_california_housing` (20,640 census block groups, 8 continuous features).
* **Models Trained:** Ordinary Least Squares (OLS), Ridge Regression ($L_2$), Lasso Regression ($L_1$), ElasticNet ($L_1+L_2$).
* **Champion Model:** Lasso Regression ($R^2 = 0.5816$, $\text{RMSE} = 0.7404$).

### 3. [Mock 3 — Multi-Class Classification & GenAI](Mock3/)
* **Focus Areas:** Python Coding (Frequency Map, 2nd Largest without sort, Deduplication preserving order, Two Sum, Palindrome), Machine Learning, Deep Learning (Vanishing Gradients, Optimizers, Activation Functions), NLP (Stemming/Lemmatization, BoW vs TF-IDF, Embeddings), and Generative AI (RAG, Metadata, Citations, LLMs).
* **Practical Project:** Multi-Class Wine Cultivar Phenotypic Classification using `sklearn.datasets.load_wine` (178 samples, 13 chemical features, 3 classes).
* **Models Trained:** Decision Tree Classifier, Random Forest Classifier, Gradient Boosting Classifier, Extra Trees Classifier.
* **Champion Models:** Random Forest and Extra Trees ($100\%$ Test Accuracy, Weighted $\text{F1} = 1.0000$).

### 4. [SQL Mock — 150 Technical Interview Questions](SQL_Mock/)
* **Sections Covered:**
  1. SQL Fundamentals (Q1–Q30)
  2. Filtering & Constraints (Q31–Q55)
  3. Aggregate Functions & Grouping (Q56–Q70)
  4. Joins & Relationships (Q71–Q90)
  5. Subqueries & Set Operations (Q91–Q105)
  6. Window Functions & Ranking (Q106–Q120)
  7. Database Design, Transactions & Performance (Q121–Q140)
  8. MySQL Internals & Real-World Problem Solving (Q141–Q150)
* **Code Reference:** [`sql_queries_reference.sql`](SQL_Mock/sql_queries_reference.sql) with executable DDL schemas, window functions, and analytics queries.

---

## Environment Setup & Installation

Clone the repository and install the standard scientific Python dependencies:

```bash
git clone https://github.com/conbott/Technical-Mock-Questions.git
cd Technical-Mock-Questions

# Install required libraries
pip install numpy pandas matplotlib seaborn scikit-learn pillow
```

Run any practical project or coding suite:
```bash
# Example: Run Mock 1 Practical
python Mock1/ml_practical_project.py

# Example: Run Mock 2 Coding Solutions
python Mock2/python_coding_solutions.py
```
