# YOLO-NAS

YOLO-NAS is a state-of-the-art object detection model developed by Deci. It is trained on the **"COCO dataset"**, **"object365 Dataset"** and **"roboflow100 Dataset"**.It achieves a mean average precision (mAP) of 50.1% at 220 ms latency on an NVIDIA V100 GPU. This is significantly better than the previous state-of-the-art model, YOLOv8, which achieves an mAP of 46.9% at 260 ms latency.

YOLO-NAS is built on top of the YOLO object detection framework. This means that it can be used with the same tools and techniques as YOLOv8.

## Features

- Neural Architecture Search (NAS): YOLO-NAS was created using NAS, which automatically finds the best architecture for the task, achieving the best trade-off between accuracy and latency.
- Quantization: YOLO-NAS supports quantization to INT8 precision without a significant loss in accuracy, making it suitable for mobile devices and embedded systems.
- Knowledge Distillation: YOLO-NAS utilizes knowledge distillation, where a large, pre-trained model is used to train a smaller, faster model, resulting in improved accuracy.
- Distribution Focal Loss: YOLO-NAS employs distribution focal loss to improve accuracy on small objects by using a loss function that is more sensitive to errors on small objects.

# YOLO-NAS Object detection from image

This repository contains code for performing object detection using the YOLO-NAS model. The YOLO-NAS model is implemented using the `super_gradients` library, an open-source computer vision training library based on PyTorch.

## Features

- YOLO-NAS: The code uses the YOLO-NAS model, which is available in three variants: small, medium, and large.
- Super Gradients: The code utilizes the `super_gradients` library for object detection. This library provides functionalities for training and predicting with computer vision models.

## Requirements

- Python 3.x
- PyTorch
- TorchVision
- OpenCV
- Super Gradients

## Install the required dependencies from given file
pip install -r requirements.txt

* The script will perform object detection on the input image using the specified YOLO-NAS model and display the output image with bounding boxes around detected objects.

## Output  Demo:
![image](https://github.com/meet5398/YOLO-NAS-object-detection/assets/108387640/cd5d3249-bc1f-46b5-aa05-efecd4536bbb)

* you can view file here : https://github.com/meet5398/YOLO-NAS-object-detection/blob/8ae4bc116cd18f6e57484bcbf32dd118aa143015/yolo-nas_image.py

#yolo-nas object detection on video 

https://github.com/meet5398/YOLO-NAS-object-detection/assets/108387640/15c0da44-861b-44b9-89a1-d66b833ae7b7


https://github.com/meet5398/YOLO-NAS-object-detection/assets/108387640/84672056-64ee-4525-a8a0-08ac54e4456c

you can view .py file of vscode here: https://github.com/meet5398/YOLO-NAS-object-detection/blob/8fb7a5a3a4f3064041cfee6cec340a8ad1e9ee9b/object_detection_on_video_using_YOLO-NAS.py  <br>
you can also view google collab file: https://github.com/meet5398/YOLO-NAS-object-detection/blob/d52eb3ac4c8062436e81439965aebe59bbcc4ddb/object_detection_using_yolo_nas_on_collab.ipynb
