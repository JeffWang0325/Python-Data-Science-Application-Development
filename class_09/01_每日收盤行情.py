# 引進相關套件
import requests
from io import StringIO
import pandas as pd
import numpy as np
import sys

# 資料日期
date1 = '20210901'
# 網址
url= 'http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date={}&type=ALL'.format(date1)

# 送出要求，並取得回應資料
response = requests.post(url)

clean_data=[]
for row in response.text.split('\n'):
    fields=row.split('",')
    if len(fields) == 17 and row[0] != '=':
        clean_data.append(row.replace(' ',''))

csv_data = "\n".join(clean_data)
print(csv_data)
try:
    df = pd.read_csv(StringIO(csv_data))
except pd.errors.EmptyDataError:
    print('可能是假日或停班 !!')
    sys.exit(0)

df.to_csv('每日收盤行情.csv', index=False, encoding='utf_8_sig') # 解決中文亂碼問題: encoding='utf_8_sig'