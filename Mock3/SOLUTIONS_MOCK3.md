# MAGNATE ACADEMY
## TECHNICAL ROUND 3 – DATA SCIENCE: COMPLETE SOLUTIONS

**Total Marks:** 50  
**Candidate Submission Guide & Master Answer Key**

---

# PART 1 – PYTHON | 15 MARKS

## A. Python Coding | 10 Marks

### 1. Count the Frequency of Each Character — 2 Marks
**Question:** Write a Python program to count the frequency of each character in a given string.  
*Example:* Input: `"programming"`  
*Output:* `{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}`

```python
def count_char_frequency(s: str) -> dict:
    """Counts character frequencies preserving first-occurrence order."""
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Example:
text = "programming"
print(count_char_frequency(text))
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
```
**Explanation:**  
- We iterate through the string and use a dictionary with `dict.get(char, 0) + 1`. This runs in $\mathcal{O}(n)$ time and $\mathcal{O}(k)$ space where $k$ is the distinct character count.

---

### 2. Second Largest Number — 2 Marks
**Question:** Write a Python program to find the second-largest distinct number in a given list.  
*Condition:* Do not use the built-in `sort()` or `sorted()` functions.  
*Example:* Input: `[10, 5, 8, 20, 20, 15]` $\rightarrow$ Output: `15`

```python
def find_second_largest(nums: list):
    """Finds second largest distinct value in O(n) time without sorting."""
    if len(nums) < 2:
        return None
    
    first = -float('inf')
    second = -float('inf')
    
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
            
    return second if second != -float('inf') else None

# Example:
sample = [10, 5, 8, 20, 20, 15]
print("Second largest:", find_second_largest(sample))
# Output: 15
```
**Explanation:**  
- By tracking `first` and `second` in a single pass, we ensure $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ space. The condition `num < first` prevents duplicate maximal entries from incorrectly occupying both first and second positions.

---

### 3. Remove Duplicate Elements — 2 Marks
**Question:** Write a Python program to remove duplicate elements from a list without changing their original order.  
*Condition:* Do not use the built-in `set()` function.  
*Example:* Input: `[1, 2, 3, 2, 4, 1, 5]` $\rightarrow$ Output: `[1, 2, 3, 4, 5]`

```python
def remove_duplicates_ordered(lst: list) -> list:
    """Removes duplicates while preserving order without using set()."""
    seen = {}
    for item in lst:
        seen[item] = True
    return list(seen.keys())

# Example:
data = [1, 2, 3, 2, 4, 1, 5]
print("Unique ordered elements:", remove_duplicates_ordered(data))
# Output: [1, 2, 3, 4, 5]
```
**Explanation:**  
- In Python 3.7+, standard dictionaries preserve insertion order. By inserting list elements as dictionary keys without using `set()`, duplicates are automatically eliminated while preserving original sequence in $\mathcal{O}(n)$ time.

---

### 4. Two Sum — 2 Marks
**Question:** Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.  
*Example:* Input: `nums = [2, 7, 11, 15]`, `target = 9` $\rightarrow$ Output: `[0, 1]`

```python
def two_sum(nums: list, target: int) -> list:
    """Finds indices of two numbers that sum to target in O(n) time."""
    seen_map = {}  # maps value -> index
    for index, val in enumerate(nums):
        complement = target - val
        if complement in seen_map:
            return [seen_map[complement], index]
        seen_map[val] = index
    return []

# Example:
nums = [2, 7, 11, 15]
target = 9
print("Indices:", two_sum(nums, target))
# Output: [0, 1]
```
**Explanation:**  
- We use a hash map to look up the required `complement = target - val` in $\mathcal{O}(1)$ average time per element, achieving optimal $\mathcal{O}(n)$ overall runtime instead of brute-force $\mathcal{O}(n^2)$.

---

### 5. Valid Palindrome — 2 Marks
**Question:** Given a string `s`, determine whether it is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.  
*Example 1:* `s = "A man, a plan, a canal: Panama"` $\rightarrow$ `True`  
*Example 2:* `s = "race a car"` $\rightarrow$ `False`

