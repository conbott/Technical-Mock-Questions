"""
Magnate Academy - Technical Round 3: Data Science
Part 1: Python Coding Solutions (Q1 - Q5)
"""

import re

# ==============================================================================
# Question 1: Count Frequency of Each Character (2 Marks)
# Write a Python program to count the frequency of each character in a given string.
# Example: Input: "programming"
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
# ==============================================================================
def count_char_frequency(s: str) -> dict:
    """
    Counts the frequency of each character in the input string.
    Maintains insertion order (dict in Python 3.7+).
    """
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq


# ==============================================================================
# Question 2: Second Largest Number (2 Marks)
# Write a Python program to find the second-largest distinct number in a given list.
# Example: Input: [10, 5, 8, 20, 20, 15] -> Output: 15
# Condition: Do not use the built-in sort() or sorted() functions.
# ==============================================================================
def find_second_largest(nums: list):
    """
    Finds the second-largest distinct number in O(n) time WITHOUT using sort() or sorted().
    Handles duplicate maximal numbers (e.g. [20, 20, 15] returns 15).
    """
    if len(nums) < 2:
        return None
    
    first = -float('inf')
    second = -float('inf')
    
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            # Strictly smaller than first, but larger than current second
            second = num
            
    return second if second != -float('inf') else None


# ==============================================================================
# Question 3: Remove Duplicate Elements (2 Marks)
# Write a Python program to remove duplicate elements from a list without changing
# their original order.
# Example: Input: [1, 2, 3, 2, 4, 1, 5] -> Output: [1, 2, 3, 4, 5]
# Condition: Do not use the built-in set() function.
# ==============================================================================
def remove_duplicates_ordered(lst: list) -> list:
    """
    Removes duplicates while preserving original element order WITHOUT using set().
    Uses a dictionary keys tracking approach (or tracking list).
    """
    seen_dict = {}
    for item in lst:
        seen_dict[item] = True
    return list(seen_dict.keys())


# ==============================================================================
# Question 4: Two Sum (2 Marks)
# Given an array of integers nums and an integer target, return the indices of
# the two numbers such that they add up to the target.
# Example: Input: nums = [2, 7, 11, 15], target = 9 -> Output: [0, 1]
# ==============================================================================
def two_sum(nums: list, target: int) -> list:
    """
    Finds two indices such that nums[i] + nums[j] == target in O(n) time
    using a hash map of complements.
    """
    visited = {}  # maps value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in visited:
            return [visited[complement], i]
        visited[num] = i
    return []


# ==============================================================================
# Question 5: Valid Palindrome (2 Marks)
# Given a string s, determine whether it is a palindrome after converting all
# uppercase letters to lowercase and removing all non-alphanumeric characters.
# Example 1: "A man, a plan, a canal: Panama" -> True
# Example 2: "race a car" -> False
# ==============================================================================
def is_valid_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome considering only alphanumeric characters
    and ignoring casing.
    Two-pointer approach runs in O(n) time and O(1) extra space.
    """
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


# ==============================================================================
# Main Verification Execution
# ==============================================================================
if __name__ == "__main__":
    print("==================================================")
    print("TECHNICAL ROUND 3 - PYTHON CODING SOLUTIONS")
    print("==================================================\n")

    # Test Q1: Character Frequency
    print("Q1: Count Character Frequency")
    text_q1 = "programming"
    freq_res = count_char_frequency(text_q1)
    print(f"Input: '{text_q1}'")
    print(f"Output: {freq_res}\n")

    # Test Q2: Second Largest Number (Without sort)
    print("Q2: Second Largest Distinct Number (No sort)")
    q2_inputs = [
        [10, 5, 8, 20, 20, 15],
        [5, 5, 5],
        [-10, -5, -20, -1]
    ]
    for inp in q2_inputs:
        print(f"Input: {inp} -> Second Largest: {find_second_largest(inp)}")
    print()

    # Test Q3: Remove Duplicates (No set)
    print("Q3: Remove Duplicates Preserving Order (No set)")
    q3_input = [1, 2, 3, 2, 4, 1, 5]
    print(f"Input:  {q3_input}")
    print(f"Output: {remove_duplicates_ordered(q3_input)}\n")

    # Test Q4: Two Sum
    print("Q4: Two Sum")
    nums_q4 = [2, 7, 11, 15]
    target_q4 = 9
    result_q4 = two_sum(nums_q4, target_q4)
    print(f"nums = {nums_q4}, target = {target_q4} -> Indices: {result_q4}")
    print(f"Verification: nums[{result_q4[0]}] + nums[{result_q4[1]}] = {nums_q4[result_q4[0]] + nums_q4[result_q4[1]]}\n")

    # Test Q5: Valid Palindrome
    print("Q5: Valid Palindrome")
    test_palindromes = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "tab a bat"
    ]
    for s in test_palindromes:
        print(f"'{s}' -> Is Palindrome: {is_valid_palindrome(s)}")
