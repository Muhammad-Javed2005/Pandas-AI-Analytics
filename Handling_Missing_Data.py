import pandas as pd

# Sample Data with Missing Values


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
    "Experience": [1, 2, 1, 3, 2, 1, 0, 2, 1, 2],
    "Performance Rating": [75, 88, 65, None, 70, 68, 60, None , 77, 80],
    "Employee ID" : [101 , None , 103 ,104 , None , 106 , 107 , 108 , None , 110]
}

data = pd.DataFrame(student_data)



#   1. Linear Interpolation
#           Description: Straight-line interpolation between two known values.
#           Syntax: data.interpolate(method='linear')

linear_data = data.copy()
linear_data.interpolate(method='linear', inplace=True)
print("Linear Interpolation:\n", linear_data[["Age", "GPA", "Performance Rating", "Employee ID"]])



# 2. Index Interpolation
#           Description: Interpolates using index values (good if index has meaning).
#           Syntax: data.interpolate(method='index')

index_data = data.copy()
index_data.interpolate(method='index', inplace=True)
print("🔹 Index Interpolation:\n", index_data[["Age", "GPA", "Performance Rating", "Employee ID"]])



#  3. Nearest Interpolation
#           Description: Fills NaN using nearest non-null data point.
#           Syntax: data.interpolate(method='nearest')

nearest_data = data.copy()
nearest_data.interpolate(method='nearest', inplace=True)
print("🔹 Nearest Interpolation:\n", nearest_data[["Age", "GPA", "Performance Rating", "Employee ID"]])


#  4. Polynomial Interpolation
#          Description: Fits a polynomial curve of specified order to interpolate.
#          Syntax: data.interpolate(method='polynomial', order=2)

polynomial_data = data.copy()
polynomial_data.interpolate(method='polynomial', order=2, inplace=True)
print("🔹 Polynomial Interpolation (Order 2):\n", polynomial_data[["Age", "GPA", "Performance Rating", "Employee ID"]])




#  5. Spline Interpolation
#          Description: Uses spline curves for smooth interpolation.
#          Syntax: data.interpolate(method='spline', order=2)

spline_data = data.copy()
spline_data.interpolate(method='spline', order=2, inplace=True)
print("🔹 Spline Interpolation (Order 2):\n", spline_data[["Age", "GPA", "Performance Rating", "Employee ID"]])




#  6. Forward Fill (Pad)
#           Description: Fills missing values using the previous non-null value.
#           Syntax: data.fillna(method='pad')

pad_data = data.copy()
pad_data.fillna(method='pad', inplace=True)
print("🔹 Forward Fill (Pad):\n", pad_data[["Age", "GPA", "Performance Rating", "Employee ID"]])





# 7. Backward Fill (Bfill)
#           Description: Fills missing values using the next non-null value.
#           Syntax: data.fillna(method='bfill')

bfill_data = data.copy()
bfill_data.fillna(method='bfill', inplace=True)
print("🔹 Backward Fill:\n", bfill_data[["Age", "GPA", "Performance Rating", "Employee ID"]])




#  8. Time Interpolation
#           Description: Interpolation using datetime index (only works if index is datetime).
#           Syntax: data.interpolate(method='time')

# ❌ Not applicable here — your DataFrame has no datetime index.


