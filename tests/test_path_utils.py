import pytest
import sys
import os
sys.path.append("..")
from basic_funcs.path_utils import get_fool_dir

# 测试在当前工作目录下存在 fool 文件夹的情况
def test_get_fool_dir_existing():
    expected_path = get_fool_dir()  # 假设当前工作目录下有 fool 文件夹
    assert expected_path[-4:] == 'fool'

# 测试在当前工作目录下不存在 fool 文件夹的情况
# def test_get_fool_dir_not_existing():
#     with pytest.raises(FileNotFoundError):
#         get_fool_dir()
