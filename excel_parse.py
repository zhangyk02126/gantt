import pandas as pd
import datetime
fname = './2020s1_v1.xlsx'
main_sheet = '甘特'
ef = pd.ExcelFile(fname)
assert main_sheet in ef.sheet_names, '%s 不在所给excel的sheet列表中'%main_sheet
# print(ef.sheet_names)
df1 = pd.read_excel(fname, sheet_name=main_sheet)
# df2 = pd.read_excel(fname, sheet_name='假期统计')
# print(df1.head(5))
# print(df2.head(5))
print(df1.columns)
# print(df2.columns)
# holidays = df2['放假']
# print(holidays.astype(datetime.datetime))
title_line_idx = 5
df1.columns=df1.iloc[title_line_idx]
print(df1.columns)

# 人员列表


needed_columns = ['里程碑说明', '类别', '责任人', '说明', '计划人日', 'MS期限', '冗余MS', '可重叠任务', '最早可开始时间', '最晚可开始时间']


today = datetime.date.today()
print(today.weekday())
