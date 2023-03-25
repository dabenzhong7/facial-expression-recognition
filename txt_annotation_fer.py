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
 
 
 
def cvtColor(image):
    """
    将图像转换成RGB图像
    """
    if len(np.shape(image)) == 3 and np.shape(image)[2] == 3:
        return image 
    else:
        image = image.convert('RGB')
        return image 
 
 
def fer2013ToImgs(data_path="fer2013.csv", rgb=True, saveDir="dataset/"):
    """
    数据集解析转化
    """
    train_file = open('cls_train.txt', 'w')
    test_file = open('cls_test.txt', 'w')
    count = 0
    df = pd.read_csv(data_path)
    data_list = df.values.tolist()
    print("data_list_length: ", len(data_list))
    width, height = 48, 48
    for i in range(len(data_list)):
        emotion, pixels, Usage = data_list[i]
        face = [int(pixel) for pixel in pixels.split(" ")]
        face = np.asarray(face).reshape(width, height)
        face = cv2.resize(face.astype("uint8"), (width, height))
        oneDir = saveDir + Usage + "/" + str(emotion) + "/"
        if not os.path.exists(oneDir):
            os.makedirs(oneDir)
        one_path = (
            oneDir + str(emotion) + "_" + str(len(os.listdir(oneDir)) + 1) + ".jpg"
        )
        print("Saving to: ", one_path)
        if rgb:
            img = Image.fromarray(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
            img = cvtColor(img)
            
            if Usage == "Training":
                train_file.write(str(emotion) + ";" + '%s'%(one_path))
                train_file.write('\n')
            else :
                test_file.write(str(emotion) + ";" + '%s'%(one_path))
                test_file.write('\n')
#            img.save(one_path)
        else: 
            continue
#            cv2.imwrite(one_path, face)
        count += 1
       
    print("count: ", count)
    train_file.close()
    test_file.close()
 
 
 
 
if __name__ == "__main__":
 

 	
    print(
        "==================================Loading Data Parser===================================="
    )
 
 
    # fer2013ToImgs(data_path="fer2013.csv", saveDir="dataset/")
 
    
    fer2013ToImgs(data_path="fer2013.csv", rgb=True, saveDir="dataset/")
 