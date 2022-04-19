//Defining the service worker for the app
// Listen for install event, set callback
self.addEventListener('install', function(event) {
    // Perform some task
    console.log('Service Worker Installed');
});

self.addEventListener('activate', function(event) {
    // Perform some task
    console.log("Service Worker Activated");
  });