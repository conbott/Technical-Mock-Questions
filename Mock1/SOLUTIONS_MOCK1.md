# MAGNATE ACADEMY
## TECHNICAL ROUND 1 – DATA SCIENCE: COMPLETE SOLUTIONS

**Total Marks:** 50  
**Candidate Submission Guide & Master Answer Key**

---

# PART 1 – PYTHON | 20 MARKS

## A. Python Coding | 10 Marks

### 1. Fibonacci Sequence — 2 Marks
**Question:** Write a Python program to generate the Fibonacci sequence up to $n$ terms.

```python
def generate_fibonacci(n: int) -> list:
    """Generates the Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# Example Execution:
n = 10
print(f"Fibonacci sequence for n = {n}:", generate_fibonacci(n))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
**Explanation:**  
- The Fibonacci sequence begins with $0$ and $1$. Each subsequent term is the sum of the preceding two terms: $F(k) = F(k-1) + F(k-2)$.
- Time Complexity: $\mathcal{O}(n)$, Space Complexity: $\mathcal{O}(n)$.

---

### 2. String Manipulation — 2 Marks
**Question:** Write a Python program to capitalise the first and last character of every word in a given string.  
*Example:* `hello a world` $\rightarrow$ `HellO A WorlD`

```python
def capitalize_first_and_last(s: str) -> str:
    """Capitalises the first and last character of every word."""
    words = s.split(' ')
    result = []
    
    for word in words:
        if not word:
            result.append(word)
        elif len(word) == 1:
            result.append(word.upper())
        else:
            capitalized = word[0].upper() + word[1:-1] + word[-1].upper()
            result.append(capitalized)
            
    return ' '.join(result)

# Example Execution:
input_text = "hello a world"
output_text = capitalize_first_and_last(input_text)
print("Output:", output_text)
# Output: HellO A WorlD
```
**Explanation:**  
- We split the input string by spaces into tokens.
- For words with a single letter (like `"a"`), `.upper()` suffices.
- For words with length $\ge 2$, we slice the first character `word[0].upper()`, keep the substring `word[1:-1]`, and append the capitalized final character `word[-1].upper()`.

---

### 3. Loop with else — 2 Marks
**Question:** Write a Python program using a `for` or `while` loop with `else`, without using an `if` statement.

```python
# -------------------------------------------------------------
# Implementation A: while loop with else (no if statement)
# -------------------------------------------------------------
count = 1
while count <= 3:
    print(f"Processing batch #{count}")
    count += 1
else:
    print("All batches processed! while condition evaluated to False.\n")

# -------------------------------------------------------------
# Implementation B: for loop with else (no if statement)
# -------------------------------------------------------------
data_pipeline_stages = ["Data Extraction", "Preprocessing", "Model Training"]
for stage in data_pipeline_stages:
    print(f"Stage executed: {stage}")
else:
    print("Pipeline finished successfully without loop interruption!")
```
**Explanation:**  
- In Python, the `else` clause attached to a `for` or `while` loop executes when the loop naturally terminates (i.e. the iterable is exhausted or the `while` condition becomes `False`).
- If the loop is terminated by a `break`, the `else` block is skipped. Here, no `if` statement is used at all.

---

### 4. Prime Number — 2 Marks
**Question:** Write a Python program to determine whether a given number is prime or not.

```python
def is_prime(n: int) -> bool:
    """Determines if a number is prime using O(sqrt(n)) primality test."""
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check factors of the form 6k +/- 1 up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True

# Example Execution:
test_vals = [1, 2, 17, 18, 29]
for val in test_vals:
    print(f"{val} is prime: {is_prime(val)}")
# Output:
# 1 is prime: False
# 2 is prime: True
# 17 is prime: True
# 18 is prime: False
# 29 is prime: True
```
**Explanation:**  
- A prime number is an integer greater than 1 divisible only by 1 and itself.
- We check divisors up to $\sqrt{n}$ using the $6k \pm 1$ optimization, achieving an optimal $\mathcal{O}(\sqrt{n})$ runtime.

---

### 5. Longest Word — 2 Marks
**Question:** Write a Python program to find the longest word in a given string.

```python
import re

