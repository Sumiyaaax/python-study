import pandas as pd

CSV_FILE='covid-19_daily_survey.csv'
df = pd.read_csv(CSV_FILE)
print(df)
print(len(df))
print(len(df.columns))
print(df.info())
cols = df.columns.values.tolist()
print(df.iloc[:2])
print(cols)