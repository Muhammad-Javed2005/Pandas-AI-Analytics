import pandas as pd

data = pd.read_csv("students_data.csv" , encoding="latin1")
print(data)


# 1. Selecting Column:
#   1. Selecting a single column and return a series.

column = data["Name"]
print(column)

#   2. Selecting multiple columns and return a dataframe.


columns = data[["Name", "Age" ,"Salary", "Performance Rating" ]]
print(columns)

# 2. Filtering rows:
#   1. Filtering data based on a condition and return a dataframe.
#   2. Filtering data based on a condition and return a series.

filter_row = data[data["GPA"]>3.0]
print(filter_row)


#   2. Filtering data based on multiple conditions and return a dataframe.
#   4. Filtering data based on multiple conditions and return a series.

# 1.
filter_rows= data[(data["Salary"]>=45000) & (data["Salary"]< 50000)]
print(filter_rows)


# 2.
filter_rows_1 = data[(data["Salary"]>45000) & (data["Age"]> 20) | (data["Performance Rating"]>60)]
print(filter_rows_1)


# 3.
filter_row_2= data[(data["Name"].str.len()>=5) & (data["City"].str.len() <8)]
print(filter_row_2)


# 4.
filter_row_3 = data["Age"].min()
print(filter_row_3)


# 5.
filter_row_4 = data["Salary"].sum()
print(filter_row_4)


# 6.
filter_row_5 = data["Performance Rating"].max()
print(filter_row_5)


# 7.
filter_row_6 = data["GPA"].mean()
print(filter_row_6)


# 8.
a = data.describe()
print(a)


# 9.
b = data.info()
print(b)




