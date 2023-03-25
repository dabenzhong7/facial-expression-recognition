import os
from os import getcwd
from random import shuffle
from utils.utils import get_classes
import cv2

classes_path    = 'model_data/ck_classes.txt'

datasets_path   = 'CK+48'
sets            = ["train", "test"]

classes, _      = get_classes(classes_path)


number = 981
each_sum_number = [135,177,75,207,84,249,54] # the sum of class number
test_number = [36,54,22,63,22,72,17] # the number of each class


photos_name = []
index = 0
if __name__ == "__main__":

    train_file = open('cls_train.txt', 'w')
    test_file = open('cls_test.txt', 'w')

    for cls in classes:
        datasets_path_t = os.path.join(datasets_path, cls)
        photos_name      = os.listdir(datasets_path_t)
        test_index = []
        train_index = []
        fold = 1

        for k in range(test_number[index]):
            test_index.append((fold-1)*test_number[index]+k * 3)



        for i in range(each_sum_number[index]):
            if i not in test_index:
                train_index.append(i)
        print(len(train_index),len(test_index))
        

        for photo_index in train_index:
            _, postfix = os.path.splitext(photos_name[photo_index])
            if postfix not in ['.jpg', '.png', '.jpeg']:
                continue
            train_file.write(str(index) + ";" + '%s'%(os.path.join(datasets_path_t, photos_name[photo_index])))
            train_file.write('\n')

        for photo_index in test_index:
            _, postfix = os.path.splitext(photos_name[photo_index])
            if postfix not in ['.jpg', '.png', '.jpeg']:
                continue
            test_file.write(str(index) + ";" + '%s'%(os.path.join(datasets_path_t, photos_name[photo_index])))
            test_file.write('\n')

        index += 1

    train_file.close()
    test_file.close()



