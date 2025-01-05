import pytest
import sys
sys.path.append("..")
from data.stocks import stock_list, hs300

# 测试 stock_list 方法是否返回一个列表
def test_stock_list_returns_list():
    result = stock_list()
    assert isinstance(result, list)

# 测试列表中的元素是否为字符串
def test_stock_list_elements_are_strings():
    result = stock_list()
    for item in result:
        assert isinstance(item, str)

# 测试列表是否不为空
def test_stock_list_is_not_empty():
    result = stock_list()
    assert len(result) > 0

# 测试正常情况
def test_hs300_normal():
    start_date = "20230101"
    end_date = "20230110"
    result = hs300(start_date, end_date)
    assert result is not None
    assert len(result) > 0

# 测试异常情况
def test_hs300_exception():
    start_date = "20230111"
    end_date = "20230101"
    result = hs300(start_date, end_date)
    assert result.empty

# 测试日期格式转换
def test_date_conversion():
    start_date = "2023-01-01"
    end_date = "2023-01-10"
    result = hs300(start_date, end_date)
    assert result is not None
    assert len(result) > 0

# 测试相同日期
def test_same_date():
    start_date = "2023-02-02"
    end_date = "2023-02-02"
    result = hs300(start_date, end_date)
    assert result is not None
    assert len(result) == 1



