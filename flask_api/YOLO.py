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

"""# Create a string buffer and a stream handler for the logging module
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
#print()
#print(model_output)

# use a pointer to get rid of the path  from model_output

start = 0
end = 0
wordToCut = '.png'
p2 = 0

for i in range(len(model_output)):
    if model_output[i] == wordToCut[p2]:
        p2 += 1
        if p2 == len(wordToCut):
            end = i
            break
#print(end)
#print(len(model_output))
#print(model_output[end:])

newOutput = model_output[end+3:]
#print(newOutput)

# delete everything after '\n' -> find \
findSlash = newOutput.find("\n")
#print(findSlash)

newOutput = newOutput[:findSlash]
#print(newOutput)

# create functions -> one for slicing and another to return """

def sliceOutput(model_output):
    end = 0
    wordToCut = '.png'
    p2 = 0

    for i in range(len(model_output)):
        if model_output[i] == wordToCut[p2]:
            p2 += 1
            if p2 == len(wordToCut):
                end = i
                break
    newOutput = model_output[end+3:]

    # delete everything after '\n' -> find \
    findSlash = newOutput.find("\n")

    newOutput = newOutput[:findSlash]

    # create functions -> one for slicing and another to return 
    return newOutput.lower()

def getFood(food):
    log_buffer = io.StringIO()
    stream_handler = logging.StreamHandler(log_buffer)

    # Get the Ultralytics logger and add the stream handler to it
    yolo_logger = logging.getLogger('ultralytics')
    yolo_logger.addHandler(stream_handler)

    # Load a pretrained YOLOv8n model
    model = YOLO('yolov8n.pt')

    # Define path to the image file
    source = food

    # Run inference on the source
    results = model(source)

    # Remove the stream handler from the Ultralytics logger
    yolo_logger.removeHandler(stream_handler)

    # Get the output of the model
    model_output = log_buffer.getvalue()

    # send what we get from model_output to the sliceOutput function

    model_sliced = sliceOutput(model_output)
    #print(model_sliced)
    if ('pizza' or 'pizzas') in model_sliced:
        print('inside')
        return 'pizza'
    elif ('pasta' or 'pastas') in model_sliced:
        return 'pasta'
    elif ('cake' or 'cakes') in model_sliced:
        return 'cake'
    # add more


print(getFood("uploads/pizza.png")) # should return pizza
