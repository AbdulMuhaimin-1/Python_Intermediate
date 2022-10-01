student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through a data frame

# for (key, value) in student_data_frame.items():
#     print(key)

# Loop through rows of a dataframe

for (index, row) in student_data_frame.iterrows():
    # print(row.score)
    if row.student == "Angela":
        print(row.score)

# {new_key:new_value for (index, row) in df.iterrows()}
