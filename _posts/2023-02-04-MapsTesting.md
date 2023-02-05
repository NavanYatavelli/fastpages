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
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB41DRUbKWJHPxaFjMAwdrzWzbVKartNGg&callback=initMap&v=weekly"
      defer
    ></script>
  </body>
</html>
