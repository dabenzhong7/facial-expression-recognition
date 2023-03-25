#!usr/bin/env python
# encoding:utf-8
from __future__ import division
 
 
"""
__Author__: 沂水寒城
功能： fer2013数据解析存储
"""
 
 
import os
import cv2
import json
import time
import pandas as pd
import numpy as np
from PIL import Image
 

 
 
def fer2013ToImgs(data_path="data/train_labels.csv", rgb=True, saveDir="data/"):
    """
    数据集解析转化
    """
    if data_path == "data/train_labels.csv":
        list_file = open('cls_train.txt', 'w')
        Usage = "train"
    else :
        list_file = open('cls_test.txt', 'w')
        Usage = "test"

    count = 0
    df = pd.read_csv(data_path)
    data_list = df.values.tolist()
    # print("data_list_length: ", len(data_list))

    for i in range(len(data_list)):
        image_path, emotion = data_list[i]
        oneDir = saveDir + Usage + "/"
        if not os.path.exists(oneDir):
            os.makedirs(oneDir)
            
        one_path = (oneDir + image_path)
        print("Saving to: ", one_path)

        list_file.write(str(emotion - 1) + ";" + '%s'%(one_path))
        list_file.write('\n')
        count += 1
       
    print("count: ", count)
    list_file.close()

 
 
 
 
if __name__ == "__main__":
 

 	
    print(
        "==================================Loading Data Parser===================================="
    )
 
 
    fer2013ToImgs(data_path="data/train_labels.csv", saveDir="data/")
 
    
    fer2013ToImgs(data_path="data/test_labels.csv", rgb=True, saveDir="data/")
 