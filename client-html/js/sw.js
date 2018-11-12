// This is an special build get the newest at https://github.com/antonk123/haweb
var CACHE_NAME = 'chache';
var urlsToCache = [
  '/',
  '/index.html',
  '/css/main.css',
  '/css/menu.css',
  '/js/menu.js',
  '/icon/favicon-32x32.png',
  '/icon/favicon-16x16.png',
  '/icon/favicon.ico'
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});
self.addEventListener('fetch', function(event) {
    event.respondWith(
      caches.match(event.request)
        .then(function(response) {
          // Cache hit - return response
          if (response) {
            return response;
          }
          return fetch(event.request);
        }
      )
    );
  });             