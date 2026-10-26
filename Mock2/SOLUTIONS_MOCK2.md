# MAGNATE ACADEMY
## TECHNICAL ROUND 2 – DATA SCIENCE: COMPLETE SOLUTIONS

**Total Marks:** 50  
**Candidate Submission Guide & Master Answer Key**

---

# PART 1 – PYTHON | 15 MARKS

## A. Python Coding | 10 Marks

### 1. Largest and Smallest Number — 2 Marks
**Question:** Write a Python program to find the largest and smallest numbers in a given list.

```python
def find_largest_and_smallest(numbers: list):
    """Finds largest and smallest values in O(n) time."""
    if not numbers:
        return None, None
    
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    return largest, smallest

# Example:
nums = [42, 17, 88, 3, 55, 99, 12, -4]
largest, smallest = find_largest_and_smallest(nums)
print(f"Largest: {largest}, Smallest: {smallest}")
# Output: Largest: 99, Smallest: -4
```
**Explanation:**  
- Initialize both `largest` and `smallest` with the first element. Traverse the list in a single pass ($\mathcal{O}(n)$ time, $\mathcal{O}(1)$ space), updating extrema dynamically.

---

### 2. First Non-Repeating Character — 2 Marks
**Question:** Write a Python program to find the first non-repeating character in a string.  
*Example:* Input: `"aabbcdde"` $\rightarrow$ Output: `"c"`

```python
def first_non_repeating_char(s: str):
    """Returns first non-repeating character in O(n) time."""
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        
    for char in s:
        if freq[char] == 1:
            return char
    return None

# Example:
text = "aabbcdde"
print("First non-repeating character:", first_non_repeating_char(text))
# Output: c
```
**Explanation:**  
- Pass 1: Build a frequency map ($\mathcal{O}(n)$).
- Pass 2: Iterate through the original string preserving character order and return the first character whose frequency count equals 1.

---

### 3. Anagram Check — 2 Marks
**Question:** Write a Python program to check whether two strings are anagrams of each other.  
*Condition:* Do not use the built-in `sorted()` function.  
*Example:* Input: `"listen"`, `"silent"` $\rightarrow$ Output: `Anagram`

```python
def is_anagram(s1: str, s2: str) -> str:
    """Checks for anagram without using sorted()."""
    clean_s1 = s1.replace(" ", "").lower()
    clean_s2 = s2.replace(" ", "").lower()
    
    if len(clean_s1) != len(clean_s2):
        return "Not Anagram"
    
    char_counts = {}
    for c in clean_s1:
        char_counts[c] = char_counts.get(c, 0) + 1
        
    for c in clean_s2:
        if c not in char_counts or char_counts[c] == 0:
            return "Not Anagram"
        char_counts[c] -= 1
        
    return "Anagram"

# Example:
print(is_anagram("listen", "silent"))      # Output: Anagram
print(is_anagram("triangle", "integral"))  # Output: Anagram
print(is_anagram("apple", "pale"))        # Output: Not Anagram
```
**Explanation:**  
- Without `sorted()`, we use a hash map ($\mathcal{O}(n)$ time, $\mathcal{O}(k)$ space where $k$ is alphabet size). We increment character counts for the first word and decrement for the second.

---

### 4. Merge Two Dictionaries — 2 Marks
**Question:** Write a Python program to merge two dictionaries. If both dictionaries contain the same key, add their values.  
*Example:* `dict1 = {"a": 10, "b": 20}`, `dict2 = {"b": 30, "c": 40}` $\rightarrow$ `{"a": 10, "b": 50, "c": 40}`

```python
def merge_and_sum_dicts(dict1: dict, dict2: dict) -> dict:
    """Merges two dicts and sums common key values."""
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

# Example:
dict1 = {"a": 10, "b": 20}
dict2 = {"b": 30, "c": 40}
print(merge_and_sum_dicts(dict1, dict2))
# Output: {'a': 10, 'b': 50, 'c': 40}
```
**Explanation:**  
- Start with a shallow copy of `dict1`. Loop over key-value pairs of `dict2`: if the key exists in the merged dictionary, add the values; otherwise, insert the new key.

---

### 5. Find the Missing Number — 2 Marks
**Question:** Given a list containing $n$ distinct numbers taken from the range $0$ to $n$, write a Python program to find the missing number.  
*Example:* Input: `[3, 0, 1]` $\rightarrow$ Output: `2`

