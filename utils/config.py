# coding: utf-8
import os

dataset1_root_test = '/home/asus/Datasets/binary_segmentation/RGBD_SOD_Datasets/DUT-RGBD/test_data'
dataset2_root_test = '/home/asus/Datasets/binary_segmentation/RGBD_SOD_Datasets/LFSD'
dataset1 = os.path.join(dataset1_root_test)
dataset2 = os.path.join(dataset2_root_test)

Model1 = '/home/asus/Datasets/binary_segmentation/result_map/rgbdsod/2021/DSNet/' # model_path
Model2 = '/home/asus/Datasets/binary_segmentation/result_map/rgbdsod/2021/UTA/' # model_path

Models = {'Model1':Model1,'Model2':Model2}
test_datasets = {'dataset1':dataset1,'dataset2':dataset2}