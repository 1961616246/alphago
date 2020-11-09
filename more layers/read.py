# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:16:28 2020

@author: Li Jiahao
"""
from matplotlib import pyplot as plt

list = []
with open('loss_list.txt', 'r') as f:
    list = f.readlines()
plt.figure(1, figsize=(8, 8))
plt.xlabel('games')
plt.ylabel('loss')
plt.plot(range(1, len(list)+1), list)