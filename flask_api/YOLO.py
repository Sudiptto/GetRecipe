import logging
import io
from ultralytics import YOLO
def UltimateSlicing(model):
    pngString = ".png:"
    speedString = ":deepS"
    frontCounter = 0
    backwardCounter = 0 
    l1 = 0
    l2 = 0
    l3 = 0
    r1 = len(model)-1
    r2 = len(pngString)-1
    r3 = len(speedString)-1
    while l2 < r2:
        if model[l1] == pngString[l2]:
            l2 += 1
        elif model[l1] != pngString[l2]:
            l2 = 0
        l1 += 1
        frontCounter += 1
    while l3 < r3:
        if model[r1] == speedString[l3]:
            l3 += 1
        elif model[l1] != speedString[l2]:
            l3 = 0
        r1 -= 1
        backwardCounter += 1
    sliced =  model[frontCounter + 12: (backwardCounter +11 )*-1 ]
    if ('pizza' or 'pizzas') in sliced:
        print('inside')
        return 'pizza'
    elif ('pasta' or 'pastas') in sliced:
        return 'pasta'
    elif ('cake' or 'cakes') in sliced:
        return 'cake'
    

def imageDetection(imageRoute):
    # Create a string buffer and a stream handler for the logging module
    log_buffer = io.StringIO()
    stream_handler = logging.StreamHandler(log_buffer)

    # Get the Ultralytics logger and add the stream handler to it
    yolo_logger = logging.getLogger('ultralytics')
    yolo_logger.addHandler(stream_handler)

    # Load a pretrained YOLOv8n model
    model = YOLO('yolov8n.pt')

    # Define path to the image file
    source = imageRoute

    # Run inference on the source
    results = model(source)

    # Remove the stream handler from the Ultralytics logger
    yolo_logger.removeHandler(stream_handler)

    # Get the output of the model
    model_output = log_buffer.getvalue()
    food = UltimateSlicing(model_output)

    return food