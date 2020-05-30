import skimage
from skimage.measure import label
from scipy.ndimage.filters import gaussian_filter
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# video_id = 1
count_thred = 0.08
min_area = 2000
gass_sigma = 3
score_thred = 0.1
for video_id in range(1, 101):
    with open("../../detection_results/test_framebyframe_2/video%s.txt" % (video_id), 'r') as f:
        # dt_results_fbf = json.load(f)
        dt_results_fbf = {}
        for line in f:
            line = line.rstrip()
            word = line.split(',')
            frame = int(word[0])
            x1 = int(word[2])
            y1 = int(word[3])
            tmp_w = int(word[4])
            tmp_h = int(word[5])
            score = float(word[6])
            if frame not in dt_results_fbf:
                dt_results_fbf[frame] = []
            if score > score_thred:
                dt_results_fbf[frame].append([x1, y1, x1 + tmp_w, y1 + tmp_h, score])

    im = cv2.imread("/media/data/umutlu/AIC20_track4/test_ori_images/%s/1.jpg" % video_id)
    h, w, c = im.shape
    mat = np.zeros((h, w))
    for frame in dt_results_fbf:
        if frame < 18000:
            tmp_score = np.zeros((h, w))
            for box in dt_results_fbf[frame]:
                score = box[4]
                tmp_score[int(float(box[1])):int(float(box[3])),int(float(box[0])):int(float(box[2]))] = np.maximum(score,tmp_score[int(float(box[1])):int(float(box[3])),int(float(box[0])):int(float(box[2]))])

            mat = mat + tmp_score

    mat = mat - np.min(mat)
    mat = mat / np.max(mat)
    mask = mat > count_thred
    mask = label(mask, connectivity=1)
    num = np.max(mask)
    for i in range(1, int(num + 1)):
        if np.sum(mask == i) < min_area:
            mask[mask == i] = 0
    mask = mask > 0
    mask = mask.astype(float)
    k = gaussian_filter(mask, gass_sigma)
    mask = k > count_thred
    np.save("../../detection_results/seg_masks_2/%s.npy" % str(video_id), mask)

    img = Image.fromarray(mask.astype('byte'))
    plt.imsave(str(video_id) + ".jpg", img, cmap='gray')