```python
def is_valid_palindrome(s: str) -> bool:
    """Two-pointer valid palindrome check ignoring non-alphanumeric and case."""
    left = 0
    right = len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True

# Example:
print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_valid_palindrome("race a car"))                      # False
```
**Explanation:**  
- Using two pointers moving inward from both ends avoids allocating new strings in memory, operating in $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ auxiliary space.

---

## B. Python Theory | 5 Marks

### 1. Difference between List and Tuple — 1 Mark
**Answer:**
- **List (`[]`):** A **mutable**, ordered sequence whose elements can be modified, appended, or deleted in place after creation.
  - *Example:* `my_list = [1, 2, 3]; my_list.append(4)`
- **Tuple (`()`):** An **immutable**, ordered sequence whose elements cannot be altered once created. Because of immutability, tuples are hashable (can serve as dictionary keys) and faster to iterate over.
  - *Example:* `my_tuple = (1, 2, 3); # my_tuple[0] = 10 raises TypeError`

---

### 2. Difference between Mutable and Immutable Data Types — 1 Mark
**Answer:**
- **Mutable Types:** Objects whose internal state or values can be altered in place without changing their memory address identity (`id()`).
  - *Examples:* **Lists** (`[1, 2]`), **Dictionaries** (`{'a': 1}`), **Sets** (`{1, 2}`).
- **Immutable Types:** Objects whose content cannot be changed once allocated in memory; modifying them creates a new object in a different memory location.
  - *Examples:* **Integers / Floats** (`42`, `3.14`), **Strings** (`"hello"`), **Tuples** (`(1, 2)`).

---

### 3. Exception Handling: `try`, `except`, and `finally` — 1 Mark
**Answer:**  
Exception handling allows programs to gracefully catch, manage, and recover from runtime errors without abruptly crashing.
- **`try` block:** Encloses the code that might trigger an exception.
- **`except` block:** Executes specific recovery logic if an error occurs inside the `try` block.
- **`finally` block:** Guaranteed to execute always, regardless of whether an exception occurred or was handled (used for cleanup tasks like closing database connections or files).

```python
try:
    file = open("dataset.csv", "r")
    content = file.read()
except FileNotFoundError as e:
    print("Error: Dataset file was not found!")
finally:
    print("Execution complete: Releasing system resources.")
```

---

### 4. What is List Comprehension in Python? — 1 Mark
**Answer:**  
List comprehension is a concise syntactic construct that generates a new list by transforming items from an iterable in a single readable line:  
`[<expression> for <item> in <iterable> if <condition>]`.  
*Example:*  
`squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]`

---

### 5. Lambda Function vs. Normal Function — 1 Mark
**Answer:**
- **Lambda Function:** An anonymous, inline function declared with the `lambda` keyword that contains only a single evaluated expression with implicit return. It is typically used for short, throwaway operations in functions like `map()` or `filter()`.
  - *Example:* `add = lambda a, b: a + b`
- **Normal Function:** Defined with the `def` keyword, has a formal name, can contain multiple statements, docstrings, loops, exception handling, and explicit `return` statements.
  - *Example:*
    ```python
    def add(a, b):
        """Adds two numbers."""
        return a + b
    ```

---

# PART 2 – MACHINE LEARNING | 5 MARKS

### 1. What is a Confusion Matrix? Explain TP, TN, FP, FN. — 1 Mark
**Answer:**  
A Confusion Matrix is an $N \times N$ performance evaluation table used in classification to compare actual ground truth labels against predicted class assignments.

```
                  Predicted Positive   Predicted Negative
Actual Positive          TP                   FN
Actual Negative          FP                   TN
```
- **True Positive (TP):** Model correctly predicts the positive event (e.g., diseased patient correctly diagnosed with disease).
- **True Negative (TN):** Model correctly predicts the negative event (e.g., healthy patient correctly diagnosed as healthy).
- **False Positive (FP - Type I Error):** Model incorrectly predicts positive when it is actually negative (e.g., healthy patient diagnosed as diseased).
- **False Negative (FN - Type II Error):** Model incorrectly predicts negative when it is actually positive (e.g., diseased patient diagnosed as healthy).

