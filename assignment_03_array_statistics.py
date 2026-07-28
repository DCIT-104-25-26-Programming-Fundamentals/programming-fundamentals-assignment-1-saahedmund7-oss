# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

def average(nums):
    total = sum(nums)
    return total / len(nums) if nums else 0

def maximum(nums):
    max_val = nums[0] if nums else None
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val

def minimum(nums):
    min_val = nums[0] if nums else None
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val

#main program to get user input and calculate statistics
try:
    n = int(input("How many numbers? "))
    if n <= 0:
        print("Error: Please enter a positive integer.")
    else:
        numbers = []
        for i in range(n):
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)

        print("\nResults:")
        print(f"Sum:     {sum(numbers)}")
        print(f"Average: {average(numbers)}")
        print(f"Maximum: {maximum(numbers)}")
        print(f"Minimum: {minimum(numbers)}")
except ValueError:
    print("Error detected: Please check the  numbers.")