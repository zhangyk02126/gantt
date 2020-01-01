import pandas as pd
import datetime

fname = './2020s1.xlsx'
ef = pd.ExcelFile(fname)
print(ef.sheet_names)
df1 = pd.read_excel(fname, sheet_name='甘特')
df2 = pd.read_excel(fname, sheet_name='假期统计')
# print(df1.head(5))
# print(df2.head(5))
print(df1.columns)
print(df2.columns)
holidays = df2['放假']
# print(holidays.astype(datetime.datetime))

needed_columns = ['里程碑说明', '类别', '责任人', '说明', '计划人日', 'MS期限', '冗余MS', '可重叠任务', '容许的最早开始时间', '容许的最晚开始时']

today = datetime.date.today()
print(today.weekday())
