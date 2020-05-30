import os
import json
import numpy as np
from tqdm import tqdm

data_root = "/media/data/umutlu/AIC20_track4/"

original_image_folder = data_root + "subset_test_ori_images/"
processed_image_folder = data_root + "test_processed_images/"

org_json_file = open(data_root + "subset_test_ori_images_info.json", 'w+')
prc_json_file = open(data_root + "test_processed_images_info.json", 'w+')
for i in tqdm(range(1, 101)):
    org_video_folder = original_image_folder + str(i) + "/"
    prc_video_folder = processed_image_folder + str(i) + "/"

    for root, dirs, files in os.walk(org_video_folder):
        for file in files:
            json_dict = {}
            json_dict["filename"] = str(i) + "/" + file
            json_dict["instances"] = [{"bbox": [], "label": [], "is_ignored": False}]
            json.dump(json_dict, org_json_file)
            org_json_file.write('\n')

    for root, dirs, files in os.walk(prc_video_folder):
        for file in files:
            json_dict = {}
            json_dict["filename"] = str(i) + "/" + file
            json_dict["instances"] = [{"bbox": [], "label": [], "is_ignored": False}]
            json.dump(json_dict, prc_json_file)
            prc_json_file.write("\n")

org_json_file.close()
prc_json_file.close()
