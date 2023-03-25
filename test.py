import os

import pandas as pd
train_data = pd.read_csv("data/train_labels.csv")
test_data = pd.read_csv("data/test_labels.csv")

# print(train_data["image"][0])
# print(train_data["label"][0])
# print(len(train_data))

train_list = open('cls_train.txt', 'w')
test_list = open('cls_test.txt', 'w')

for index in range(len(train_data)):
    train_list.write(str(train_data["label"][index] - 1) + ";" +os.path.join("./data/train",train_data["image"][index]))
    train_list.write('\n')

for index in range(len(test_data)):
    test_list.write(str(test_data["label"][index] - 1) + ";" + os.path.join("./data/test",test_data["image"][index]))
    test_list.write('\n')

train_list.close()
test_list.close()

# with open("./datasets/train_list.txt", encoding='utf-8') as f:
#     train_lines = f.readlines()
#     annotation_path = "./datasets/" + train_lines[0].split('	')[0]
#     print(annotation_path)
#     y = int(train_lines[0].split('	')[1])
#     print(1)
    
# import random 
# import h5py
# ck_path = "CK+48"


# anger_path = os.path.join(ck_path, 'anger')
# disgust_path = os.path.join(ck_path, 'disgust')
# fear_path = os.path.join(ck_path, 'fear')
# happy_path = os.path.join(ck_path, 'happy')
# sadness_path = os.path.join(ck_path, 'sadness')
# surprise_path = os.path.join(ck_path, 'surprise')
# contempt_path = os.path.join(ck_path, 'contempt')

# total_path = []
# total_path.append(anger_path)
# total_path.append(disgust_path)
# total_path.append(fear_path)
# total_path.append(happy_path)
# total_path.append(sadness_path)
# total_path.append(surprise_path)
# total_path.append(contempt_path)

# print(total_path)



# train_list = open('cls_train.txt', 'w')
# test_list = open('cls_test.txt', 'w')

# num = 0
# for path in total_path: 
#     pics      = os.listdir(path)
#     number = len(pics)
#     list    = range(number)  
#     tv      = int(number*0.1)  
#     test_index = []
#     test_index= random.sample(list,tv)  
#     train_index = []
#     for i in range(number):
#         if i not in test_index:
#             train_index.append(i)

#     print(len(train_index),len(test_index))

#     for index in train_index:
#         train_list.write(str(num) + ";" + '%s'%(os.path.join(path, pics[index])))
#         train_list.write('\n')

#     for index in test_index:
#         test_list.write(str(num) + ";" + '%s'%(os.path.join(path, pics[index])))
#         test_list.write('\n')
#     num += 1

# train_list.close()
# test_list.close()


# from PIL import Image
# import numpy as np
# data_x1 = []
# data_y1 = []

# data_x2 = []
# data_y2 = []
# data_trainpath = os.path.join('data','CK_traindata.h5')
# data_testpath = os.path.join('data','CK_testdata.h5')

# if not os.path.exists(os.path.dirname(data_trainpath)):
#     os.makedirs(os.path.dirname(data_trainpath))

# if not os.path.exists(os.path.dirname(data_testpath)):
#     os.makedirs(os.path.dirname(data_testpath))
# num = 0
# for path in total_path: 
#     pics      = os.listdir(path)
#     number = len(pics)
#     list    = range(number)  
#     tv      = int(number*0.1)  
#     test_index = []
#     test_index= random.sample(list,tv)  
#     train_index = []
#     for i in range(number):
#         if i not in test_index:
#             train_index.append(i) 
    
#     for index in train_index:
        
#         image = Image.open(os.path.join(path, pics[index]))
#         image = np.array(image)
#         data_x1.append(image)
#         data_y1.append(num)
        
#     for index in test_index:
#         image = Image.open(os.path.join(path, pics[index]))
#         image = np.array(image)
#         data_x2.append(image)
#         data_y2.append(num)    
#     num += 1


# datafile = h5py.File(data_trainpath, 'w')
# datafile.create_dataset("data_pixel", data=data_x1)
# datafile.create_dataset("data_label", data=data_y1)
# datafile.close()

# datafile = h5py.File(data_testpath, 'w')
# datafile.create_dataset("data_pixel", data=data_x2)
# datafile.create_dataset("data_label", data=data_y2)
# datafile.close()

# print(np.shape(data_x1))
# print(np.shape(data_y1))

# print("Save data finish!!!")



