from flask import Flask, request, jsonify
from flask import send_from_directory
from recipe import * 
from YOLO import *
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

    # use Oluwajembola's function to get the food -> YOLO
    food = imageDetection(imageRoute)
    # Note: Using Samin's recipie.py right now to return back a twoD 
    allRecipe = getRecipe(food)

    ingredients = allRecipe[0]
    recipe = allRecipe[1]
    print(ingredients, recipe)
    #print(ingredients, recipe)
    # TEST FOR AYEN USE THESE TO NOT DRAIN OPENAI
    # How to use comment out the previous lines of code above and use the ingredients down here instead (so comment out the allRecipe, ingredients and recipe variables above and use the new ones below)
    #ingredients = ['Dough', 'Tomato sauce', 'Mozzarella cheese', 'Olive oil', 'Salt', 'Pepper', 'Fresh basil', 'Pizza toppings (e.g., pepperoni, mushrooms, onions, etc.)']
    #recipe = ['Preheat the oven to 475°F (245°C).', 'Roll out the pizza dough on a floured surface to your desired thickness.', 'Transfer the dough to a greased baking sheet or pizza stone.', 'Spread a thin layer of pizza sauce evenly over the dough.', 'Top with your favorite toppings, such as cheese, pepperoni, mushrooms, onions, and bell peppers.', 'Bake in the preheated oven for about 10-15 minutes, or until the crust is golden and the cheese is melted and bubbly.', 'Remove the pizza from the oven and let it cool for a few minutes before slicing and serving.', 'Enjoy your classic homemade pizza!']
    return jsonify({ 'ingredients': ingredients, 'recipe': recipe, 'filename': filename })

# used to send images from the uploads directory to the front-end
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.run(debug=True)