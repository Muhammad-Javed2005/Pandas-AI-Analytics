import pandas as pd

student_data = {
    "Name": [
        "Javed", None, "Mehwish", "Rida", "Qurratulain",
        "Zunaira", "Anus", "Ammad", "Rafay", "Muzna"
    ],
    "Age": [22, 21, 23, 24, None, 20, 22, 21, 24, 23],
    "Roll Number": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    "Department": [
        "Computer Science", "IT", "Mathematics", "AI", "Physics",
        "Biology", None , "Economics", "Statistics", "Chemistry"
    ],
    "GPA": [3.2, 3.5, None, 3.8, 3.1, 3.0, 2.7, 3.6, 3.3, 3.4],
    "Gender": ["Male", "Female", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Female"],
    "Language": ["Urdu", "English", "Punjabi", "English", "Urdu", "Pashto", "Sindhi", "Urdu", "Punjabi", "English"],
    "City": [
        "Karachi", "Lahore", "Islamabad", "Peshawar", "Multan",
        None, "Rawalpindi", "Faisalabad", "Hyderabad", "Sialkot"
    ],
    "Salary": [45000, 50000, 42000, 55000, 48000, 46000, 40000, 53000, 47000, 49000],
    "Experience": [1, 2, 1, 3, 2, 1, 0, 2, 1, 2],  # in years
    "Performance Rating": [75, 88, 65, None, 70, 68, 60, None , 77, 80]  # out of 100
}

df = pd.DataFrame(student_data)
# print(df)

# 1. isnull()
#   Return dataframe in boolean type
#   True = Value not present or Nan is missing
#   False = Value present or Not missing

print(df.isnull())

# Return total sum of Nan values in each column
print(df.isnull().sum())


# Drop or delete all rows whose have Nan value
# df.dropna(axis = 0 ,inplace=True)


# Drop or delete all coulmns whose have Nan value
# df.dropna(axis = 1 ,inplace=True)



# Replace Nan value with zero
# df.fillna(0,inplace=True)

# Replace Nan value with mean value of this column
df['GPA'].fillna(df['GPA'].mean(), inplace=True)
df["Age"].fillna(df["Age"].mean() , inplace = True)



print(df)



