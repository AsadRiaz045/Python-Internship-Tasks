# 🐍 Python Internship Tasks

This repository contains my daily tasks and solutions during my Python Internship.

---

## 📅 Day 1: Python Basics, Data Structures & OOP

On the first day of my internship, I covered fundamental Python concepts along with Object-Oriented Programming (OOP) and Error Handling.

### 🚀 Key Concepts Covered:
- **Core Python:** Loops (`for`, `range`) and Math functions.
- **Data Structures:** Working with `Sets` and `Dictionaries`.
- **OOP:** Classes, Inheritance, and Method Overriding.
- **File Handling:** Reading files and handling errors with `try-except`.

### ✅ Tasks Completed:

1.  **Area of Circle:** Calculated area using user input radius and `math.pi`.
2.  **Reverse Loop:** Printed numbers from 20 down to 1 using a `for` loop.
3.  **Prime Checker:** Created a function `is_prime(n)` to check for prime numbers.
4.  **Unique Words:** Used a **Set** to find unique words in a string.
5.  **File Reader:** Read a text file (`poem.txt`) to count lines.
6.  **Phonebook Dict:** Built a dictionary for contact storage.
7.  **OOP (Inheritance):**
    - Created a base class `Animal` and derived class `Dog`.
    - Used **Method Overriding** for the `speak()` function.
8.  **Error Handling:** Used `try-except` to handle "File not found" errors safely.

---
## 📅 Day 2: Logic Building & Algorithms
**Focus:** Strengthening logic through 20 algorithmic problems involving Lists, Strings, Recursion, and Math.

### ✅ Problems Solved:
1.  **Variable Swap:** Swapping values without a third variable.
2.  **Even Numbers:** Filtering even numbers from a list.
3.  **String Reversal:** Reversing a user input string.
4.  **Prime Validator:** Function to check if a number is prime.
5.  **Character Count:** Counting specific character occurrences.
6.  **Factorial:** Using **Recursion** to find factorial.
7.  **Palindrome:** Checking if a number is a palindrome.
8.  **Find Max:** Finding the largest number in a list.
9.  **Remove Duplicates:** Removing duplicates while keeping order.
10. **Most Frequent:** Finding the most frequent element.
11. **Word Counter:** Counting words in a sentence.
12. **Temperature:** Converting Celsius to Fahrenheit.
13. **Perfect Square:** Logic to check perfect squares.
14. **Common Elements:** Finding intersection of two lists.
15. **Sorting:** Sorting a list of strings alphabetically.
16. **Fibonacci:** Generating Fibonacci series up to `n`.
17. **Digit Sum:** Calculating the sum of digits of a number.
18. **File Line Count:** Reading a file to count lines.
19. **GCD:** Finding Greatest Common Divisor of two numbers.
20. **Merge Lists:** Merging two sorted lists.

---
## Day 03: Data Analysis & Visualization (Pandas & Matplotlib) 🐼📊

In this session, I performed extensive data manipulation using **Pandas** and created visualizations using **Matplotlib/Seaborn**. The tasks involved processing a Products Dataset.

### 🔹 Key Learnings & Operations:
* **Data Handling:**
    * Converted Dictionary to DataFrame & saved as **CSV**.
    * Loaded data and performed Data Inspection (Shape, Dtypes, Info, Describe).
    * Checked for Missing Values (`isnull`).

* **Data Transformation:**
    * **Sorting:** Sorted rows by rating (Ascending/Descending).
    * **Columns:** Renamed columns (`image` -> `img_path`), Dropped columns, and created new ones (`rating_squared`, `is_low_rated`).
    * **Indexing:** Reset index and Set `pid` as the official index.

* **CRUD Operations:**
    * **Update:** Created functions to update product ratings and save changes.
    * **Delete:** Removed specific products by index.

* **Advanced Selection:**
    * Used **`.loc`** and **`.iloc`** for specific row/column slicing.
    * Filtered data (e.g., Products with Rating < 2 or Price < 100).
    * Generated random prices (80-1200) for analysis.

### 📈 Visualizations Created:
1.  **Histogram:** Rating distribution (bins=8) with mean line.
2.  **Count Plot:** Frequency of specific ratings.
3.  **Horizontal Bar Chart:** Product vs. Rating comparison.
4.  **Box Plot:** To analyze the spread of ratings.
