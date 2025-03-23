#!/usr/bin/env python3
# Author: Mikhail Ibrahim
# Date: Mar 23, 2025
# Description: A Python program that asks the user to guess a number between 1 and 9.

import random  # Import random module

# ==========================
# Test Cases:
# ==========================

# Test Case 1: Correct Guess
correct_number = 6  # Manually set for testing
test_input_1 = 6  # Simulated user input
print(f"Test Case 1 - Input: {test_input_1}")
if test_input_1 == correct_number:
    print("Expected Output: You guessed correctly!")
else:
    print(f"Expected Output: You guessed wrong. The correct number was {correct_number}")

print()  # Blank line for readability

# Test Case 2: Incorrect Guess
correct_number = 9  # Manually set for testing
test_input_2 = 3  # Simulated user input
print(f"Test Case 2 - Input: {test_input_2}")
if test_input_2 == correct_number:
    print("Expected Output: You guessed correctly!")
else:
    print(f"Expected Output: You guessed wrong. The correct number was {correct_number}")

print("\nNow, let's play the actual game!\n")

# ==========================
# Actual Game:
# ==========================

# Generate a random number for the actual game
correct_number = random.randint(1, 9)  # Generate a random number between 1 and 9 (excluding 0)

# Ask the user for their guess
user_guess = int(input("Guess a number between 1 and 9: "))

# Check if the guess is correct
if user_guess == correct_number:
    print("You guessed correctly!")

# Check if the guess is incorrect
if user_guess != correct_number:
    print(f"You guessed wrong. The correct number was {correct_number}")
