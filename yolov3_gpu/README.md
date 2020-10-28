# MindSpore YOLOv3-DarkNet53 Tutorial with GPU backend

This is a tutorial for training MindSpore YOLOv3-DarkNet53 model to detecting basketball game.

> **NOTICE:** The codebase of this tutorial is developed based on `v1.0` MindSpore [ModelZoo](https://github.com/mindspore-ai/mindspore/tree/r1.0/model_zoo/official/cv/yolov3_darknet53).

## Guidelines

### Install some system packages

* System package

    ```
    sudo apt install -y unzip
    ```

* Python package

    ```
    pip install opencv-python pycocotools
    ```

* MindSpore (**v1.0**)

    For MindSpore installation, please refer to [MindSpore install page](https://www.mindspore.cn/install).

### Download source code

```
git clone https://github.com/leonwanghui/ms-yolov3-basketball.git
cd ms-yolov3-basketball/
```

### Download basketball dataset

```
cd basketball-dataset/ && wget https://ascend-tutorials.obs.cn-north-4.myhuaweicloud.com/yolov3-darknet53/basketball-dataset/basketball-dataset.zip
unzip basketball-dataset.zip && rm basketball-dataset.zip
cd ../yolov3_gpu/
```

### Download pre-trained DarkNet-53 backbone model

```
cd ./ckpt_files && wget https://ascend-tutorials.obs.cn-north-4.myhuaweicloud.com/yolov3_darknet53/ckpt_files/backbone_darknet53.ckpt
```

### Model training

```
python train.py --data-dir ../basketball-dataset/ --pretrained_backbone ./ckpt_files/backbone_darknet53.ckpt  --max_epoch 320
```

### Download the pre-trained YOLOv3 model

```
cd ./ckpt_files && wget https://ascend-tutorials.obs.cn-north-4.myhuaweicloud.com/yolov3_darknet53/ckpt_files/yolov3-320_1600.ckpt
```

### Model evaluation

```
python eval.py --data-dir ../basketball-dataset/ --pretrained ./ckpt_files/yolov3-320_1600.ckpt
```
```

```

### Model prediction


## License

[Apache License 2.0](../LICENSE)
