#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:04:26 2017

@author: fayewang
"""

import pandas as pd
import numpy as np
import re

cn_rap =  pd.read_csv('lyrics.csv')
cn_rap = cn_rap.dropna(axis=0, how='any')
cn = ''.join(cn_rap['lyric'])


def translate(st):  
    line = st.strip()  
    p2 = re.compile(u'[^\u4e00-\u9fa5]+')  # 中文的编码范围是：\u4e00到\u9fa5  
    zh = " ".join(p2.split(line)).strip()  
    zh = "\n".join(zh.split())  
    return zh

cn_data = translate(cn)

for i in range(len(cn_data)):
    line = cn_data[i]
    if "歌词" in line or "作词" in line or "作曲" in line or "编曲" in line or "录音" in line or "混缩" in line or "制作人" in line:
        cn_data[i] = "\n"
        
        
with open("cn_raps.txt", "w") as text_file:
    text_file.write(cn_data)
