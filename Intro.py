# Author : Engr. Muhammad Javed

import pandas as pd 

# Read data from csv file into data frame
# Use encoding = "uft-8" or "latin1"
data1 = pd.read_csv("sales_data_sample.csv" , encoding = 'latin1')
# print(data1)



# Read data from excel file into data frame
# First pip install openpyxl library or xlrd library for read excel file.
data2 = pd.read_excel("SampleSuperstore.xlsx")
# print(data2)



# Read data from json file into data frame
# First pip install json library or json5 library for read json file.
data3 = pd.read_json("sample_Data.json")
# print(data3)




# Create Student data dictionary:

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


# Create DataFrame
df_students = pd.DataFrame(student_data)

# Display DataFrame
print(df_students)

# Optional: Save as CSV and Excel
df_students.to_csv("students_data.csv", index=False)
df_students.to_excel("students_data.xlsx", index=False)
df_students.to_json("students_data.json", orient="records", indent=4)

# To create .json file so you can use this code
# df_students.to_json("students_data.json", orient="records", indent=4)




data10 = pd.read_csv("sales_data_sample.csv" , encoding = "latin1")
data10.to_json("sales_data_sample.json" , orient="records" , indent=4)


