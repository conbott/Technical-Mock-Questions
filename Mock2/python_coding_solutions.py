"""
Magnate Academy - Technical Round 2: Data Science
Part 1: Python Coding Solutions (Q1 - Q5)
"""

# ==============================================================================
# Question 1: Largest and Smallest Number (2 Marks)
# Write a Python program to find the largest and smallest numbers in a given list.
# ==============================================================================
def find_largest_and_smallest(numbers: list):
    """
    Finds the largest and smallest numbers in a given list in O(n) time.
    Handles empty lists gracefully.
    """
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


# ==============================================================================
# Question 2: First Non-Repeating Character (2 Marks)
# Write a Python program to find the first non-repeating character in a string.
# Example: Input: "aabbcdde" -> Output: "c"
# ==============================================================================
def first_non_repeating_char(s: str):
    """
    Finds the first non-repeating character in a given string.
    Returns the character if found, or None if all characters repeat.
    Runs in O(n) time using character frequency mapping.
    """
    freq = {}
    # Count frequency of each character
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        
    # Find first character with count == 1
    for char in s:
        if freq[char] == 1:
            return char
            
    return None


# ==============================================================================
# Question 3: Anagram Check (2 Marks)
# Write a Python program to check whether two strings are anagrams of each other.
# Condition: Do not use the built-in sorted() function.
# Example: Input: "listen", "silent" -> Output: Anagram
# ==============================================================================
def is_anagram(s1: str, s2: str) -> str:
    """
    Checks if two strings are anagrams WITHOUT using sorted().
    Uses hash map (dictionary) frequency counting.
    Ignores whitespace and case differences.
    """
    clean_s1 = s1.replace(" ", "").lower()
    clean_s2 = s2.replace(" ", "").lower()
    
    if len(clean_s1) != len(clean_s2):
        return "Not Anagram"
    
    counts = {}
    for char in clean_s1:
        counts[char] = counts.get(char, 0) + 1
        
    for char in clean_s2:
        if char not in counts or counts[char] == 0:
            return "Not Anagram"
        counts[char] -= 1
        
    return "Anagram"


# ==============================================================================
# Question 4: Merge Two Dictionaries (2 Marks)
# Write a Python program to merge two dictionaries.
# If both dictionaries contain the same key, add their values.
# Example:
#   dict1 = {"a": 10, "b": 20}
#   dict2 = {"b": 30, "c": 40}
#   Expected: {"a": 10, "b": 50, "c": 40}
# ==============================================================================
def merge_and_sum_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Merges two dictionaries. If a key is present in both, their numeric
    values are summed.
    """
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged


# ==============================================================================
# Question 5: Find the Missing Number (2 Marks)
# Given a list containing n distinct numbers taken from the range 0 to n,
# write a Python program to find the missing number.
# Example:
#   Input: [3, 0, 1]
#   Output: 2
# ==============================================================================
def find_missing_number(nums: list) -> int:
    """
    Finds the missing number from 0 to n using Gauss's summation formula.
    Sum of 0 to n = n * (n + 1) // 2.
    Time Complexity: O(n), Space Complexity: O(1).
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


# ==============================================================================
# Main Verification Execution
# ==============================================================================
if __name__ == "__main__":
    print("==================================================")
    print("TECHNICAL ROUND 2 - PYTHON CODING SOLUTIONS")
    print("==================================================\n")

    # Test Q1: Largest and Smallest
    print("Q1: Largest and Smallest Number")
    test_list = [42, 17, 88, 3, 55, 99, 12, -4]
    max_val, min_val = find_largest_and_smallest(test_list)
    print(f"List: {test_list}")
    print(f"Largest: {max_val}, Smallest: {min_val}\n")

    # Test Q2: First Non-Repeating Character
    print("Q2: First Non-Repeating Character")
    q2_input = "aabbcdde"
    print(f"Input:  '{q2_input}'")
    print(f"Output: '{first_non_repeating_char(q2_input)}'\n")

    # Test Q3: Anagram Check (Without sorted())
    print("Q3: Anagram Check without sorted()")
    pairs = [
        ("listen", "silent"),
        ("Triangle", "Integral"),
        ("hello", "world"),
        ("apple", "pale")
    ]
    for s1, s2 in pairs:
        print(f"'{s1}' & '{s2}' -> {is_anagram(s1, s2)}")
    print()

    # Test Q4: Merge Two Dictionaries
    print("Q4: Merge Two Dictionaries with Summed Overlaps")
    d1 = {"a": 10, "b": 20}
    d2 = {"b": 30, "c": 40}
    print(f"dict1: {d1}")
    print(f"dict2: {d2}")
    print(f"Merged Result: {merge_and_sum_dicts(d1, d2)}\n")

    # Test Q5: Find the Missing Number
    print("Q5: Find the Missing Number in range [0, n]")
    missing_samples = [
        [3, 0, 1],
        [0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1]
    ]
    for sample in missing_samples:
        print(f"Input: {sample} -> Missing Number: {find_missing_number(sample)}")
