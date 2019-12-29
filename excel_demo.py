import pandas as pd
import datetime
fname = '/Users/zhangyukui/Documents/2020s1.xlsx'
ef = pd.ExcelFile(fname)
print(ef.sheet_names)
df1 = pd.read_excel(fname,sheet_name='甘特')
df2 = pd.read_excel(fname,sheet_name='假期统计')
# print(df1.head(5))
# print(df2.head(5))
print(df1.columns)
print(df2.columns)
holidays = df2['放假']
# print(holidays.astype(datetime.datetime))

today = datetime.date.today()
print(today.weekday())