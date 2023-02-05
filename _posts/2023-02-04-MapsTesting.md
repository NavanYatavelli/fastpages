---
toc: false
layout: post
description: Maps Testing
categories: [Maps Testing]
title: Maps Testing
---

<html>
  <head>
    <title>Add Map</title>
    <style>
    #map {
      height: 400px; /* The height is 400 pixels */
      width: 100%; /* The width is the width of the web page */
    }
    </style>
  </head>
  <body>
    <h3>My Google Maps Demo</h3>
    <!--The div element for the map -->
    <div id="map"></div>

    <!-- 
      The `defer` attribute causes the callback to execute after the full HTML
      document has been parsed. For non-blocking uses, avoiding race conditions,
      and consistent behavior across browsers, consider loading using Promises
      with https://www.npmjs.com/package/@googlemaps/js-api-loader.
      -->
    <script
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCN2Uj3V2VRs9VYvj121X4olweMBKcBNzI&callback=initMap&v=weekly"
      defer
    ></script>
    <script>
      // Initialize and add the map
      function initMap() {
        // The location of Uluru
        const uluru = { lat: -25.344, lng: 131.031 };
        // The map, centered at Uluru
        const map = new google.maps.Map(document.getElementById("map"), {
          zoom: 4,
          center: uluru,
        });
        // The marker, positioned at Uluru
        const marker = new google.maps.Marker({
          position: uluru,
          map: map,
        });
      }

      window.initMap = initMap;
  </script>

</body>
</html>
