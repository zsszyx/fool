import os
import configparser

def get_fool_dir():
    # 获取当前工作目录
    current_dir = os.getcwd()

    # 找到fool文件夹的路径
    fool_dir = None
    while current_dir:
        if os.path.basename(current_dir) == 'fool':
            fool_dir = current_dir
            break
        current_dir = os.path.dirname(current_dir)

    # 如果找到了fool文件夹，则读取sqlconfig.ini文件
    if fool_dir:
        return fool_dir
    else:
        raise FileNotFoundError("fool文件夹未找到")

if __name__ == '__main__':
    print(get_fool_dir())