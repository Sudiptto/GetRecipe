self.addEventListener('fetch', function(event) {
    if (event.request.url.endsWith('/api/data')) {
      event.respondWith(fetch(event.request).then(function(response) {
        return response.json().then(function(data) {
          console.log(data.message);
          return new Response(JSON.stringify(data));
        });
      }));
    }
  });