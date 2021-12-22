## Introduction

This is a project for the Tianchi competition: adversarial attack for universal object detection. Here is the url: https://tianchi.aliyun.com/competition/entrance/531806/information. We obtain the second in this contest.

## Data preparation and model checkpoint.

- Download 1000 pictures needed for the competition on the official [website](https://tianchi.aliyun.com/competition/entrance/531806/information)
- You can get data (`images.zip`) and the definition, weight and evaluation code of two white box models (`eval_code.zip`). We use yolov4 and faster_rcnn as whitebox models.
- Create two new folders, `images` and `models`, Unzip `images.zip` to `images`, and move all checkpoint and config files to models.

## Requirements

This code is based on pytorch. Some basic dependencies are recorded in `requirements.txt`

- torch
- torchvision
- pillow
- numpy
- tqdm
- scipy
- scikit-image
 
You can run yolov4 now if all above requirements are satisfied.

Another faster rcnn model is implemented based on mmdetection. So, ensure that the mmdetection library has been installed and can be run on your machine. You can refer install guide of mmdetection to [github](https://github.com/open-mmlab/mmdetection/blob/master/docs/install.md)

After installation, put the mmdetection directory into `eval_code/` below. Alternatively, it is optional that using [docker](https://github.com/open-mmlab/mmdetection/blob/master/docker/Dockerfile) provided by mmdetection.

## Usage

Unzip `eval_code.zip`，move and unzip `images.zip` to` images`, ensure the following structure:

```
|--images
    |-- XXX.png
    |-- XXX.png
    |-- XXX.png
    …
    |-- XXX.png
```

Move all checkpoints and config files to `models` as:

```
|--models
    |-- faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth
    |-- yolov4.cfg
    |-- yolov4.weights
```

## Run Attack algorithm

```bash
python attack.py --patch_type grid --lines 3 --box_scale 1.0
python attack.py --patch_type grid --lines 2 --box_scale 1.0
python attack.py --patch_type grid --lines 1 --box_scale 1.0


python attack.py --patch_type astroid
```

## Run ensemble algorithm
```bash
python ensemble.py
```
## attack your custom yolov4 model
1、 modify yolov4_helper.py
    #model path
    class Helper():
       def __init__(self):
       # cfgfile = "models/yolov4.cfg"
       # weightfile = "models/yolov4.weights"
       cfgfile = "models/custom.cfg"
       weightfile = "models/custom.weights"

       #class number
       item = item.reshape(-1, 5+16, h*w).permute(1,0,2).reshape(5+16, -1)

2. update the class number  and anchor numbers according to your model's  config file
       #    anchors = [12, 16, 19, 36, 40, 28, 36, 75, 76, 55, 72, 146, 142, 110, 192, 243, 459, 401]
       #    num_anchors = 9
       #    anchor_masks = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
       #    strides = [8, 16, 32]
       anchors = [8, 13,  18, 27,  25, 54,  52, 37,  38, 93,  77, 74,  62,134, 194, 60, 133,132,  85,232, 157,291, 288,207]
       num_anchors = 12
       anchor_masks = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
       strides = [8,16,32]

3. run attack
       python attackyolo.py --patch_type grid --lines 3 --box_scale 1.0

       python attackyolo.py --patch_type astroid