
import os
import glob
import json
import shutil
import numpy as np
import xml.etree.ElementTree as ET

# JPEGImages为原始的数据集文件夹
# Annotations为原始的数据集对应的标签文件夹
JPEGImages = 'JPEGImages/'
Annotations = 'Annotations/'

imageid = glob.glob(Annotations + '/*.xml')
imageid = [i.split('.')[0][-11:] for i in imageid]
print(imageid)

np.random.seed(100)
np.random.shuffle(imageid)

train_ratio = 0.9
train_num = int(len(imageid) * train_ratio)
print('train_num is {}'.format(train_num))
print('val_num is {}'.format(len(imageid) - train_num))
img_xml_list_train = imageid[:train_num]
img_xml_list_val = imageid[train_num:]



# 开始搬运jpg和xml到各自对应的文件夹
# train 为划分后的训练集文件夹
# train_xml为划分后训练集对应的xml文件夹
# val 为划分后的训练集文件夹
# val_xml为划分后训练集对应的xml文件夹

for i in img_xml_list_train:
    img_name = os.path.join(JPEGImages + i + '.jpg')
    shutil.copy(img_name, 'train/' + i + '.jpg')

    xml_name = os.path.join(Annotations + i + '.xml')
    shutil.copy(xml_name, 'train_xml/' + i + '.xml')


for i in img_xml_list_val:
    img_name = os.path.join(JPEGImages + i + '.jpg')
    shutil.copy(img_name, 'val/' + i + '.jpg')

    xml_name = os.path.join(Annotations + i + '.xml')
    shutil.copy(xml_name, 'val_xml/' + i + '.xml')
