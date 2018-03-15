#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os


def readFileConfigs():
    file_name_list = []
    filenames = []
    list_dir = '/usr/local/capitek/aaa/data/server/log/radacct/acctrec/'
    file_names = os.listdir(list_dir)

    for file_name in file_names:
        filename = os.path.splitext(file_name)[0]  # 文件名
        filenames.append(int(filename))

    # 对文件进行排序
    filenames.sort()

    for x, y in enumerate(filenames):
        for files in file_names:
            filename = os.path.splitext(files)[0]  # 文件名
            if int(filename) == y:
                file_name_list.append(os.path.join(list_dir, files))

    return file_name_list


def json_list():
    file_name_list = readFileConfigs()

    return file_name_list
