# From a dictionary
student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 78, 98]
}

# We can loop through a dictionary
for (key, value) in student_dict.items():
    print(key)
    print(value)
# RESULT:
# student
# ['Angela', 'James', 'Lilly']
# score
# [56, 78, 98]

print()

# Similarly, we can loop through a DataFrames (but this way is not very useful as it iterates over each column in the
# DataFrame, not over each row in the DataFrame)
import pandas

students_dataframe = pandas.DataFrame(student_dict)
# RESULT:
#   student  score
# 0   Angela      56
# 1    James      78
# 2    Lilly      98

for column, content in students_dataframe.items():
    print(column)
    print(content)
# RESULT:
# student
# 0    Angela
# 1     James
# 2     Lilly
# score
# 0    56
# 1    78
# 2    98

print()

# Pandas has the iterrows() method which allows to loop trough each row in a DataFrames
for (index, row) in students_dataframe.iterrows():
    print(row)  # row is a pandas Series object
# RESULT:
# student    Angela
# score          56
# student    James
# score         78
# student    Lilly
# score         98

print()

# Since row is a Series object we can get specific values from that row either using dot notation o brackets notation
for (index, row) in students_dataframe.iterrows():
    if row["student"] == "Angela":
        print(row["score"])
