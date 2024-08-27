import pandas as pd

data_csv = pd.read_csv("sample.csv", encoding='ISO-8859-1')
# print(data_csv.head(100))
# print(data_csv.tail(20))
print(data_csv.info())

# Creating a DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40],
    'C': [100, 200, 300, 400]
}
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])

print("Original DataFrame:")
print(df)