---

### 2. What is Gradient Descent? How does it help a model learn? — 1 Mark
**Answer:**  
Gradient Descent is an iterative optimization algorithm used to minimize a model's objective loss/cost function $J(\mathbf{w})$.  
**How it helps the model learn:**  
It computes the partial derivatives (gradients) of the loss with respect to each model parameter $\nabla_\mathbf{w} J(\mathbf{w})$, indicating the direction of steepest loss increase. By adjusting weights in the opposite direction ($\mathbf{w} \leftarrow \mathbf{w} - \eta \nabla_\mathbf{w} J(\mathbf{w})$ with learning rate $\eta$), the model iteratively reduces its prediction errors until reaching the optimal parameter configuration.

---

### 3. Difference between Classification and Regression — 1 Mark
**Answer:**
- **Classification:** Predicts a **discrete categorical class label** from a finite set of categories.
  - *Example:* Predicting whether a credit card transaction is Fraudulent or Genuine (Binary Classification).
- **Regression:** Predicts a **continuous numerical quantity** on a continuous scale.
  - *Example:* Predicting the market price of a residential house in dollars.

---

### 4. What is Feature Engineering? Why is it important? — 1 Mark
**Answer:**  
Feature engineering is the process of using domain expertise and data science techniques to extract, transform, combine, and select the most relevant variables from raw data to improve model predictive power.  
**Why it is important:**  
Machine learning algorithms can only learn from the representations fed to them. High-quality features expose the underlying signal clearly, simplifying model architecture, speeding up training, and boosting accuracy.  
*Example:* Calculating `DebtToIncomeRatio = MonthlyDebt / MonthlyIncome` in credit scoring, or extracting `HourOfDay` and `IsWeekend` from a raw timestamp.

---

### 5. What is Regularisation? Difference between L1 and L2 Regularisation. — 1 Mark
**Answer:**  
Regularisation is a technique that penalizes overly complex models by adding a penalty term to the cost function, preventing overfitting and improving out-of-sample generalization.

| Feature | L1 Regularisation (Lasso) | L2 Regularisation (Ridge) |
| :--- | :--- | :--- |
| **Penalty Term** | $\lambda \sum_{j=1}^p \|w_j\|$ (sum of absolute weights) | $\lambda \sum_{j=1}^p w_j^2$ (sum of squared weights) |
| **Sparsity** | Drives unimportant coefficients strictly to **zero**. | Shrinks coefficients **close to zero**, but never zero. |
| **Feature Selection** | Performs **automatic feature selection**. | Retains all features; handles multicollinearity. |
| **Geometry** | Diamond-shaped constraint with sharp corners on axes. | Circular/Spherical smooth constraint surface. |

---

# PART 3 – MACHINE LEARNING PRACTICAL | 15 MARKS

