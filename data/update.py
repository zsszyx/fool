from basic_funcs.time_utils import get_trade_date, start_date 
import pandas as pd
from basic_funcs.sql_utils import save, check_table_exists, get_last_row_date
from data.stocks import hs300, stock_list, stock_history
current_date=get_trade_date()
# default date format: YYYMMDD

def update(func, table_name, params=None):
    if params is None: params={}
    if not check_table_exists(table_name):
        
        save(func(start_date=start_date,end_date=current_date,**params),table_name)
        print(f'table {table_name} not exists, create it')
    else:
        last_date=get_last_row_date(table_name,'date')
        last_date=pd.to_datetime(last_date)
        assert last_date.timestamp()<=current_date.timestamp(), f'last date {last_date} is later than current date {current_date}'
        if last_date.timestamp()==current_date.timestamp():
            print(f'table {table_name} up to date')
        else:
            
            save(func(start_date=last_date+pd.Timedelta(days=1),end_date=current_date,**params),table_name, method='append')
            print(f'update from {last_date} to {current_date}')


class update_manager():
    def __init__(self):
        self.num_threads=4
        self.stock_list=stock_list()

    def update_all(self):
        update(hs300,'hs300')
        for i in self.stock_list:
            params={'code':i}
            update(stock_history,i,params=params)
        
        

  
