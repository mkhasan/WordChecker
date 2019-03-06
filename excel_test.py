# Import `os`
import os

import pandas as pd

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
cwd

# Change directory
#os.chdir("/path/to/your/folder")

# List all files and directories in current directory
#print(os.listdir('.'))

file = 'TOPIK_Lists.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
#print(xl.sheet_names)

sheet_name = xl.sheet_names

df1 = xl.parse(sheet_name)

#print(len(df1))

a = df1['중급']

print(len(a.columns))