import akshare as ak
from basic_funcs.sql_utils import save
from basic_funcs.time_utils import get_trade_date, start_date
import pandas as pd
# default date format: YYYMMDD

empty_df = pd.DataFrame({
   'date':[start_date-pd.Timedelta(days=1)],
   'open':[None],
   'close':[None],
   'high':[None],
   'low':[None],
   'volume':[None],
   'amount':[None],
   'swing':[None],
   'change_pct':[None],
   'change_amount':[None],
   'turnover_rate':[None],
})
# empty_df = pd.DataFrame()


def hs300( start_date, end_date, code='')->pd.DataFrame:
    start_date = pd.to_datetime(start_date).strftime("%Y%m%d")
    end_date = pd.to_datetime(end_date).strftime("%Y%m%d")
    try:
        index_zh_a_hist_df = ak.index_zh_a_hist(symbol="000300", period="daily", start_date=start_date, end_date=end_date)
        index_zh_a_hist_df= index_zh_a_hist_df.rename(columns={'日期': 'date', '开盘': 'open', '收盘': 'close', '最高': 'high', '最低': 'low', '成交量': 'volume', '成交额': 'amount', '振幅': 'swing', '涨跌幅': 'change_pct', '涨跌额': 'change_amount', '换手率': 'turnover_rate'})
    except Exception as e:
        print('hs300 data error')
        index_zh_a_hist_df = empty_df
    return index_zh_a_hist_df.infer_objects()


def stock_history(code, start_date, end_date)->pd.DataFrame:
    start_date = pd.to_datetime(start_date).strftime("%Y%m%d")
    end_date = pd.to_datetime(end_date).strftime("%Y%m%d")
    try:
        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=code, period="daily", start_date=start_date, end_date=end_date, adjust='hfq')
        stock_zh_a_hist_df.drop(columns=['股票代码'], inplace=True)
        stock_zh_a_hist_df= stock_zh_a_hist_df.rename(columns={'日期': 'date', '开盘': 'open', '收盘': 'close', '最高': 'high', '最低': 'low', '成交量': 'volume', '成交额': 'amount', '振幅': 'swing', '涨跌幅': 'change_pct', '涨跌额': 'change_amount', '换手率': 'turnover_rate'})
    except:
        print(f'{code} data error')
        stock_zh_a_hist_df = empty_df
    return stock_zh_a_hist_df.infer_objects()

def stock_list()->list:
    df = ak.stock_zh_a_spot_em()
    df = df[['代码','名称']]
    df = df.rename(columns={'代码':'code','名称':'name'})
    print('stock list长度: ',len(df))
    return list(df['code'])

if __name__ == '__main__':
    print(stock_list())