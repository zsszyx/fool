import configparser
import pandas as pd
from sqlalchemy import create_engine, text
from basic_funcs.path_utils import get_fool_dir
import os

# 1. 读取配置文件
config = configparser.ConfigParser()
config.read(os.path.join(get_fool_dir(), 'sqlconfig.ini'))

# 2. 获取数据库连接参数
db_config = config['database']
username = db_config['username']
password = db_config['password']
host = db_config['host']
port = db_config['port']
database_name = db_config['database_name']

# 3. 创建数据库连接
db_url = f"postgresql://{username}:{password}@{host}:{port}/{database_name}"
engine = create_engine(db_url)

def save(df, table_name, method='replace'):
    df.to_sql(table_name, engine, if_exists=method, index=False)

def load(table_name):
    return pd.read_sql_table(table_name, engine)


def check_table_exists(table_name,schema='public'):
    """
    检查指定的表是否存在
    :param db_url: 数据库连接字符串
    :param schema: 模式名称
    :param table_name: 表名称
    :return: 表存在返回 True 否则返回 False
    """
    # 创建数据库引擎
    # engine = create_engine(db_url)

    # 构建查询语句
    query = text("""
    SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema = :schema
        AND table_name = :table_name
    )
    """)

    # 执行查询并获取结果
    with engine.connect() as connection:
        result = connection.execute(query, {"schema": schema, "table_name": table_name}).scalar()

    return result

def get_last_row_date(table_name, date_column):
    """
    获取指定表的最后一行数据的日期
    :param db_url: 数据库连接字符串
    :param table_name: 表名称
    :param date_column: 日期字段名
    :return: 最后一行数据的日期
    """

    # 构建查询语句
    query = text(f"""
    SELECT {date_column}
    FROM {table_name}
    ORDER BY {date_column} DESC
    LIMIT 1;
    """)

    # 执行查询并获取结果
    with engine.connect() as connection:
        result = connection.execute(query).scalar()

    return pd.to_datetime(result)

def delete(table_name): 
    with engine.connect() as conn:
        with conn.begin():
            # 执行 DROP TABLE 语句
            conn.execute(text(f"DROP TABLE IF EXISTS {table_name}"))



# 使用示例
if __name__ == "__main__":
    print(load('hs300'))