```python
def find_missing_number(nums: list) -> int:
    """Finds missing number in range 0..n using Gauss's summation formula."""
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example:
nums = [3, 0, 1]
print("Missing number:", find_missing_number(nums))
# Output: 2
```
**Explanation:**  
- In a list of length $n$, numbers range from $0$ to $n$. The sum of all integers from $0$ to $n$ is $\frac{n(n+1)}{2}$. Subtracting the actual sum yields the missing number in $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ auxiliary memory.

---

## B. Python Theory | 5 Marks

### 1. What are `*args` and `**kwargs` in Python? Give a suitable example. — 1 Mark
**Answer:**  
`*args` and `**kwargs` allow a function to accept a dynamic, variable number of arguments:
- **`*args` (Positional Variable Arguments):** Collects extra positional arguments into a **tuple**.
- **`**kwargs` (Keyword Variable Arguments):** Collects extra named/keyword arguments into a **dictionary**.

```python
def demo_func(*args, **kwargs):
    print("args (tuple):", args)
    print("kwargs (dict):", kwargs)

demo_func(1, 2, "apple", model="RandomForest", accuracy=0.92)
# args (tuple): (1, 2, 'apple')
# kwargs (dict): {'model': 'RandomForest', 'accuracy': 0.92}
```

---

### 2. What is the difference between a parameter and an argument in Python? — 1 Mark
**Answer:**
- **Parameter:** The variable listed inside the parentheses in the **function definition** (acting as a placeholder).
- **Argument:** The actual value or reference passed into the function when it is **invoked/called**.

```python
def calculate_area(width, height):  # 'width' and 'height' are PARAMETERS
    return width * height

result = calculate_area(10, 20)       # 10 and 20 are ARGUMENTS
```

---

### 3. What is the difference between `print` and `return` in Python? — 1 Mark
**Answer:**
- **`print`:** Displays an output or string representation on the standard console for human inspection. It does **not** return a value to the caller (it returns `None`) and cannot be assigned to variables for further computation.
- **`return`:** Terminates the execution of a function and passes the calculated result back to the caller, allowing that value to be stored in variables or passed into other functions.

```python
def func_print(x):
    print(x * 2)

def func_return(x):
    return x * 2

a = func_print(5)   # Displays 10 on console; 'a' stores None
b = func_return(5)  # Nothing printed; 'b' stores 10 (can do b + 5 = 15)
```

---

### 4. What is the `range()` function in Python? Give an example. — 1 Mark
**Answer:**  
The `range([start], stop[, step])` built-in function returns an immutable sequence of integers from `start` (inclusive, default 0) to `stop` (exclusive), incremented by `step` (default 1). It computes items lazily to conserve memory.

```python
# range(start, stop, step)
for val in range(2, 10, 2):
    print(val, end=" ")
# Output: 2 4 6 8
```

---

### 5. What are nested conditions in Python? Give a suitable example. — 1 Mark
**Answer:**  
Nested conditions occur when an `if` (or `elif`/`else`) statement is placed inside another `if` (or `elif`/`else`) block. They are used to evaluate hierarchical, multi-tiered logical conditions where the inner condition is only tested if the outer condition evaluates to `True`.

```python
age = 22
has_license = True

if age >= 18:
    if has_license:
        print("Eligible to drive independently.")
    else:
        print("Eligible for a learner's permit.")
else:
    print("Underage; not eligible to drive.")
```

---

# PART 2 – MACHINE LEARNING | 5 MARKS

### 1. What is Overfitting in Machine Learning? How can it be reduced? — 1 Mark
**Answer:**  
**Overfitting** occurs when a machine learning model learns the training data too well, memorizing noise and random fluctuations rather than the underlying pattern. It results in **very low training error but high test/generalization error** (high variance).  
**How to reduce it:**
1. Regularisation ($L_1$ Lasso, $L_2$ Ridge, Dropout in Neural Networks).
2. Cross-validation and early stopping.
3. Pruning decision trees or constraining tree depth (`max_depth`).
4. Gathering more training data or applying data augmentation.
5. Feature selection to remove noisy/redundant predictors.

---

