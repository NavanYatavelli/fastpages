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
      height: 700px; /* The height is 400 pixels */
      width: 150%; /* The width is the width of the web page */
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
      // Initialize and add the map
      function initMap() {
        // The location of Borrego Springs
        var sd = { lat: 33.2559, lng: -116.3750 };
        // The map, centered at Uluru
        var map = new google.maps.Map(document.getElementById("map"), {
          zoom: 10,
          center: sd,
        });
        /*
        var poway = {lat: 32.9628, lng: -117.0359};  
        var marker1 = new google.maps.Marker({
          position: poway,
          map: map,
        });      
                                 
        // The marker, positioned at Uluru      
        var marker = new google.maps.Marker({
          position: sd,
          map: map,
        });
       */
           // Array of markers 
        var markers = [
          {
          coords : {lat: 32.7157, lng: -117.1611}, 
          content: '<p style="color:blue;">Padres FanFest mayhem: Long lines, crowded concourses, and delayed entry</p>' 
          },
          {
          coords : {lat: 33.4934, lng: -117.1488}, 
          content: '<p style="color:blue;">Temecula - Forklifts Stolen From Home Depot</p>'  
          }, 
          {
          coords : {lat: 33.6846, lng: -117.8265}, 
          content: '<p style="color:blue;">Long Beach State beats UC Irvine in OT</p> '  
          }, 
          {  
          coords : {lat: 32.7920, lng: -115.5631}, 
          content: '<p style="color:blue;"> El Centro will conduct a public hearing for new parks</p>'  
          }, 
          {
          coords : {lat: 33.8734, lng: -115.9010}, 
          content: '<p style="color:blue;">Backpacking Permits For Joshua Tree National Park Available Online</p>'  
          },
          {
          coords : {lat: 33.1192, lng: -117.0864}, 
          content: '<p style="color:blue;">Escondido council appoints Palomar College trustee to vacant seat</p>'  
          }	
        ];
      
        // Loop through markers 
        for(var i = 0; i < markers.length; i++) { 
          addMarker(markers[i]); 
        }
                                          
        // Add Marker Function 
        function addMarker(props){ 
          var marker =  new google.maps.Marker({ 
            position:props.coords, 
            map:map, 
          });
          // Check content 
          if(props.content) { 
               var infoWindow = new google.maps.InfoWindow({ 
              content:props.content 
               });
            infoWindow.open(map, marker);//display by default
            marker.addListener( 'click', function(){ 
              infoWindow.open(map, marker); 
            });
          }
        }                                          
      }

      window.initMap = initMap;
  </script>

</body>
</html>
