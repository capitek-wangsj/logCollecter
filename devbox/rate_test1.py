# coding=utf-8

import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
#import matplotlib.pyplot as plt

data = {"1522113001": 162454, "1522113061": 306911, "1522113121": 378799, "1522113181": 425046,
        "1522113241": 444792, "1522113301": 518139, "1522113361": 550266, "1522113421": 586098,
        "1522113481": 612848, "1522113541": 616872, "1522113601": 633516, "1522113661": 696442}


def f2(a, b):
    return -1 if a[0] < b[0] else 1


def main():
    list_data = sorted(data.items(), cmp=lambda x, y: cmp(x[0], y[0]))  # 按照 key 正序排列
    byte_df = pd.DataFrame(list_data, columns=['date', 'byte'])  # 将 data 数据转换为 DataFrame操作

    # 原始列表: [1, 3, 3, 8, 15]
    # 增长率: [3, 3, 8, 15] - [1, 3, 3, 8] = [2, 0, 5, 7]
    byte_rise_df = pd.DataFrame(
        np.array(byte_df.byte[1:]) - np.array(byte_df.byte[:-1]),
        columns=['byte_rise_up']
    )
    byte_rise_df['date'] = byte_df.date[1:]  # 添加日期列

    # print byte_rise_df

    print byte_rise_df['date']
    print byte_rise_df['byte_rise_up']




if __name__ == '__main__':
    main()