The complete Machine Learning practical task has been implemented using the real **Wine Recognition Dataset** loaded directly from `sklearn.datasets.load_wine`:
- Executable Python script: [`ml_practical_project.py`](file:///c:/Users/con1k/Documents/datascience_course/Technical%20Round%20Mock%20Questions/Mock3/ml_practical_project.py)
- Persisted Dataset: [`dataset.csv`](file:///c:/Users/con1k/Documents/datascience_course/Technical%20Round%20Mock%20Questions/Mock3/dataset.csv)
- Generated EDA Figures: [`visualizations/`](file:///c:/Users/con1k/Documents/datascience_course/Technical%20Round%20Mock%20Questions/Mock3/visualizations/)
- GitHub Documentation: [`README.md`](file:///c:/Users/con1k/Documents/datascience_course/Technical%20Round%20Mock%20Questions/Mock3/README.md)

### Stage-by-Stage Fulfillment Table

| Stage | Requirement | Marks | Status & Findings |
| :---: | :--- | :---: | :--- |
| **1** | Dataset selection and loading | **2 / 2** | Loaded real chemical wine dataset using `sklearn.datasets.load_wine(as_frame=True)` ($N=178$ wine samples, 13 chemical constituents, 3 cultivar target classes). Persisted locally as `dataset.csv`. |
| **2** | Data preprocessing | **3 / 3** | Inspected missing values ($0$ nulls). Standardized all 13 continuous chemical predictors via `StandardScaler` inside scikit-learn `Pipeline` to prevent train-test data leakage. |
| **3** | Exploratory Data Analysis & visualisation | **2 / 2** | Produced 4 figures in `visualizations/`: Cultivar class frequencies, Alcohol vs Flavanoids scatter plot, Pearson Correlation Heatmap, and Proline concentration box plot across cultivars. |
| **4** | Feature/target selection & train-test split | **2 / 2** | Isolated 13 chemical features against multi-class `target` variable. Performed stratified 80/20 train-test split ($N_{\text{train}}=142$, $N_{\text{test}}=36$) with `random_state=42`. |
| **5** | Model selection and training | **2 / 2** | Trained and evaluated 4 distinct tree and ensemble classifiers using 5-fold cross-validation: **Decision Tree**, **Random Forest**, **Gradient Boosting**, and **Extra Trees**. |
| **6** | Model evaluation and interpretation | **2 / 2** | Assessed on Accuracy, Weighted Precision, Recall, and F1-Score. Champion models: **Random Forest** and **Extra Trees** achieved **$100\%$ test accuracy** and **$1.0000$ Weighted F1**. Plotted multi-class confusion matrix and Gini feature importance rankings. |
| **7** | GitHub repository & project documentation | **2 / 2** | Documented under repository name `Technical round 3` with comprehensive `README.md` containing chemical background, flowcharts, metric tables, and run commands. |
| **TOTAL**| | **15 / 15**| **All 7 stages fully executed in order with 0 stages skipped.** |

---

# PART 4 – DEEP LEARNING | 5 MARKS

### 1. What is the Vanishing Gradient Problem? How can it be addressed? — 1 Mark
**Answer:**  
The **Vanishing Gradient Problem** occurs in deep neural networks during backpropagation when error gradients are multiplied across many layers using the chain rule. When using activation functions like Sigmoid or Tanh whose derivatives are bounded ($< 0.25$), gradients shrink exponentially towards zero as they propagate back to early layers, preventing early layers from updating their weights.  
**How it is addressed:**
1. Using non-saturating activation functions like **ReLU**, Leaky ReLU, or ELU.
2. Implementing **Residual Connections (Skip Connections)** as in ResNets.
3. Proper weight initialization (e.g., He / Kaiming or Xavier / Glorot initialization).
4. Applying **Batch Normalization** or Layer Normalization across intermediate layers.

---

### 2. Difference between Sigmoid, Tanh, and ReLU Activation Functions — 1 Mark
**Answer:**

| Activation Function | Mathematical Formula | Output Range | Key Characteristics |
| :--- | :--- | :--- | :--- |
| **Sigmoid** | $\sigma(z) = \frac{1}{1 + e^{-z}}$ | $(0, 1)$ | Smooth S-curve; outputs valid probabilities; suffers heavily from vanishing gradients; not zero-centered. |
| **Tanh** | $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$ | $(-1, 1)$ | Zero-centered; stronger gradients than Sigmoid; still saturates at extreme values. |
| **ReLU** | $f(z) = \max(0, z)$ | $[0, \infty)$ | Non-saturating for positive inputs; computationally efficient (no exponentials); standard default for deep hidden layers; subject to "Dying ReLU". |

---

### 3. Difference between Epoch, Batch, and Iteration — 1 Mark
**Answer:**
- **Epoch:** One complete pass through the **entire training dataset** by the neural network during training.
- **Batch:** A subset of the training dataset processed simultaneously in one step (batch size is the number of samples in that subset, e.g., 32 or 64).
- **Iteration (Step):** A single parameter update step using one batch.  
  $$\text{Iterations per Epoch} = \left\lceil \frac{\text{Total Training Samples}}{\text{Batch Size}} \right\rceil$$

---

### 4. What is an Optimiser? Explain the role of SGD and Adam. — 1 Mark
**Answer:**  
An optimizer is an algorithm that calculates how model parameters (weights and biases) should change based on the computed loss gradient to minimize training loss.
- **SGD (Stochastic Gradient Descent):** Updates parameters using a single random sample or mini-batch per step. It provides unbiased gradient estimates with high variance, which helps escape saddle points, but can oscillate in steep ravines.
- **Adam (Adaptive Moment Estimation):** Combines the advantages of **Momentum** (exponentially decaying average of past gradients, first moment) and **RMSprop** (exponentially decaying average of past squared gradients, second moment) to adaptively adjust learning rates for each parameter individually, offering fast convergence and robust performance across diverse architectures.

---

### 5. Default Values of `epochs` and `batch_size` in Keras `model.fit()` — 1 Mark
**Answer:**  
In the official Keras specification (`tf.keras.Model.fit()`):
- **Default `epochs`:** `1`
- **Default `batch_size`:** `32`

---

# PART 5 – NLP | 5 MARKS

### 1. Difference between Stemming and Lemmatization — 1 Mark
**Answer:**
- **Stemming:** A crude, heuristic rule-based process that chops off suffixes and prefixes from words without understanding grammar or dictionary context. Often produces non-dictionary pseudo-words.
  - *Example:* `"studies"`, `"studying"` $\rightarrow$ `"studi"`.
- **Lemmatization:** A linguistically informed morphological analysis that uses a vocabulary and morphological rules to reduce a word to its true dictionary canonical base form (lemma) based on its Part-of-Speech (POS) tag.
  - *Example:* `"better"` $\rightarrow$ `"good"`; `"studies"` $\rightarrow$ `"study"`.

---

### 2. Difference between Bag of Words (BoW) and TF-IDF — 1 Mark
**Answer:**
- **Bag of Words (BoW):** Represents a document as a sparse vector of raw token frequencies (counts) across the global vocabulary, completely ignoring word order, grammar, and semantic significance across documents.
- **TF-IDF (Term Frequency-Inverse Document Frequency):** Weights each word's frequency ($\text{TF}$) by how rare/informative it is across the entire corpus ($\text{IDF} = \log(N / \text{DF})$). Frequent common words (e.g., "the", "is") receive low weights, while distinctive domain keywords receive high weights.

---

### 3. What are Stop Words? Why are they removed? — 1 Mark
**Answer:**  
Stop words are high-frequency, non-distinctive grammatical words in a language (such as `"the"`, `"is"`, `"at"`, `"which"`, `"on"`) that convey minimal domain-specific semantic meaning.  
**Why they are removed:**  
1. Reduces vocabulary size and matrix dimensionality, conserving memory and computing power.
2. Prevents non-informative function words from dominating statistical frequency metrics (like BoW or search index frequencies).

---

### 4. What are Word Embeddings? How does Word2Vec represent words? — 1 Mark
**Answer:**  
Word embeddings are dense, continuous, low-dimensional numerical vectors (e.g., $\mathbb{R}^{300}$) representing words, where semantically similar words are mapped to proximate points in vector space.  
**How Word2Vec represents words:**  
Word2Vec trains a shallow 2-layer neural network using the Distributional Hypothesis ("a word is characterized by the company it keeps"). It employs either:
1. **Continuous Bag of Words (CBOW):** Predicts the target word given its surrounding context words.
2. **Skip-gram:** Predicts the surrounding context words given a single target word.  
The learned hidden-layer weight matrix serves as the word embedding lookup table, capturing geometric semantic relationships (e.g., $\vec{v}_{\text{King}} - \vec{v}_{\text{Man}} + \vec{v}_{\text{Woman}} \approx \vec{v}_{\text{Queen}}$).

---

### 5. Difference between Unigrams, Bigrams, and Trigrams — 1 Mark
**Answer:**  
An $N$-gram is a contiguous sequence of $N$ tokens extracted from a given text window:
- **Unigram ($N=1$):** Single isolated words.
  - *Example:* `"Machine learning is powerful"` $\rightarrow$ `["Machine", "learning", "is", "powerful"]`
- **Bigram ($N=2$):** Two-word pairs capturing immediate sequential context.
  - *Example:* `["Machine learning", "learning is", "is powerful"]`
- **Trigram ($N=3$):** Three-word triplets capturing broader phrase patterns.
  - *Example:* `["Machine learning is", "learning is powerful"]`

---

# PART 6 – GEN AI | 5 MARKS

### 1. What is Generative AI? How is it different from Traditional AI? — 1 Mark
**Answer:**  
**Generative AI** is a branch of Artificial Intelligence powered by foundation models (such as Transformers, Diffusion Models, and VAEs) that can **create novel, realistic content** (text, synthetic images, audio, code, 3D assets) by learning the underlying joint probability distribution $P(X)$.  
**Difference from Traditional AI:**  
- **Traditional (Discriminative/Analytical) AI:** Focuses on analyzing existing data to classify, predict, or cluster (e.g., deciding if an email is spam, predicting house prices, optimizing routes). It learns $P(Y|X)$.
- **Generative AI:** Generates brand-new synthetic data instances that mirror the training distribution.

---

### 2. What is a Large Language Model (LLM)? Give examples. — 1 Mark
**Answer:**  
A Large Language Model (LLM) is a deep learning model based on the Transformer architecture (typically billions to trillions of parameters) trained on massive web-scale textual corpora using self-supervised autoregressive next-token prediction. It demonstrates emergent capabilities in reasoning, coding, translation, and natural language understanding.  
*Examples:*  
- **Gemini** (Google DeepMind)
- **GPT-4 / GPT-4o** (OpenAI)
- **Claude 3.5 Sonnet** (Anthropic)
- **Llama 3** (Meta)

---

### 3. What is Retrieval-Augmented Generation (RAG)? Why is it used? — 1 Mark
**Answer:**  
Retrieval-Augmented Generation (RAG) is an architectural framework that enhances an LLM's prompt by dynamically retrieving relevant document chunks from an external factual knowledge base (e.g., vector database) and passing them as context during inference.  
**Why it is used:**
1. **Eliminates Hallucinations:** Grounds model answers in verified source facts.
2. **Access to Proprietary & Private Data:** Enables querying internal corporate data without expensive model pre-training.
3. **Overcomes Training Cutoff Dates:** Keeps knowledge up-to-date in real time simply by updating the vector database.
4. **Auditability:** Provides source citations for every claim.

---

### 4. What is Metadata in Generative AI? Why is it important in RAG? — 1 Mark
**Answer:**  
Metadata refers to auxiliary contextual attributes attached to stored document chunks (e.g., document title, creation date, source URL, author, security access tier, department, category).  
**Why it is important in RAG:**
1. **Filtered Vector Search (Hybrid Search):** Enables pre-filtering or post-filtering searches (e.g., "Search only documents created in 2026 under 'Engineering'").
2. **Access Control & Security:** Restricts information retrieval based on user role and permissions.
3. **Recency Weighting:** Allows boosting newer policy documents over outdated versions.
4. **Accurate Attribution:** Powers automated citation generation.

---

### 5. What is Source Tracking and Citation in Generative AI? — 1 Mark
**Answer:**  
Source tracking and citation is the mechanism by which a Generative AI application tracks the exact external reference documents, paragraphs, and page numbers retrieved during query execution and explicitly cites them in the generated response (e.g., "[Source: Q3_Financial_Report.pdf, Page 14]").  
**Importance:**  
It provides transparency, establishes user trust, enables human fact-checking, prevents intellectual property ambiguity, and meets enterprise compliance standards.
