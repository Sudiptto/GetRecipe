// TAKE THE PICTURE DATA AND SEND TO FLASK 
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('myForm').addEventListener('submit', function(event) {
      event.preventDefault();
  
      var fileInput = document.getElementById('inputBox');
      var file = fileInput.files[0];
  
      var formData = new FormData();
      formData.append('image', file);
  
      fetch('http://127.0.0.1:5000/api/form', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        var blob = new Blob(["<h1>" + data.text + "</h1>"], { type: 'text/html' });
        var blobUrl = URL.createObjectURL(blob);
        chrome.tabs.create({ url: blobUrl });
      });
    });
  });