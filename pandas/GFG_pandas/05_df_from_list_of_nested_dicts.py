# Convert list of nested dictionary into Pandas dataframe
import pandas as pd

# 1. Using from_dict(orient='index')
data = [
    {'A': {'a': 1, 'b': 2}, 'B': {'a': 3, 'b': 4}},
    {'A': {'a': 5, 'b': 6}, 'B': {'a': 7, 'b': 8}},
]
df1 = pd.DataFrame.from_dict({i: data[i] for i in range(len(data))}, orient='index')
print("DataFrame using from_dict(orient='index'):\n", df1)


# 2. Native Method

data = [
    {'A': {'a': 1, 'b': 2}, 'B': {'a': 3, 'b': 4}},
    {'A': {'a': 5, 'b': 6}, 'B': {'a': 7, 'b': 8}},
]
df2 = pd.DataFrame(data)
print("\nDataFrame using native method:\n", df2)

# so whats the difference?
# Both methods yield the same result in this case, creating a DataFrame from a list of nested dictionaries.
# however, the from_dict method provides more flexibility in terms of orientation and handling of data structures.
# how? 
# The from_dict method allows you to specify the orientation of the data (e.g., 'index' or 'columns'),
# which can be useful when dealing with more complex data structures or when you want to control how the data is interpreted.

# another example
list = [{
        "Student": [{"Exam": 90, "Grade": "a"},
                    {"Exam": 99, "Grade": "b"},
                    {"Exam": 97, "Grade": "c"},
                    ],
        "Name": "Paras Jain"
        },
        {
        "Student": [{"Exam": 89, "Grade": "a"},
                    {"Exam": 80, "Grade": "b"}
                    ],
        "Name": "Chunky Pandey"
        }
        ]

rows = []

for data in list:
    data_row = data['Student']
    time = data['Name']

    for row in data_row:
        row['Name'] = time
        rows.append(row)

# using data frame
df = pd.DataFrame(rows)

print(df)