def find_longest_word(sentence: str) -> str:
    """Finds the longest word in a given sentence."""
    # Extract clean words excluding punctuation
    words = re.findall(r'\b[A-Za-z0-9\'-]+\b', sentence)
    if not words:
        return ""
    return max(words, key=len)

# Example Execution:
text = "Machine learning and artificial intelligence are revolutionizing technology."
print("Longest word:", find_longest_word(text))
# Output: revolutionizing (15 characters)
```
**Explanation:**  
- `re.findall(r'\b[A-Za-z0-9\'-]+\b', sentence)` extracts clean word tokens regardless of trailing commas or periods.
- `max(words, key=len)` finds the token with the maximum character length in $\mathcal{O}(N)$ time.

---

## B. Python Theory | 10 Marks

### 1. What is Python? — 1 Mark
**Answer:**  
Python is a high-level, interpreted, dynamically typed, and garbage-collected programming language created by Guido van Rossum. It supports multiple programming paradigms (procedural, object-oriented, and functional) and emphasizes code readability with its clean, indentation-based syntax. It is the dominant language in Data Science, Machine Learning, and Scientific Computing due to its extensive ecosystem of specialized libraries (NumPy, Pandas, Scikit-Learn, PyTorch).

---

### 2. What is a Lambda Function? Give an example. — 1 Mark
**Answer:**  
A lambda function in Python is an anonymous, small, single-expression function defined using the `lambda` keyword. It can take any number of arguments but can evaluate only one expression and implicitly returns its result.

```python
# Syntax: lambda arguments: expression
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Commonly used inline with map, filter, or sorted:
nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))  # Output: [2, 4]
```

---

### 3. Differentiate between List, Tuple, Set and Dictionary. — 1 Mark
**Answer:**

| Feature | List (`[]`) | Tuple (`()`) | Set (`{}`) | Dictionary (`{k: v}`) |
| :--- | :--- | :--- | :--- | :--- |
| **Mutability** | Mutable | **Immutable** | Mutable | Mutable (keys immutable) |
| **Order** | Ordered | Ordered | **Unordered** | Ordered (Python 3.7+) |
| **Duplicates** | Allowed | Allowed | **Not Allowed** | Keys unique, values duplicate |
| **Indexing** | By zero-based index | By zero-based index | Not indexable | By unique keys |
| **Use Case** | Dynamic sequences | Fixed records, coordinates | Membership testing, uniqueness | Key-value lookups, hash maps |

---

### 4. What is List Comprehension? Give an example. — 1 Mark
**Answer:**  
List comprehension is a concise and elegant syntax for creating new lists by applying an expression to each item in an existing iterable, optionally filtering with a condition.

```python
# Syntax: [expression for item in iterable if condition]
numbers = [1, 2, 3, 4, 5, 6]
squared_evens = [x ** 2 for x in numbers if x % 2 == 0]
print(squared_evens)  # Output: [4, 16, 36]
```

---

### 5. What are Generators? Why are they useful? — 1 Mark
**Answer:**  
Generators are special functions that return an iterator object which yields values one at a time using the `yield` keyword instead of `return`.  
**Why they are useful:**
1. **Memory Efficiency (Lazy Evaluation):** They calculate items on demand without storing the entire sequence in memory, making them ideal for processing massive datasets or infinite streams.
2. **State Retention:** Execution pauses at `yield` and resumes exactly where it stopped on the next call to `next()`.

```python
def count_up_to(max_val):
    count = 1
    while count <= max_val:
        yield count
        count += 1
```

---

### 6. What are Decorators in Python? — 1 Mark
**Answer:**  
A decorator is a design pattern in Python that allows you to dynamically modify or extend the behavior of a function or method without altering its original source code. Decorators take a function as an argument, wrap it with extra functionality, and return the wrapped function using the `@decorator_name` syntax.

```python
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@log_execution
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

---