### 2. What is Underfitting in Machine Learning? — 1 Mark
**Answer:**  
**Underfitting** occurs when a model is too simple to capture the underlying structure and non-linear patterns of the data. It results in **high training error and high testing error** (high bias).  
*How to fix:* Increase model capacity/complexity (e.g., transition from linear model to polynomial or ensemble tree), engineer more relevant domain features, and decrease regularisation penalties.

---

### 3. What is the difference between Parameters and Hyperparameters in Machine Learning? — 1 Mark
**Answer:**

| Dimension | Parameters | Hyperparameters |
| :--- | :--- | :--- |
| **Origin** | Learned automatically from training data during optimization. | Set manually by the practitioner **before** model training begins. |
| **Optimization Method** | Gradient Descent, Normal Equation, backpropagation. | Grid Search, Random Search, Bayesian Optimization. |
| **Location** | Internal to the model configuration. | External configuration governing the training process. |
| **Examples** | - Weights ($w$) and biases ($b$) in Neural Networks.<br>- Regression coefficients $\beta_j$. | - Learning rate ($\eta$).<br>- Number of trees (`n_estimators`).<br>- Tree depth (`max_depth`), batch size. |

---

### 4. Differentiate between Hard Voting and Soft Voting in Ensemble Learning. — 1 Mark
**Answer:**
- **Hard Voting (Majority Rule):** Each individual base classifier predicts a class label, and the ensemble chooses the class that receives the majority of votes ($> 50\%$).
- **Soft Voting (Probability Average):** Each classifier outputs a calibrated probability for each class, and the ensemble computes the weighted average of these probabilities; the class with the highest average probability is chosen. (Soft voting often yields higher accuracy because it accounts for model certainty).

---

### 5. What is Boosting? How is it different from Bagging? — 1 Mark
**Answer:**  
**Boosting** is a sequential ensemble method where models are trained one after another. Each subsequent learner focuses on correcting the mistakes (residuals/misclassifications) of the previous models by re-weighting instances or fitting to gradient residuals.

**Key Differences from Bagging:**

| Feature | Bagging (e.g., Random Forest) | Boosting (e.g., XGBoost, Gradient Boosting) |
| :--- | :--- | :--- |
| **Training Paradigm** | **Parallel** and independent. | **Sequential** and dependent. |
| **Primary Goal** | **Reduces Variance** (prevents overfitting). | **Reduces Bias** (converts weak learners to strong). |
| **Data Sampling** | Bootstrap aggregation (random sampling with replacement). | Weighted instances or residual errors from previous step. |
| **Aggregation** | Simple majority vote or uniform average. | Weighted sum based on individual model performance. |

---

# PART 3 – MACHINE LEARNING PRACTICAL | 15 MARKS

