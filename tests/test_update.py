import pytest
import sys
sys.path.append("..")
from data.update import update
from basic_funcs.time_utils import get_trade_date, start_date
from basic_funcs.sql_utils import check_table_exists, get_last_row_date
from data.stocks import stock_list, hs300

# 测试表不存在的情况
def test_update_table_not_exists():
    table_name = "hs300"
    update(hs300,table_name)
    assert check_table_exists(table_name)

# 测试表已存在且最新日期与当前日期相同的情况
def test_update_table_up_to_date():
    table_name = "hs300"
    last_date = get_trade_date()
    update(hs300, 'hs300')
    assert get_last_row_date(table_name, 'date') == last_date

from data.update import update_manager

# 测试构造函数是否正确初始化
def test_update_manager_init():
    # 创建 update_manager 对象
    um = update_manager()

    # 断言 num_threads 是否正确设置
    assert um.num_threads == 4

    # 断言 stock_list 是否正确初始化
    assert um.stock_list is not None

# 测试异常情况
def test_update_manager_init_exception():
    # 尝试创建 update_manager 对象时传入非法参数
    with pytest.raises(TypeError):
        um = update_manager(num_threads="非法参数")


