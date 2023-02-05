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


    <script
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCN2Uj3V2VRs9VYvj121X4olweMBKcBNzI&callback=initMap&v=weekly"
      defer
    ></script>
    <script>
      // Array of markers 
      var markers = [
        {
        coords : {lat: 32.7157, Ing: -117.1611}, 
        content: '<h1>San Diego Breaking news added here </h1> ' 
        },
        {
        coords : {lat: 32.9628, Ing: -117.0359}, 
        content: '<h1>Poway Headlines News </h1> '  
        }, 
        {
        coords : {lat: 32.9628, Ing: -117.0359}, 
        content: '<h1>Poway Headlines News </h1> '  
        }, 
        {  
        coords : {lat: 32.8351, Ing: -116.7664}, 
        content: '<h1>Alpine Headlines News </h1> '  
        }, 
        {
        coords : {lat: 32.8675, Ing: -116.4188}, 
        content: '<h1>Mt Laguna Headlines News </h1> '  
        },
        {
        coords : {lat: 33.1192, Ing: -117.0864}, 
        content: '<h1>Escondido  Headlines News </h1> '  
        }	
      ];



      // Add Marker Function 
      function addMarker(props){ 
        var marker =  new google.maps.Marker({ 
          position:props.coords , 
          map:map, 
        });
        // Check content 
        if(props.content) { 
             var infoWindow = new google.maps.InfoWindow({ 
            content:props.content 
             });

          marker.addListener( 'click', function(){ 
            infoWindow.open(map, marker); 
          });
        }
      }
                                 
      // Initialize and add the map
      function initMap() {
        // The location of Uluru
        const sd = { lat: 32.7157, lng: -117.1611 };
        // The map, centered at Uluru
        const map = new google.maps.Map(document.getElementById("map"), {
          zoom: 8,
          center: sd,
        });
                                 
        // The marker, positioned at Uluru
        const marker = new google.maps.Marker({
          position: sd,
          map: map,
        });
      
        // Loop through markers 
        for(var i = 0; i < markers. length; i++) { 
          addMarker(markers[i]); 
        }      
      }

      window.initMap = initMap;
  </script>

</body>
</html>