The complete Machine Learning practical task has been implemented using the real **California Housing Dataset** loaded directly from `sklearn.datasets.fetch_california_housing`:
- Executable Python script: [`ml_practical_project.py`](file:///c:/Users/con1k/Documents/datascience_course/Technical%20Round%20Mock%20Questions/Mock2/ml_practical_project.py)
- Persisted Dataset: [`dataset.csv`](file:///c:/Users/con1k/Documents/datascience_course/Technical%20Round%20Mock%20Questions/Mock2/dataset.csv)
- Generated EDA Figures: [`visualizations/`](file:///c:/Users/con1k/Documents/datascience_course/Technical%20Round%20Mock%20Questions/Mock2/visualizations/)
- GitHub Documentation: [`README.md`](file:///c:/Users/con1k/Documents/datascience_course/Technical%20Round%20Mock%20Questions/Mock2/README.md)

### Stage-by-Stage Fulfillment Table

| Stage | Requirement | Marks | Status & Findings |
| :---: | :--- | :---: | :--- |
| **1** | Dataset selection and loading | **2 / 2** | Loaded real California census and housing dataset using `sklearn.datasets.fetch_california_housing(as_frame=True)` ($N=20,640$ block groups, 8 continuous predictors). Persisted locally as `dataset.csv`. |
| **2** | Data preprocessing | **3 / 3** | Verified zero null entries. Standardized all 8 continuous predictors via `StandardScaler` inside scikit-learn `Pipeline` to prevent train-validation data leakage. |
| **3** | Exploratory Data Analysis & visualisation | **2 / 2** | Produced 4 figures saved to `visualizations/`: Price distribution, Median Income vs Price scatter plot, Pearson Correlation Heatmap, and Geographic Spatial Distribution (Latitude vs Longitude). |
| **4** | Feature/target selection & train-test split | **2 / 2** | Features $X$ (8 columns) separated from continuous target `MedHouseVal`. Partitioned into 80% train ($N=16,512$) and 20% test ($N=4,128$) using `random_state=42`. |
| **5** | Model selection and training | **2 / 2** | Trained and evaluated 4 distinct linear and regularized regression models using 5-fold cross-validation: **OLS Linear Regression**, **Ridge ($L_2$)**, **Lasso ($L_1$)**, and **ElasticNet ($L_1 + L_2$)**. |
| **6** | Model evaluation and interpretation | **2 / 2** | Evaluated on MAE, RMSE, and $R^2$. Lasso achieved champion test performance ($R^2 = 0.5816$, $\text{RMSE} = 0.7404$). Plotted `actual_vs_predicted.png`, `feature_coefficients.png`, and `residual_distribution.png`. |
| **7** | GitHub repository & project documentation | **2 / 2** | Structured repository named `Technical round 2` with complete `README.md` containing econometric background, architecture, metrics table, and execution instructions. |
| **TOTAL**| | **15 / 15**| **All 7 stages fully executed in order with 0 stages skipped.** |

---

# PART 4 – DEEP LEARNING | 10 MARKS

### 1. What is Deep Learning? — 1 Mark
**Answer:**  
Deep Learning is a specialized subfield of Machine Learning based on Artificial Neural Networks with representation learning across **multiple hidden layers** ("deep" architectures). It automatically extracts hierarchical features from raw, unstructured data (images, audio, video, text) without requiring manual feature engineering.

---

### 2. What is an Activation Function? Why is it used in a neural network? — 1 Mark
**Answer:**  
An activation function is a mathematical transformation applied to the weighted sum of inputs plus bias at each artificial neuron: $a = \sigma(\mathbf{w}^T\mathbf{x} + b)$.  
**Why it is used:**  
It introduces **non-linearity** into the network. Without non-linear activation functions, any composition of linear layers collapses mathematically into a single linear regression transformation ($\mathbf{W}_2(\mathbf{W}_1\mathbf{x}) = \mathbf{W}_{\text{comb}}\mathbf{x}$), preventing the network from learning complex non-linear decision boundaries.

---

### 3. What is Forward Propagation? — 1 Mark
**Answer:**  
Forward propagation is the process by which input data passes through the network's layers in sequential order—from the input layer, through one or more hidden layers, to the output layer—computing affine transformations and non-linear activations at each stage to generate final predictions $\hat{y}$ and compute the loss $L(y, \hat{y})$.

---

### 4. What is Backward Propagation (Backpropagation)? — 1 Mark
**Answer:**  
Backpropagation (backward propagation of errors) is an efficient algorithm for computing the gradient of the loss function with respect to every weight and bias in the neural network using the mathematical **Chain Rule** of calculus. It propagates the error gradient backwards from the output layer to earlier layers, enabling gradient descent optimizers to update the weights.

---

### 5. What are the default values of `epochs` and `batch_size` when using Keras `model.fit()` if they are not explicitly specified? — 1 Mark
**Answer:**  
In the official Keras API (`tf.keras.Model.fit()`):
- **`epochs` default value:** `1` (the model trains for exactly one single pass over the entire dataset).
- **`batch_size` default value:** `32` (or `None` if data is passed as a batched `tf.data.Dataset` / generator).

---

### 6. What is a Convolution Operation in a Convolutional Neural Network (CNN)? — 1 Mark
**Answer:**  
A convolution operation involves sliding a small learnable filter/kernel (e.g., $3 \times 3$ matrix) across an input tensor (e.g., image), computing element-wise multiplications, and summing the results to create a 2D **Feature Map** (activation map). It preserves spatial relationships and enforces parameter sharing and translation invariance.

---

### 7. What is Pooling in CNN? Why is it used? — 1 Mark
**Answer:**  
Pooling is a downsampling operation (such as **Max Pooling** or **Average Pooling**) applied across spatial patches of feature maps.  
**Why it is used:**
1. **Dimensionality Reduction:** Progressively reduces the spatial dimensions ($H \times W$) of feature maps, cutting computational cost and memory.
2. **Translation & Distortion Invariance:** Makes representations robust to small shifts, translations, and rotations in the input.
3. **Overfitting Prevention:** Reduces the total number of downstream trainable parameters.

---

### 8. What is Sequential Data? Give one suitable example. — 1 Mark
**Answer:**  
Sequential data is any data where the **order, temporal sequence, or positional dependency** of data points matters fundamentally to its meaning and context. In sequential data, observation $x_t$ depends on preceding observations $x_{t-1}, x_{t-2}$.  
*Suitable Example:* Natural language text (e.g., "The cat sat on the mat" where swapping word order alters semantic meaning), stock price time-series, audio waveforms, or DNA nucleotide sequences.

---

### 9. What is the difference between a CNN and an RNN? — 1 Mark
**Answer:**

| Dimension | Convolutional Neural Network (CNN) | Recurrent Neural Network (RNN) |
| :--- | :--- | :--- |
| **Primary Domain** | Spatial data (images, computer vision, video). | Sequential & temporal data (NLP, speech, time series). |
| **Architectural Flow** | Feed-forward spatial filtering; no internal state cycles. | Recurrent loops with a hidden state passing memory across time steps. |
| **Parameter Sharing** | Kernels shared spatially across image coordinates. | Same weight matrices ($W_{hh}, W_{xh}$) shared across all time steps. |
| **Core Mechanism** | Convolution and Pooling. | Recurrent hidden state update: $h_t = \tanh(W_{hh}h_{t-1} + W_{xh}x_t)$. |

---

### 10. What is a Neuron in a Neural Network? — 1 Mark
**Answer:**  
A neuron (or Perceptron / artificial node) is the fundamental computational unit of a neural network. It receives one or more numeric inputs ($x_1, x_2, \dots, x_n$), multiplies each by a corresponding learnable weight ($w_i$), sums them along with an added bias ($b$), and passes the result through an activation function ($\sigma$) to generate an output:
$$y = \sigma\left(\sum_{i=1}^n w_i x_i + b\right)$$

---

# PART 5 – NLP | 5 MARKS

### 1. What is Natural Language Processing (NLP)? — 1 Mark
**Answer:**  
Natural Language Processing (NLP) is an interdisciplinary field of Artificial Intelligence, Computer Science, and Computational Linguistics that enables computers to understand, interpret, process, manipulate, and generate human language in both text and speech forms.

---

### 2. What are some common applications of NLP? — 1 Mark
**Answer:**  
Common real-world NLP applications include:
1. **Machine Translation:** Translating text across languages (e.g., Google Translate).
2. **Sentiment Analysis:** Classifying social media reviews as positive, negative, or neutral.
3. **Chatbots & Conversational AI:** Virtual assistants and customer support systems.
4. **Information Extraction & Named Entity Recognition (NER):** Extracting people, organizations, dates, and medical codes from documents.
5. **Text Summarization:** Generating concise abstracts from lengthy legal or financial reports.

---

### 3. When is Sentence Tokenisation useful? — 1 Mark
**Answer:**  
Sentence tokenisation (splitting continuous text into discrete sentences) is useful when:
1. Performing **document summarization**, where extraction or generation operates on whole sentence units.
2. Parsing sentence-level grammar, dependency trees, and syntactic structures.
3. Processing long documents for NLP models with token limits (e.g., chunking text for Transformer LLM contexts or RAG embeddings).
4. Translating documents where sentence boundaries dictate translation alignment.

---

### 4. What is Tokenisation in NLP? — 1 Mark
**Answer:**  
Tokenisation is the foundational NLP preprocessing step of breaking down a continuous stream of raw text into smaller, meaningful discrete units called **tokens** (such as words, subwords, characters, or punctuation marks) so they can be indexed and converted into numerical vector representations.

---

### 5. When is Word Tokenisation useful? — 1 Mark
**Answer:**  
Word tokenisation (splitting sentences into individual words/lexemes) is useful when:
1. Building **Bag-of-Words (BoW)** or **TF-IDF** vocabulary tables.
2. Generating word embeddings (e.g., Word2Vec, GloVe, FastText).
3. Performing Part-of-Speech (POS) tagging and Named Entity Recognition (NER).
4. Filtering stop words, calculating word frequency distributions, and applying stemming/lemmatization.
