<<<<<<< HEAD
# task 02 数据分析
#coding:utf-8
#导入warnings包，利用过滤器来实现忽略警告语句。
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from tqdm import tqdm
import multiprocessing as mp
import os
import pickle
import random
# 把读取所有数据的函数放在单独的python文件中，是为了解决多线程问题在jupyter notebook无法运行的问题
import read_all_data

class Load_Save_Data(): # 定义加载和存储数据的函数
    def __init__(self,file_name=None):
        self.filename = file_name

    def load_data(self,Path=None):
        if Path is None:
            assert self.filename is not None,"Invalid Path...."
        else:
            self.filename = Path
        with open(self.filename,"wb") as f:
            data = pickle.load(f)
        return data

    def save_data(self,data,path):
        if path is None:
            assert self.filename is not None,"Invalid path...."
        else:
            self.filename = path
        with open(self.filename,"wb") as f:
            pickle.dump(data,f)

# 定义读取数据的函数
def read_data(Path,Kind=""):
    """
    :param Path:待读取数据的存放路径
    :param Kind:'train' of 'test'
    """

    # 替换成数据存放的路径
    filenames = os.listdir(Path)
    print("\n@Read Data From"+Path+".........................")
    with mp.Pool(processes=mp.cpu_count()) as pool:
        data_total = list(tqdm(pool.map(read_all_data.read_train_file if Kind == "train" else 
                                        read_all_data.read_test_file,filenames),total=len(filenames)))
    print("\n@End Read total Data............................")
    load_save = Load_Save_Data()
    if Kind == "train":
        load_save.save_data(data_total,"./data_tmp/total_data.pkl")
    return data_total

# 训练数据读取

# 存放数据的绝对路径
train_path = "/Users/gaohan/Documents/GitHub/wisdomOcean/智慧海洋组队文件/hy_round1_train_20200102/"
data_train = read_data(train_path,Kind="train")
data_train = pd.concat(data_train)

# 测试数据读取

# 存放数据的绝对路径
test_path = "/Users/gaohan/Documents/GitHub/wisdomOcean/智慧海洋组队文件/hy_round1_testA_20200102/"
data_test = read_data(test_path,Kind="test")
data_test = pd.concat(data_test)
=======
import
>>>>>>> 30368350c02f9bf8a97bc8e8c08cfe2b984f37ab
