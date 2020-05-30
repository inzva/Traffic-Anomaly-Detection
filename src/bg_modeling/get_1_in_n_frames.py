import os
import shutil

N = 6

data_root = "/media/data/umutlu/AIC20_track4/"

original_image_folder = data_root + "test_ori_images/"
subset_folder = data_root + "subset_test_ori_images/"

for i in range(1, 101):
    org_video_folder = original_image_folder + str(i) + "/"
    subset_video_folder = subset_folder + str(i) + "/"

    os.makedirs(subset_video_folder, exist_ok=True)

    files = os.listdir(org_video_folder)

    f = 1
    while f < len(files):
        shutil.copyfile(org_video_folder + str(f) + ".jpg", subset_video_folder + str(f) + ".jpg")
        f += N

    print("Video " + str(i) + " is done.")
