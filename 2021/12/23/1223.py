import pandas as pd
import openpyxl
INPUT_FILE_NAME = 'population2021.xlsx'
INPUT_BOOK = pd.ExcelFile(INPUT_FILE_NAME)
INPUT_SHEET_NAME = INPUT_BOOK.sheet_names
print(INPUT_SHEET_NAME)
df = INPUT_BOOK.parse(INPUT_SHEET_NAME[0])
print(df)