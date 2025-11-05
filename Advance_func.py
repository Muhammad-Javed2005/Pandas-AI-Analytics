import pandas as pd

student_data = {
    "Name": [
        "Javed", "Fabha", "Mehwish", "Rida", "Qurratulain",
        "Zunaira", "Anus", "Ammad", "Rafay", "Muzna"
    ],
    "Age": [22, 21, 23, 24, 23, 20, 22, 21, 24, 23],
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
# print(data)




# 1. Adding new column to dataframe:

#   Syntax:
        # data["New_column_name"] = [list_of_values] or "any equation" or "any formula"

data["Bonus"] = data["Salary"] * 0.1
print(data[["Name" , "Bonus"]])
data["Country"] = "Iran"




# Using lambda function to create new column in dataframe:
#   Syntax:
# data["New_column_name"] = data.apply(lambda row: "any equation" or "
# "any formula", axis=1)

data['Bonus3'] = data.apply(lambda row:
                          row['Salary']*.5 if row['Age']>=20
                          else row['Salary']*.4 if row['Age']>=22
                          else row['Salary']*.1 if row['Age']>=24
                          else row['Salary']*.05, axis=1)




def Bonus(sal):
    if sal > 200000:
        return sal * 0.5
    elif sal>= 150000:
        return sal * 0.3
    elif sal>= 100000:
        return sal * 0.25
    elif sal >= 75000:
        return sal * 0.2
    else :
        return sal * 0.1


data['Bouns2'] = data.Salary.apply(lambda sal:sal*.5 if sal>=40000
                                else sal*.3 if sal>=45000
                                else sal*.25 if sal>=50000
                                else sal*.2 if sal>=55000
                                else sal*.1)


# Using insert method:
#   Syntax:
#       data.insert(loc, column_name, values)

data.insert(3 , "Bonus" , data["Salary"] * 0.1)
data.insert(1 , "Employee ID" , [101 , 102 , 103 ,104 , 105 , 106 , 107 , 108 , 109 , 110])
print(data[["Name" , "Bonus" , "Employee ID"]])
print(data)


# 2. Update a value in column:
#   Syntax:
#       data.loc[row_index  , "Column Name"] = new_value

data.loc[2 , "Age"] = 32
print(data[["Name" , "Age"]])

data.loc[5 ,"Salary"] = 50000
print(data[["Name" , "Salary"]])

data["Salary"] = data["Salary"] * 1.05
print(data[["Name" , "Salary"]])


# Delete or drop a column:
#   Syntax:
#       data.drop("column_name" , axis=1 , inplace=True)
#


data.drop("Bonus" , axis=1 , inplace=True)
data.drop("Country" , axis=1 , inplace=True)
print(data)



# Delete or drop a row:
#   Syntax:
#       data.drop(index , axis=0 , inplace=True)

data.drop(0 , axis=0 , inplace=True)
data.drop(5, axis=0 , inplace=True)
print(data)


# Grouped by a column and apply a function to each group:
#   Syntax:
#       data.groupby("column_name").apply(function_name)

grouped = data.groupby("Age")["Salary"].sum()
print(grouped)




print(data[["Bonus2 , Bonus3"]])
