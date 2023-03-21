import pandas as pd
pd.options.display.max_rows = 9999
s = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv.txt')
s1 = s.dropna(inplace = True)
print(s.duplicated())
print(s.corr())
print(pd.options.display.max_rows)
