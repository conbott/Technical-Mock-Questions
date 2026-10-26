"""
Magnate Academy - Technical Round 1: Data Science
Part 1: Python Coding Solutions (Q1 - Q5)
"""

# ==============================================================================
# Question 1: Fibonacci Sequence (2 Marks)
# Write a Python program to generate the Fibonacci sequence up to n terms.
# ==============================================================================
def generate_fibonacci(n: int) -> list:
    """
    Generates the Fibonacci sequence up to n terms.
    The sequence starts with 0, 1, 1, 2, 3, 5, 8, ...
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


# ==============================================================================
# Question 2: String Manipulation (2 Marks)
# Write a Python program to capitalise the first and last character of every word
# in a given string.
# Example: "hello a world" -> "HellO A WorlD"
# ==============================================================================
def capitalize_first_and_last(s: str) -> str:
    """
    Capitalises the first and last character of each word in the input string.
    Single-character words are simply converted to uppercase.
    Preserves word spacing.
    """
    words = s.split(' ')
    result_words = []
    
    for word in words:
        if not word:
            result_words.append(word)
        elif len(word) == 1:
            result_words.append(word.upper())
        else:
            # Capitalise first character, keep middle unchanged, capitalise last character
            new_word = word[0].upper() + word[1:-1] + word[-1].upper()
            result_words.append(new_word)
            
    return ' '.join(result_words)


# ==============================================================================
# Question 3: Loop with else (2 Marks)
# Write a Python program using a for or while loop with else, without using an if statement.
# ==============================================================================
def loop_with_else_demo():
    """
    Demonstrates for...else and while...else loops without using ANY if statement.
    In Python, the 'else' block executes when the loop finishes iterating naturally
    (i.e., not interrupted by a break statement).
    """
    print("--- 3A. while...else without if ---")
    count = 1
    while count <= 5:
        print(f"Iteration: {count}")
        count += 1
    else:
        print("Loop completed successfully! Condition 'count <= 5' is now False.\n")

    print("--- 3B. for...else without if ---")
    items = ["Data Collection", "Data Preprocessing", "Model Training", "Model Evaluation"]
    for step_num, step_name in enumerate(items, 1):
        print(f"Step {step_num}: {step_name}")
    else:
        print("All pipeline steps processed successfully via for...else!\n")


# ==============================================================================
# Question 4: Prime Number (2 Marks)
# Write a Python program to determine whether a given number is prime or not.
# ==============================================================================
def is_prime(num: int) -> bool:
    """
    Determines if a given number is prime.
    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.
    Uses O(sqrt(n)) time complexity.
    """
    if num <= 1:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    # Check potential factors of form 6k +/- 1 up to sqrt(num)
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
        
    return True


# ==============================================================================
# Question 5: Longest Word (2 Marks)
# Write a Python program to find the longest word in a given string.
# ==============================================================================
import re

def find_longest_word(text: str) -> str:
    """
    Finds and returns the longest word in a given string,
    stripping punctuation so that tokens like 'world!' are treated as 'world'.
    """
    # Extract words containing alphabetic/alphanumeric characters
    words = re.findall(r'\b[A-Za-z0-9\'-]+\b', text)
    if not words:
        return ""
    
    # Use max with key=len (or manual loop)
    longest = max(words, key=len)
    return longest


# ==============================================================================
# Main Execution / Test Verification
# ==============================================================================
if __name__ == "__main__":
    print("==================================================")
    print("TECHNICAL ROUND 1 - PYTHON CODING SOLUTIONS")
    print("==================================================\n")
    
    # Test Q1: Fibonacci
    print("Q1: Fibonacci Sequence")
    for n in [0, 1, 5, 10]:
        print(f"n = {n} -> {generate_fibonacci(n)}")
    print()

    # Test Q2: String Manipulation
    print("Q2: String Manipulation")
    sample_q2 = "hello a world"
    print(f"Input:  '{sample_q2}'")
    print(f"Output: '{capitalize_first_and_last(sample_q2)}'")
    sample_q2_extra = "python machine learning data science"
    print(f"Input:  '{sample_q2_extra}'")
    print(f"Output: '{capitalize_first_and_last(sample_q2_extra)}'")
    print()

    # Test Q3: Loop with else (No IF)
    print("Q3: Loop with else without if statement")
    loop_with_else_demo()

    # Test Q4: Prime Number
    print("Q4: Prime Number Verification")
    test_numbers = [-5, 0, 1, 2, 3, 4, 17, 25, 29, 97, 100]
    for num in test_numbers:
        print(f"Number {num:3d} -> Is Prime: {is_prime(num)}")
    print()

    # Test Q5: Longest Word
    print("Q5: Longest Word")
    sample_q5 = "Data Science and Artificial Intelligence are revolutionizing modern industries."
    print(f"Input sentence: '{sample_q5}'")
    print(f"Longest word:   '{find_longest_word(sample_q5)}'")
