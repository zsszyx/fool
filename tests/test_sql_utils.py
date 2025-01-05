import sys
sys.path.append("..")
import pytest
from basic_funcs.sql_utils import save, engine, load, check_table_exists, get_last_row_date
import pandas as pd
from datetime import datetime

# 测试数据
df = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})

# 测试保存方法
def test_save_replace():
    # 执行保存操作
    save(df, 'test_table', method='replace')

    # 验证数据是否成功保存
    result = pd.read_sql('SELECT * FROM test_table', engine)
    assert len(result) == 3
"-------------------------------------------------------------"
# 测试正常加载数据
def test_load_normal():
    # 模拟表名
    table_name = "test_table"
    # 执行加载操作
    result = load(table_name)
    # 断言结果是否与期望一致
    assert result.equals(df)

# 测试表不存在的情况
def test_load_table_not_exist():
    table_name = "non_existent_table"
    # 执行加载操作，期望抛出异常
    with pytest.raises(Exception) as e:
        load(table_name)
    # 断言异常信息是否符合预期
    assert "not found" in str(e.value)

"-------------------------------------------------------------"

def test_save_append():
    # 再次执行保存操作，使用 append 方法
    save(df, 'test_table', method='append')

    # 验证数据是否成功追加
    result = pd.read_sql('SELECT * FROM test_table', engine)
    assert len(result) == 6

def test_save_invalid_method():
    # 测试无效的保存方法
    with pytest.raises(ValueError):
        save(df, 'test_table', method='invalid_method')

"-------------------------------------------------------------"

# 测试表存在的情况
def test_check_table_exists_exists():
    # 模拟数据库连接字符串
    assert check_table_exists('test_table') == True

# 测试表不存在的情况
def test_check_table_exists_not_exists():
    assert check_table_exists('table_name') == False

"-------------------------------------------------------------"

# 测试正常情况
def test_get_last_row_date_normal():
    # 调用方法并验证结果
    result = get_last_row_date('hs300', 'date')
    assert isinstance(result, datetime)


