# Author : Engr. Muhammad Javed


import pandas as pd
import numpy as np



data = pd.read_csv("sales_data_sample.csv" , encoding = 'latin1')
# print(data)



# 1. data.head()
# ➤ Displays the first 5 rows of the DataFrame.
# ➤ Useful for quickly checking the structure and sample data.
print("1. Head (First 5 Rows):")
print(data.head(5))



# 2. data.tail()
# ➤ Displays the last 5 rows of the DataFrame.
# ➤ Helpful for checking the ending records in the dataset.
print("\n2. Tail (Last 5 Rows):")
print(data.tail(5))




# 3. data.shape
# ➤ Returns a tuple with (number of rows, number of columns).
# ➤ Tells us the overall size of the dataset.
print("\n3. Shape (Number of Rows and Columns):")
print(data.shape)




# 4. data.sample(5)
# ➤ Returns 5 random rows from the dataset.
# ➤ Useful for inspecting random samples of data.
print("\n4. Sample (Random 5 Rows):")
print(data.sample(5))




# 5. data.info()
# ➤ Displays a summary of the DataFrame.
# ➤ Shows column names, non-null values, and data types.
print("\n5. Info (Dataset Summary):")
print(data.info())




# 6. data.describe()
# ➤ Provides statistical summary for numerical columns.
# ➤ Includes count, mean, std, min, max, and quartiles.
print("\n6. Describe (Statistical Summary):")
print(data.describe())




# 7. data.columns
# ➤ Returns a list of column names in the DataFrame.
# ➤ Useful to see what features (columns) are present.
print("\n7. Columns (Column Names):")
print(data.columns)




# 8. data.index
# ➤ Returns the index (row labels) of the DataFrame.
# ➤ Shows how the rows are numbered or labeled.
print("\n8. Index (Row Index Info):")
print(data.index)




# 9. data.memory_usage()
# ➤ Returns the memory usage of each column in bytes.
# ➤ Useful for understanding how much memory your DataFrame is using.
print("\n9. Memory Usage (in Bytes):")
print(data.memory_usage())



# 10. data.isnull()
# ➤ Returns a DataFrame of the same shape with True where values are missing (NaN), False otherwise.
# ➤ Helps in identifying where the missing values are.
print("1. Check for Missing Values (True = Missing):")
print(data.isnull())



# 11. data.notnull()
# ➤ Opposite of isnull(); returns True where values are not missing.
print("\n2. Check for Non-Missing Values (True = Present):")
print(data.notnull())



# 12. data.isnull().sum()
# ➤ Returns the count of missing (null) values in each column.
# ➤ Very useful for data cleaning and preprocessing.
print("\n3. Count of Missing Values per Column:")
print(data.isnull().sum())



# 13. data.notnull().sum()
# ➤ Returns the count of non-missing (valid) values in each column.
print("\n4. Count of Non-Missing Values per Column:")
print(data.notnull().sum())




# 14. data.Designation
# ➤ Accesses the 'Designation' column from the DataFrame.
print("\n5. ORDERNUMBER Column:")
print(data.ORDERNUMBER)
print("\n5. QUANTITYORDERED Column:")
print(data.QUANTITYORDERED)
print("\n5.ORDERDATE Column:")
print(data.ORDERDATE)
print("\n5. CUSTOMERNAME Column:")
print(data.CUSTOMERNAME)





# 15. data.Designation.unique()
# ➤ Returns all the unique values in the 'Designation' column.
# ➤ Helps understand the distinct job titles or roles.
print("\n5. ORDERNUMBER Column:")
print(data.ORDERNUMBER.unique())
print("\n5. QUANTITYORDERED Column:")
print(data.QUANTITYORDERED.unique())
print("\n5.ORDERDATE Column:")
print(data.ORDERDATE.unique())
print("\n5. CUSTOMERNAME Column:")
print(data.CUSTOMERNAME.unique())




# 16. data.dtypes
# ➤ Returns data types of each column
print(data.dtypes)




# 17. data.nunique()
# ➤ Number of unique values in each column
print(data.nunique() , )

data.n



# 18. data.value_counts()
# ➤ Count of each unique value (works on a Series only)
print(data["CITY"].value_counts())





# 19. data.duplicated()
# ➤ Returns True for duplicated rows
print(data.duplicated())





# 20. data.duplicated().sum()
# ➤ Count of duplicate rows
print(data.duplicated().sum())




# 21. data.dropna()
# ➤ Removes rows with missing values
cleaned_data = data.dropna()




# 22. data.fillna(0)
# ➤ Fills missing values with 0 (or any value)
data_filled = data.fillna(0)




# 23. data["Salary"].replace(np.inf, np.nan)
# ➤ Replace infinite values with NaN
data["CITY"] = data["CITY"].replace(np.inf, np.nan)





# 24. data.query("Age > 22")
# ➤ Filter rows using a query
print(data.query("Age > 22"))





# 25. data["NewCol"] = data["GPA"] * 10
# ➤ Create a new column
data["GPA_scaled"] = data["QTR_ID"] * 10
print(data.GPA_scaled)




# 26. data.rename(columns={"Roll Number": "Roll_No"})
# ➤ Rename a column
data = data.rename(columns={"YEAR_ID": "YEAR_ID_NO"})




# 27. data.drop(columns=["Language"])
# ➤ Drop a column
data = data.drop(columns=["PRICEEACH"])



## 28. data.groupby("Department").mean()
# ➤ Group by department and calculate mean
print(data.groupby("ORDERNUMBER").mean())




# 29. data.groupby("Gender")["GPA"].max()
# ➤ Max GPA per Gender
print(data.groupby("Gender")["GPA"].max())



# 32. data.to_csv("clean_data.csv")
# ➤ Export DataFrame to CSV
data.to_csv("clean_data.csv", index=False)





# 33. data.to_json("data.json", orient="records", indent=4)
# ➤ Export to JSON in readable format
data.to_json("data.json", orient="records", indent=4)





# 34. data[data["GPA"] > 3.5]
# ➤ Filter rows where GPA is greater than 3.5
print(data[data["GPA"] > 3.5])




# 35. data[(data["Gender"] == "Female") & (data["City"] == "Lahore")]
# ➤ Filter based on multiple conditions
print(data[(data["Gender"] == "Female") & (data["City"] == "Lahore")])