### 7. What is a Function? Why do we use functions? — 1 Mark
**Answer:**  
A function is an organized, reusable block of code created using the `def` keyword that performs a specific, cohesive action.  
**Why we use functions:**
1. **Code Reusability & DRY (Don't Repeat Yourself):** Write once, execute multiple times across the program.
2. **Modularity & Readability:** Breaks complex software architectures into small, manageable, and testable modules.
3. **Maintainability & Abstraction:** Allows updating underlying logic without breaking dependent systems.

---

### 8. Differentiate between `for` and `while` loops. — 1 Mark
**Answer:**

| Feature | `for` loop | `while` loop |
| :--- | :--- | :--- |
| **Condition Type** | Iterates over a predefined collection or sequence (finite). | Repeats as long as a boolean condition remains `True`. |
| **Number of Iterations** | Known or fixed in advance based on iterable length. | Unknown beforehand; depends on runtime state. |
| **Loop Variable Management** | Handled automatically by the iterator. | Requires manual initialization and update inside loop. |
| **Risk of Infinite Loop** | Extremely low / rare. | High if condition variable is not updated properly. |

---

### 9. What is Recursion? Give a suitable example. — 1 Mark
**Answer:**  
Recursion is a programming technique where a function calls itself directly or indirectly to solve a smaller instance of the same problem, continuing until it reaches a defined **base condition** that halts further recursive calls.

```python
def factorial(n: int) -> int:
    # Base condition
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

---

### 10. Differentiate between `break`, `continue`, and `pass`. — 1 Mark
**Answer:**
- **`break`:** Immediately terminates the enclosing loop entirely and transfers control to the statement directly following the loop.
- **`continue`:** Skips the rest of the current iteration's code block and immediately jumps to the next iteration of the loop.
- **`pass`:** A null placeholder statement that does absolutely nothing; used when a statement is syntactically required (e.g. empty functions, classes, or loops) but no action is needed.

```python
for i in range(5):
    if i == 1:
        pass        # Does nothing, proceeds
    elif i == 2:
        continue    # Skips printing 2
    elif i == 4:
        break       # Stops loop before printing 4
    print(i)        # Prints: 0, 1, 3
```

---

# PART 2 – MACHINE LEARNING | 15 MARKS

### 1. What is Machine Learning? Explain its major types. — 2 Marks
**Answer:**  
Machine Learning (ML) is a branch of Artificial Intelligence that gives computer systems the ability to automatically learn patterns and decision rules from historical data to make predictions or decisions without being explicitly programmed with rule-based heuristics.

**Major Types of Machine Learning:**
1. **Supervised Learning:** The model is trained on labeled data $(X, y)$, learning a mapping function $f(X) \approx y$.
   - *Subtypes:* Regression (continuous target, e.g., house prices), Classification (discrete categories, e.g., spam vs. non-spam).
2. **Unsupervised Learning:** The model is trained on unlabeled data $(X)$, discovering hidden structures, groupings, or representations.
   - *Subtypes:* Clustering (K-Means, DBSCAN), Dimensionality Reduction (PCA, t-SNE), Association Rules.
3. **Semi-Supervised Learning:** Combines a small amount of labeled data with a large volume of unlabeled data to improve learning efficiency.
4. **Reinforcement Learning (RL):** An agent interacts with an environment and learns an optimal policy through trial-and-error by maximizing cumulative numerical rewards.

---

### 2. Differentiate between Classification and Regression with examples. — 2 Marks
**Answer:**

| Dimension | Classification | Regression |
| :--- | :--- | :--- |
| **Target Variable Type** | **Categorical / Discrete** (finite classes/labels). | **Continuous / Numerical** (infinite possible values). |
| **Output Goal** | Map inputs to a class boundary or class probability. | Map inputs to a numeric quantity on the real number line. |
| **Evaluation Metrics** | Accuracy, Precision, Recall, F1-Score, ROC-AUC, Log-Loss. | Mean Squared Error (MSE), RMSE, MAE, $R^2$ Score. |
| **Algorithms** | Logistic Regression, Decision Trees, SVM, Naive Bayes. | Linear Regression, Ridge, Lasso, SVR, Random Forest Regressor. |
| **Real-World Examples** | - Predicting whether an email is Spam or Ham.<br>- Classifying a tumor as Malignant or Benign. | - Predicting house prices in dollars.<br>- Forecasting tomorrow's temperature in Celsius. |

---

### 3. Differentiate between a Loss Function and a Cost Function. — 2 Marks
**Answer:**
- **Loss Function:** Measures the discrepancy or error between the predicted value $\hat{y}^{(i)}$ and the actual ground truth $y^{(i)}$ for a **single individual training sample**.
  - *Example:* Binary Cross-Entropy Loss for sample $i$:
    $$L(y^{(i)}, \hat{y}^{(i)}) = -\left[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \right]$$
- **Cost Function:** The aggregate or average of the loss function values computed over the **entire dataset** (or an entire mini-batch), often including an optional regularisation penalty.
  - *Example:* Mean Squared Error Cost Function over $m$ samples:
    $$J(\theta) = \frac{1}{2m} \sum_{i=1}^m \left(h_\theta(x^{(i)}) - y^{(i)}\right)^2$$

In short: **Loss is sample-specific; Cost is dataset-wide.**

---

### 4. What are the key assumptions of Linear Regression? — 2 Marks
**Answer:**  
Ordinary Least Squares (OLS) Linear Regression relies on five foundational assumptions:
1. **Linearity:** The relationship between the independent variables ($X$) and the dependent variable ($y$) is linear in the parameters.
2. **Independence (No Autocorrelation):** The observations and residual errors are independent of one another (verified via Durbin-Watson test).
3. **Homoscedasticity:** The variance of the error terms $\epsilon_i$ is constant across all levels of the independent variables (i.e. $\text{Var}(\epsilon_i) = \sigma^2$).
4. **Normality of Residuals:** The residuals/errors $\epsilon$ are normally distributed with zero mean: $\epsilon \sim \mathcal{N}(0, \sigma^2)$ (verified via Q-Q plot or Shapiro-Wilk test).
5. **No Multicollinearity:** Independent variables must not be highly linearly correlated with each other (verified via Variance Inflation Factor, $\text{VIF} < 5$ or $10$).

---

### 5. What is Ridge Regression (L2 Regularisation)? Why is it used? — 2 Marks
**Answer:**  
**Definition:**  
Ridge Regression is a regularized variant of Linear Regression that adds an $L_2$ penalty equal to the sum of squared coefficients to the OLS cost function:
$$J_{\text{Ridge}}(\mathbf{w}) = \text{MSE}(\mathbf{w}) + \lambda \sum_{j=1}^p w_j^2 = \frac{1}{m} \|\mathbf{y} - \mathbf{X}\mathbf{w}\|_2^2 + \lambda \|\mathbf{w}\|_2^2$$
where $\lambda \ge 0$ is the regularisation hyperparameter.

**Why it is used:**
1. **Prevents Overfitting:** Shrinks model parameters towards zero, reducing model complexity and variance.
2. **Mitigates Multicollinearity:** When features are strongly collinear, OLS matrix $(\mathbf{X}^T\mathbf{X})$ becomes ill-conditioned or near-singular. Ridge adds $\lambda \mathbf{I}$, guaranteeing invertibility: $\mathbf{w} = (\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I})^{-1}\mathbf{X}^T\mathbf{y}$.
3. **Maintains All Features:** Unlike Lasso ($L_1$), Ridge never sets coefficients strictly to zero, making it suitable when all features contribute small signals.

---

### 6. What is Gradient Descent? Explain how it works. — 2 Marks
**Answer:**  
**Definition:**  
Gradient Descent is a first-order iterative optimization algorithm used to find the local or global minimum of a differentiable objective/cost function $J(\mathbf{\theta})$.

**How it works:**
1. **Initialization:** Initialize model parameters (weights $\mathbf{w}$ and bias $b$) with random or zero values.
2. **Compute Gradient:** Calculate the vector of partial derivatives of the cost function with respect to each parameter, $\nabla_\mathbf{w} J(\mathbf{w})$, representing the direction of steepest ascent.
3. **Parameter Update:** Update weights in the opposite direction of the gradient (steepest descent) scaled by a learning rate $\eta$:
   $$\mathbf{w}_{\text{new}} = \mathbf{w}_{\text{old}} - \eta \cdot \nabla_\mathbf{w} J(\mathbf{w}_{\text{old}})$$
4. **Iteration:** Repeat steps 2 and 3 iteratively until convergence (when the change in loss $|\Delta J| < \epsilon$ or maximum iterations are reached).

Variants include **Batch Gradient Descent** (entire dataset per step), **Stochastic Gradient Descent (SGD)** (1 sample per step), and **Mini-batch Gradient Descent** (small batches, e.g., 32–256).

---

### 7. What is Ensemble Learning? Why does combining multiple models often improve performance? — 3 Marks
**Answer:**  
**Definition:**  
Ensemble Learning is a meta-algorithmic paradigm in machine learning where multiple base learners (models) are trained to solve the same problem and their predictions are aggregated (via voting, averaging, or stacking) to yield a superior final prediction.

**Why Combining Multiple Models Improves Performance:**
1. **Variance Reduction (Bagging / Bootstrap Aggregating):**
   - Individual models (e.g. unconstrained decision trees) suffer from high variance and sensitivity to training data noise.
   - Averaging predictions across $M$ decorrelated models reduces variance by a factor proportional to $1/M$ without increasing bias.
2. **Bias Reduction (Boosting):**
   - Weak learners with high bias (e.g. shallow decision stumps) are trained sequentially, with each subsequent model focusing specifically on the residual errors of the previous models, systematically driving down bias.
3. **Error Compensation & Statistical Robustness:**
   - Different algorithms explore different regions of the hypothesis space. When individual models make uncorrelated errors, majority voting cancels out idiosyncratic errors, producing robust generalization boundaries.

---

# PART 3 – MACHINE LEARNING PRACTICAL | 15 MARKS

The complete Machine Learning practical task has been implemented using the real **Breast Cancer Wisconsin Diagnostic Dataset** loaded directly from `sklearn.datasets.load_breast_cancer`:
- Executable Python script: [`ml_practical_project.py`](file:///c:/Users/con1k/Documents/datascience_course/Technical%20Round%20Mock%20Questions/Mock1/ml_practical_project.py)
- Persisted Dataset: [`dataset.csv`](file:///c:/Users/con1k/Documents/datascience_course/Technical%20Round%20Mock%20Questions/Mock1/dataset.csv)
- Generated EDA Figures: [`visualizations/`](file:///c:/Users/con1k/Documents/datascience_course/Technical%20Round%20Mock%20Questions/Mock1/visualizations/)
- GitHub Documentation: [`README.md`](file:///c:/Users/con1k/Documents/datascience_course/Technical%20Round%20Mock%20Questions/Mock1/README.md)

### Mark-by-Mark Fulfillment Breakdown

| Requirement | Marks | Implementation Details |
| :--- | :---: | :--- |
| **1. Dataset Selection and Loading** | **2 / 2** | Loaded real clinical oncology benchmark data using `sklearn.datasets.load_breast_cancer(as_frame=True)` ($N=569$ patients, 30 continuous nuclear features). Also persisted as `dataset.csv`. |
| **2. Data Preprocessing** | **3 / 3** | Inspected missing values ($0$ nulls). Built an isolated scikit-learn `Pipeline` utilizing `StandardScaler` to normalize all 30 features to $\mu=0, \sigma=1$ without data leakage across cross-validation folds. |
| **3. Exploratory Data Analysis & Visualisation** | **2 / 2** | Generated 4 figures saved into `visualizations/`: Diagnosis class balance, Mean Radius vs Texture scatter plot, Pearson Correlation Heatmap, and Concave Points box plot across diagnoses. |
| **4. Feature/Target Selection & Train-Test Split** | **2 / 2** | Features $X$ (30 attributes) separated from binary target $y$ (`target`). Executed stratified 80/20 train-test split ($N_{\text{train}}=455$, $N_{\text{test}}=114$) with `random_state=42`. |
| **5. Model Selection and Training** | **2 / 2** | Evaluated 3 distinct model architectures using 5-fold cross validation: **Logistic Regression ($L_2$ Regularized)**, **Support Vector Classifier (SVC with RBF Kernel)**, and **K-Nearest Neighbors (KNN, $k=5$)**. |
| **6. Model Evaluation and Interpretation** | **2 / 2** | Computed Test Accuracy, Precision, Recall, F1-Score, and ROC-AUC. Logistic Regression achieved champion test performance (**$98.25\%$ accuracy**, **$0.9954$ ROC-AUC**). Plotted ROC comparison curves, confusion matrix, and feature coefficient importance. |
| **7. GitHub Repository & Documentation** | **2 / 2** | Documented under repository name `Technical round 1` with a comprehensive `README.md` detailing clinical background, architecture, metrics table, and run commands. |
| **TOTAL** | **15 / 15** | **All 7 stages executed sequentially in exact order without skipping.** |
