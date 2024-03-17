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
source = 'uploads/pizza.png'

# Run inference on the source
results = model(source)

# Remove the stream handler from the Ultralytics logger
yolo_logger.removeHandler(stream_handler)

# Get the output of the model
model_output = log_buffer.getvalue()

# Now you can process the output as needed
print()
print(model_output[110:134])