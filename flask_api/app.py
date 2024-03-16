from flask import Flask, request, jsonify
from detect import detectImage
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

    detectImage(os.path.join(UPLOAD_FOLDER, filename))
    # Process the image 
    # Process the image and generate some text
    text = 'Image processed: ' + filename

    return jsonify({ 'text': text })

if __name__ == '__main__':
    app.run(debug=True)