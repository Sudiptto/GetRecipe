"""from ultralytics import YOLO #GETTING THE YOLO LIBRARY
import numpy

def imageDetection(imageRoute):
    imageRoute = ""
    model = YOLO('yolov8n.pt', "v8")  # load a pretrained model (recommended for training)

    detectionOutput = model.predict(source= imageRoute, conf = 0.25, save = True)
    print(detectionOutput)
    print(detectionOutput[0].numpy())
    return food
"""
import logging
import io
from ultralytics import YOLO

# Create a string buffer and a stream handler for the logging module
log_buffer = io.StringIO()
stream_handler = logging.StreamHandler(log_buffer)

# Get the Ultralytics logger and add the stream handler to it
yolo_logger = logging.getLogger('ultralytics')
yolo_logger.addHandler(stream_handler)

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Define path to the image file
source = 'uploads/CAKE.png'

# Run inference on the source
results = model(source)

# Remove the stream handler from the Ultralytics logger
yolo_logger.removeHandler(stream_handler)

# Get the output of the model
model_output = log_buffer.getvalue()

# Now you can process the output as needed
print()
print(len(model_output))
pngString = ".png:"
speedString = ":deepS"
frontCounter, backwardCounter = 0 , 0
l1 , l2, l3 = 0, 0, 0
r1 = len(model_output)-1
r2 = len(pngString)-1
r3 = len(speedString)-1
while l2 < r2:
    if model_output[l1] == pngString[l2]:
        l2 += 1
    elif model_output[l1] != pngString[l2]:
        l2 = 0
    l1 += 1
    frontCounter += 1
while l3 < r3:
    if model_output[r1] == speedString[l3]:
        l3 += 1
    elif model_output[l1] != speedString[l2]:
        l3 = 0
    r1 -= 1
    backwardCounter += 1
print(frontCounter)
print(backwardCounter)
    

    

print(model_output[frontCounter + 1: -])
