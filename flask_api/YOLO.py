from ultralytics import YOLO #GETTING THE YOLO LIBRARY
import numpy

def imageDetection(imageRoute):
    # Load a model
    model = YOLO('yolov8n.pt', "v8")  # load a pretrained model (recommended for training)

    detectionOutput = model.predict(source= imageRoute, conf = 0.25, save = True)
    print(detectionOutput)
    print(detectionOutput[0].numpy())
    