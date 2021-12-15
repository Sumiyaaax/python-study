import pandas as pd
import os
import datetime

CSV_FILE='covid-19_daily_survey.csv'
OUTPUT_CSV_FILE='output_1.csv'
df = pd.read_csv(CSV_FILE)
print(df)
print(len(df))
print(len(df.columns))
print(df.info())
cols = df.columns.values.tolist()
print(df.iloc[:2])
print(cols)
df = df[['医療機関ID','医療機関名', '都道府県名', '医療機関住所', '電話番号']]
print(df)
df.to_csv(OUTPUT_CSV_FILE, index=False)
print(os.listdir('./'))
os.remove('output_1.csv')
print(os.listdir('./'))
# os.mkdir('test2')
print('============walk============')
print(os.walk('./'))
os.system('ls -l')
dt_now = datetime.datetime.now()
print(dt_now.year)
print(dt_now.month)
print(dt_now.day)
print(df.pivot_table(index='医療機関ID',columns='都道府県名',values='電話番号'))
df.set_index('医療機関ID', inplace=True)
print(df)