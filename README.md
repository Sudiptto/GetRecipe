# Project Documentation

## Overview

This project is a Chrome extension leveraging AI and Computer Vision to analyze food images and return corresponding recipes. The AI model used is a pre-trained YOLOv8 model from the Ultralytics library. The application communicates with various APIs and uses Flask as the backend framework, with a frontend built using HTML, CSS, and JavaScript.

## Installation

Ensure Python is installed on your machine (`python --version`). Install the necessary Python packages by running `pip install -r requirements.txt` in the project directory.

## OpenAI Key

This project uses the OpenAI API. You will need to obtain your own OpenAI key. Visit the [OpenAI website](https://www.openai.com/) to get your key.

## Running the Application

The application comprises a Chrome extension and a Flask API.

### Chrome Extension

1. Navigate to `chrome://extensions/` in Chrome.
2. Enable Developer mode (top right).
3. Click "Load unpacked" and select the `chrome_extension` directory.

### Flask API

1. Navigate to the `flask_api` directory in your terminal.
2. Run `python app.py` to start the Flask server.

## Usage

1. Open the Chrome extension and upload a PNG food image.
2. The extension sends the image to the Flask API.
3. The API processes the image with the YOLOv8 model and returns a recipe.
4. The recipe is displayed in the Chrome extension.

## Technologies and APIs

The project uses the following technologies:

- Flask: Backend framework.
- HTML/CSS/JavaScript: Frontend technologies.
- Python-JavaScript communication: To facilitate interaction between the frontend and backend.

The project communicates with the following APIs:

- OpenAI
- The Meal DB API: [https://www.themealdb.com/](https://www.themealdb.com/)

## Dependencies

Key libraries used include Flask, Ultralytics, OpenCV, Torch, Torchvision, Numpy, Pandas, Matplotlib, and Seaborn. Refer to `requirements.txt` for a full list of dependencies.

---

Developed by: Ayen (Hunter College), Samin (Hunter College), Oluwajembola (Midwood High School), and Sudiptto (Hunter College).