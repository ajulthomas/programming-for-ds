# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:13:27 2023

@author: ajult
"""

import io_data_module as iodata
data_list = iodata.read_multi_dim_data_file('iris.data')
for key,value in data_list.items():
    print(key,value)
