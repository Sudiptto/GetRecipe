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

          // NOTE FOR AYEN: THIS IS WHERE YOU CAN MODIFY THE HTML/CSS FOR THE MESSAGE.HTML (where the ingredients are )
          // Create a new HTML blob with the ingredients and recipe
          // The text is centered using CSS and each ingredient is on a new line
          // Front-end developers can modify the CSS here to change the appearance of the text
            var blob = new Blob([`
              <html>
                <body style="background-color: yellow;">
                  <div style="text-align: center; padding: 20px; color: black;">
                    <h1>Ingredients:</h1>
                    <p>${ingredients}</p>
                    <h1>Recipe:</h1>
                    <p>${recipe}</p>
                  </div>
                </body>
              </html>
            `], { type: 'text/html' });

          // Create a URL for the blob
          var blobUrl = URL.createObjectURL(blob);

          // Open a new tab with the blob URL
          chrome.tabs.create({ url: blobUrl });
      });
  });
});