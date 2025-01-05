import pytest
import sys
sys.path.append("..")
from datetime import datetime
from basic_funcs.time_utils import get_trade_date, start_date
import pandas as pd

# 测试获取交易日期的功能
def test_get_trade_date():
    # 调用方法获取交易日期
    trade_date = get_trade_date()

    # 断言交易日期不为空
    assert trade_date is not None

    # 断言交易日期是 datetime 类型
    assert isinstance(trade_date, datetime)

    assert trade_date <= datetime.now()

    # 断言交易日期在预期范围内
    # 这里假设交易日期在过去的一年内
    assert trade_date >= datetime.now() - pd.Timedelta(days=10)
    
def test_start_date():
    assert start_date == datetime.strptime('20190101', '%Y%m%d')