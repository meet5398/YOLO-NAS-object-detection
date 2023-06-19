import cv2
from super_gradients.training import models
import torch
device=torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")
model=models.get("yolo_nas_m",pretrained_weights="coco").to(device)
# yolo -nas come up with 3 model small, medium and large
out=model.predict("image.jpg")
out.show()
# use of super_gradient library : to do  object detection using yolo-nas we require super_gradient library
#super_gradient is pytorch based open source computer vision  training library 
# if we install super_gradient library it will also install pytorch and torch vision library

# reading image from opencv and then detecting object in it
image =cv2.imread("image.jpg")
image =cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

out2=model.predict(image)
out2.show()