import pandas as pd

# read from csv file
csv = pd.read_csv('data/example.csv')
print(csv)

# write to csv file
csv.to_csv('data/csvOutput.csv', index=False)
print(pd.read_csv('data/csvOutput.csv'))

# read from excel file
excel = pd.read_excel('data/Excel_Sample.xlsx', sheetname = 'Sheet1')
print(excel)

# write to excel file
excel.to_excel('data/xlsxOutput.xlsx', index=False)
print(pd.read_excel('data/xlsxOutput.xlsx'))

# read from html
html = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(html[0].head()) # or print(html) or print(html[0])
