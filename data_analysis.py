# Week-3 Client Project
# Data Cleaning and Aggregation using NumPy and Pandas

import numpy as np
import pandas as pd

print("===== Week 3: Data Cleaning & Aggregation =====")

# Sample dataset
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [85, 90, None, 78, 92]
}

df = pd.DataFrame(data)

print("\nOriginal Data:")
print(df)

# Step 1: Remove missing values
cleaned_df = df.dropna()

print("\nCleaned Data (After Removing Missing Values):")
print(cleaned_df)

# Step 2: Calculate average marks
average_marks = cleaned_df["Marks"].mean()

print("\nAverage Marks:", round(average_marks, 2))

# Step 3: NumPy operation
marks_array = np.array(cleaned_df["Marks"])
print("\nNumPy Array of Marks:", marks_array)
print("Maximum Marks:", np.max(marks_array))
print("Minimum Marks:", np.min(marks_array))
