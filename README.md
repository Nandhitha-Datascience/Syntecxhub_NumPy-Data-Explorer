# 📊 NumPy Data Analysis Project

## Overview
This project demonstrates data analysis using NumPy by creating a synthetic dataset and performing various operations such as indexing, slicing, mathematical computations, statistical analysis, reshaping, broadcasting, and performance comparison.

## Tools & Technologies
- Python
- NumPy
## Dataset
A synthetic dataset was generated using NumPy with the following columns:
- Age
- Salary
- Experience

Dataset size: 50 records

## Operations Performed

### 1.Array Creation
- Generated random dataset using NumPy
- Combined multiple arrays into a structured dataset

### 2.Access-Based Operations (Indexing & Slicing)
- Accessed individual elements using indexing
- Extracted subsets using slicing
- Selected specific columns such as salary and age

### 3.Mathematical Operations
- Increased salary by 10%
- Added bonus to salary
- Applied element-wise operations using broadcasting

### 4.Statistical Operations
- Calculated sum, mean, minimum, maximum
- Computed standard deviation of salary
- Performed column-wise analysis

### 5.Axis-Based Operations
- Column-wise operations using axis=0
- Row-wise operations using axis=1

### 6.Reshaping
- Reshaped dataset into different dimensions
- Converted 2D array into 1D array

### 7.Broadcasting
- Applied operations across arrays of different shapes efficiently

### 8.Save and Load Operations
- Saved NumPy array using .npy format
- Loaded the saved array for reuse

### 9.Performance Comparison
- Compared execution time between:
  - Python lists
  - NumPy arrays

## Key Insights
- NumPy operations are significantly faster than Python lists for large datasets
- Broadcasting allows efficient element-wise operations without loops
- Column-wise statistical operations provide meaningful insights

## Conclusion
This project demonstrates the efficiency and power of NumPy for numerical computations, data manipulation, and performance optimization compared to standard Python approaches.
