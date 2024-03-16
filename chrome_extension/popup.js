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

          // Update the background color of the popup container dynamically
          var popupContainer = document.querySelector('.popup-container');
          popupContainer.style.backgroundColor = '#FFA07A'; // Change the background color to light salmon

          // Update the message dynamically
          var message = document.getElementById('message');
          message.textContent = "Your recipe is ready!"; // Change the message content
          message.style.color = '#FF6347'; // Change the text color to tomato
          
          var blob = new Blob([`
              <div style="text-align: center; padding: 20px;">
                  <h1>Ingredients:</h1>
                  <p>${ingredients}</p>
                  <h1>Recipe:</h1>
                  <h2>${recipe}</h2>
              </div>
          `], { type: 'text/html' });

          // Create a URL for the blob
          var blobUrl = URL.createObjectURL(blob);

          // Open a new tab with the blob URL
          chrome.tabs.create({ url: blobUrl });
      });
  });
});
