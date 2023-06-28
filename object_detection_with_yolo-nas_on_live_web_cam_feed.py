import cv2
import torch
from super_gradients.training import models
device=torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")
model=models.get("yolo_nas_m",pretrained_weights="coco").to(device)

model.predict_webcam(conf=0.5)
#by default confidence score is 0.25