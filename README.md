# Student Dataset Cleaning Project

## 🧼 Description

This project focuses on cleaning a student performance dataset to ensure it is ready for further analysis or machine learning tasks. It includes steps like handling missing values, correcting data inconsistencies, and feature engineering.

## 🛠️ Tech Stack

- Python
- Pandas

## ✅ Features

- Loads raw student data from CSV
- Identifies and removes missing values and duplicates
- Standardizes categorical data (e.g., Gender)
- Validates data ranges (e.g., no negative scores)
- Encodes categorical columns
- Adds a new feature: `GradeAverage`
- Saves the cleaned dataset as `cleaned_student_data.csv`


## 🚀 How to Run

1. Make sure you have Python installed.
2. Place the original `student.csv` in the same directory as the script.
3. Run the script:
    ```bash
    python "Kaggel dataset cleaning - (Tanuja Subhash Shinde).py"
    ```
4. The cleaned file will be saved as `cleaned_student_data.csv`.

## 📂 Dataset

File required: `student.csv`

Ensure this file includes columns like:
- `Gender`
- `MathScore`
- `ReadingScore`
- `WritingScore`
- `ParentEduc`

---

*Author: Tanuja Subhash Shinde*

