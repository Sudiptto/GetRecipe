from flask import Flask, request, jsonify
from YOLO import imageDetection 
#from detect import detectImage
from recipe import * 
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# GET THE IMAGE FROM THE USERS AND UPLOAD IT TO THE UPLOADS DIRECTORY (LOCAL)
@app.route('/api/form', methods=['POST'])
def handle_form():
    image = request.files['image']
    filename = secure_filename(image.filename)
    image.save(os.path.join(UPLOAD_FOLDER, filename))

    #detectImage(os.path.join(UPLOAD_FOLDER, filename))
    # Process the image 
    # Process the image and generate some text
    text = 'Image processed: ' + filename
    imageRoute = f"uploads/{filename}"
    imageDetection(imageRoute) #RUNS THE IMAGE DETECTION FUNCTION IN THE YOLO.PY SCRIPT

    # Note: Using Samin's recipie.py right now to return back a twoD 
    food = "pizza" # placeholder for now
    allRecipe = getRecipe(food)
    ingredients = allRecipe[0]
    recipe = allRecipe[1]

    return jsonify({ 'ingredients': ingredients, 'recipe': recipe })

if __name__ == '__main__':
    app.run(debug=True)