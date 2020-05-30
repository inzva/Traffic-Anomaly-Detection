
# Traffic Anomaly Detection - CVPR NVIDIA AI City Challenge

This repository contains the modified code taken from [https://github.com/ShuaiBai623/AI-City-Anomaly-Detection/](https://github.com/ShuaiBai623/AI-City-Anomaly-Detection/)

We are working on improving this model, yet we are still in the process of replicating the original results.

In the original repository, it is not trivial to directly run the code with the challenge dataset of 2020, and there are some problems with the code. However,
we managed to fix those errors and replicated the results with one exception: We are still trying to figure out how did the original authors use the perspective crops
in the anomaly detection model.

A detailed explanation of the order the scripts should be run will come soon.

The credit goes to the original work: [Traffic Anomaly Detection via Perspective Map based on Spatial-temporal Information Matrix](http://openaccess.thecvf.com/content_CVPRW_2019/papers/AI%20City/Bai_Traffic_Anomaly_Detection_via_Perspective_Map_based_on_Spatial-temporal_Information_CVPRW_2019_paper.pdf)

To cite the original work:

```
@InProceedings{Bai_2019_CVPR_Workshops,
author = {Bai, Shuai and He, Zhiqun and Lei, Yu and Wu, Wei and Zhu, Chengkai and Sun, Ming and Yan, Junjie},
title = {Traffic Anomaly Detection via Perspective Map based on Spatial-temporal Information Matrix},
booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
month = {June},
year = {2019}
}
```