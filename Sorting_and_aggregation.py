import pandas as pd


student_data = {
    "Name": [
        "Javed", "Fabha", "Mehwish", "Rida", "Qurratulain",
        "Zunaira", "Anus", "Ammad", "Rafay", "Muzna"
    ],
    "Age": [22, 21, 23, 24, 25, 20, 22, 21, 24, 23],
    "Roll Number": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    "Department": [
        "Computer Science", "IT", "Mathematics", "AI", "Physics",
        "Biology", "Software Engineering", "Economics", "Statistics", "Chemistry"
    ],
    "GPA": [3.2, 3.5, 2.9, 3.8, 3.1, 3.0, 2.7, 3.6, 3.3, 3.4],
    "Gender": ["Male", "Female", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Female"],
    "Language": ["Urdu", "English", "Punjabi", "English", "Urdu", "Pashto", "Sindhi", "Urdu", "Punjabi", "English"],
    "City": [
        "Karachi", "Lahore", "Islamabad", "Peshawar", "Multan",
        "Quetta", "Rawalpindi", "Faisalabad", "Hyderabad", "Sialkot"
    ],
    "Salary": [45000, 50000, 42000, 55000, 48000, 46000, 40000, 53000, 47000, 49000],
    "Experience": [1, 2, 1, 3, 2, 1, 0, 2, 1, 2],  # in years
    "Performance Rating": [75, 88, 65, 92, 70, 68, 60, 85, 77, 80]  # out of 100
}


data = pd.DataFrame(student_data)


# Sorting a cloumn in descending order:
#   Syntax:
        # data.sort_value(by = "Column Name", ascending = False/True , inplace= Ture)
        # data.sort_values(by = ["Column Name1" , "COlumn Name2" ,....], ascending = False/True , inplace= Ture)

# data.sort_values(by ="GPA", ascending=False, inplace=True)
# print(data[["Name" , "GPA"]])

data.sort_values(by=["GPA" ,"Age" ,"Performance Rating","Salary"] , ascending = [False , True , True , False] , inplace = True)

print(data[["Name" , "GPA" ,"Age" ,"Performance Rating","Salary"]])

# 
# print(data)


# Aggregation function:



# 1. Sum of column:
#       Syntax: data["column name"].sum()

sum_of_salary = data["Salary"].sum()
print("Sum of Salary : ",sum_of_salary)
sum_of_age = data["Age"].sum()
print("Sum of Age : ",sum_of_age)




# 2. Mean of column:
#       Syntax: data["column name"].mean()

mean_of_GPA = data["GPA"].mean()
print("Mean of GPA : ",mean_of_GPA)
mean_of_performance = data["Performance Rating"].mean()
print("Mean of Performance Rating : ",mean_of_performance)



# 3. Median of column:
#       Syntax: data["column name"].median()

median_of_experience = data["Experience"].median()
print("Median of Experience : ",median_of_experience)
median_of_age = data["Age"].median()
print("Median of Age : ",median_of_age)



# 4.Mode of column:
#       Syntax: data["column name"].mode()
#       Note: If there are multiple modes, it will return all of them.

mode_of_performance = data["Performance Rating"].mode()
print("Mode of Performance Rating : ",mode_of_performance)



# 5. Standard Deviation of column:
#       Syntax: data["column name"].std()


std_deviation_of_age = data["Age"].std()
print("Standard Deviation of Age : ",std_deviation_of_age)


# 6. Variance of column:
#       Syntax: data["column name"].var()


variance_of_age = data["Age"].var()
print("Variance of Age : ",variance_of_age)



# 7. Unique values in a column:
#       Syntax: data["column name"].unique()

unique_values_of_performance = data["Performance Rating"].unique()
print("Unique values of Performance Rating : ",unique_values_of_performance)



# 8. Count of unique values in a column:
#       Syntax: data["column name"].nunique()

count_of_unique_performance = data["Performance Rating"].nunique()
print("Count of unique values of Performance Rating : ",count_of_unique_performance)



# 9. Dataframe info
#       Syntax: data.info()

data.info()



# 10. Dataframe describe
#       Syntax: data.describe()

data.describe()



# 11. Dataframe head
#       Syntax: data.head()

data.head()




# 12. Dataframe tail
#       Syntax: data.tail()

data.tail()



# 13. Max value in a column
#       Syntax: data["column name"].max()

max_age = data["Age"].max()
print("Max age : ",max_age)

# 14. Min value in a column
#       Syntax: data["column name"].min()

min_experience = data["Experience"].min()
print("Min experience : ",min_experience)







