from datetime import datetime
import akshare as ak
import pandas as pd
import time
start_date = '20190101'
start_date = datetime.strptime(start_date, '%Y%m%d')


def get_trade_date():
    # 获取交易日期数据
    df = ak.tool_trade_date_hist_sina()
    
    # 将 trade_date 列转换为 datetime 类型
    df['trade_date'] = pd.to_datetime(df['trade_date'])
    
    # 获取当前日期
    today = datetime.now()
    
    # 找到最近的交易日
    time_delta = (df['trade_date'] - today)
    # print(time_delta.tail(20), today-today)
    time_delta =time_delta[time_delta<= today-today]
    time_delta = time_delta.argmax()
    nearest_trade_date = df.iloc[time_delta]['trade_date']
    
    print(f"最近的交易日是: {nearest_trade_date}")
    return nearest_trade_date
    
if __name__ == '__main__':
    get_trade_date()