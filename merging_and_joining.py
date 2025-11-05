import pandas as pd

# First customer DataFrame
df1 = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Ali', 'Javed', 'Zunaira'],
    'City': ['Lahore', 'Karachi', 'Islamabad']
})


# Second customer DataFrame
df2 = pd.DataFrame({
    'CustomerID': [1, 4, 3],
    'Purchase': ['Laptop', 'Mobile', 'Tablet'],
    'Amount': [90000, 35000, 45000]
})

# 1.Merging 

# Merge on 'CustomerID'
merged_df_inner = pd.merge(df1, df2, on='CustomerID', how='inner')
# print(merged_df_inner)


# Left Join (All from df1)
merged_df_left =pd.merge(df1, df2, on='CustomerID', how='left')
# print(merged_df_left )


# Right Join (All from df2)
merged_df_right = pd.merge(df1, df2, on='CustomerID', how='right')
# print(merged_df_right)



# Outer Join (All from both)
merged_df_outer = pd.merge(df1, df2, on='CustomerID', how='outer')
# print(merged_df_outer)



# Cross joint 
merged_df_cross = pd.merge(df1, df2, how='cross')
# print(merged_df_cross)




# 2. Concatenating


#   Syntax : pd.concat([df1, df2], axis=0 ignore_index = True /False)

#   axis=0 is for vertical concatenation
#   axis=1 is for horizontal concatenation
#   ignore_index = True will reset the index of the resulting DataFrame
#   ignore_index = False will keep the index of the resulting DataFrame


new_student_data = {
    "Name": ["Hassan", "Ayesha", "Bilal", "Saba", "Rimshah"],
    "Age": [22, 21, 24, 23, 20],
    "Roll Number": [211, 212, 213, 214, 215],
    "Department": ["AI", "Data Science", "IT", "Mathematics", "Physics"],
    "GPA": [3.6, 3.7, 3.0, 2.8, 3.2],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Language": ["Urdu", "English", "Punjabi", "Sindhi", "Pashto"],
    "City": ["Lahore", "Karachi", "Multan", "Peshawar", "Quetta"],
    "Salary": [52000, 54000, 46000, 43000, 47000],
    "Experience": [1, 2, 1, 1, 0],
    "Performance Rating": [85, 90, 72, 66, 78]
}

data1 = pd.DataFrame(new_student_data)



student_data = {
    "Name": [
        "Javed", "Ghulam", "Mehwish", "Rida", "Qurratulain",
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



data2 = pd.DataFrame(student_data)


df_concate = pd.concat([data1 , data2] , axis = 0 , ignore_index = True)
# print(df_concate)



data = pd.read_csv("students_data.csv" , encoding = "latin1")



data["Bonus"]

print(data)