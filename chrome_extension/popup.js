// This script is executed when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Add an event listener for the form submission
  document.getElementById('myForm').addEventListener('submit', function(event) {
      // Prevent the default form submission action
      event.preventDefault();

      // Get the file input element and the file it contains
      var fileInput = document.getElementById('inputBox');
      var file = fileInput.files[0];

      // Create a new FormData object and append the file to it
      var formData = new FormData();
      formData.append('image', file);

      // Make a POST request to the Flask API with the FormData object
      fetch('http://127.0.0.1:5000/api/form', {
          method: 'POST',
          body: formData
      })
      .then(response => response.json()) // Parse the JSON response from the server
      .then(data => {
          // Convert the ingredients and recipe arrays into strings
          // Each ingredient is separated by a line break for better readability
          var ingredients = data.ingredients.join('<br>');
          var recipe = data.recipe.join('. ');

          //png file name
          var filename = data.filename;

          // NOTE FOR AYEN: THIS IS WHERE YOU CAN MODIFY THE HTML/CSS FOR THE MESSAGE.HTML (where the ingredients are )
          // Create a new HTML blob with the ingredients and recipe
          // The text is centered using CSS and each ingredient is on a new line
          // Front-end developers can modify the CSS here to change the appearance of the text
            var blob = new Blob([`
            <html lang="en">
            <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Londrina+Shadow&family=Madimi+One&display=swap" rel="stylesheet">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Madimi+One&display=swap" rel="stylesheet">
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Recipe</title>
            </head>
            <style>.body {
            background-color: #ffffe0; /* Light yellow background */
            font-family: Arial, sans-serif;
            }
            ,container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            }
            ,content {
            text-align: center;
            padding: 20px;
            color: black;
            border: 2px solid #ffd700; /* Gold border */
            border-radius: 10px;
            background-color: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Soft shadow */
            }
            ,recipe-details {
            margin-top: 20px;
            text-align: center;s
            }
            h1 {
            color: #ff6347; /* Tomato red for headings */
            font-size: 2.5em;
            font-family: "Madimi One", sans-serif;
            text-align: center;
            }
            h2 {
            color: #4682b4; /* Steel blue for subheadings */
            font-size: 1.5em;
            font-family: "Londrina Shadow", sans-serif;
            font-weight: bold;
            text-align: center;
            }
            p {
            font-size: 1.1em;
            line-height: 1.6;
            text-align: center;
            }
            img{
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 30%;
            }
            </style>
            <body style="background-color: #ffffe0;">
            <div class="container">
            <div class="content">
            <h1>Delicious Recipe</h1>
            <div class="recipe-details">
            <h2>Ingredients:</h2>
            <p>${ingredients}</p>
            <h2>Recipe:</h2>
            <p>${recipe}</p>
            </div>
            <img src = "http://127.0.0.1:5000/uploads/${filename}" style=>
            </div>
            </div>
            </body>
            </html>`], { type: 'text/html' });

          // Create a URL for the blob
          var blobUrl = URL.createObjectURL(blob);

          // Open a new tab with the blob URL
          chrome.tabs.create({ url: blobUrl });
      });
  });
});

