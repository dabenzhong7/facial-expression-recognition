'''
predict.py有几个注意点
1、无法进行批量预测，如果想要批量预测，可以利用os.listdir()遍历文件夹，利用Image.open打开图片文件进行预测。
2、如果想要将预测结果保存成txt，可以利用open打开txt文件，使用write方法写入txt，可以参考一下txt_annotation.py文件。
'''
from PIL import Image

from classification import Classification

import time
import os
classfication = Classification()

fps = 0.0
# while True:
datasets_path   = 'data/test'
photos_name     = os.listdir(datasets_path)
photos_name     = photos_name[0:100]

for photo in photos_name:
    t1 = time.time()
    try:
        image = Image.open(datasets_path+"/"+photo)
    except:
        print('Open Error! Try again!')
        continue
    else:
        class_name = classfication.detect_image(image)
        fps  = ( fps + (1./(time.time()-t1)) ) / 2
        print("fps= %.2f"%(fps))
        print(class_name)