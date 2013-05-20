// This file is part of Loukku, an application to display available rental apartments on Google Maps map.
// Copyright (C) 2013  Anton Laurila, Jari-Matti Kankaanpää, Samuel Uusi-Mäkelä
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as
// published by the Free Software Foundation, either version 3 of the
// License, or (at your option) any later version.
// For more information, please refer to LICENCE file found in /Lakauma,
// or <http://www.gnu.org/licenses/> and GNU Affero General Public License


    var map;   
    var infowindow;
    var markers = [];
    function initialize() {	

        //Center the map to desired location        
        var mapOptions = {
          center: new google.maps.LatLng(62.2500, 25.7600),
          zoom: 12,
          mapTypeId: google.maps.MapTypeId.ROADMAP       
        };
        
        map = new google.maps.Map(document.getElementById("map_canvas"),
            mapOptions);
          
        var request = new XMLHttpRequest();
        request.onreadystatechange = function() {
            if (request.readyState == 4) 
            {
                var object = JSON.parse(request.responseText);           
                for (var i in object) {
                    drawMarkers(object[i], map);
                }
            }
        };

        // Get json object from server. 
        request.open('GET', '/vuokra_tiedot/get_json', true);
        request.send(null);
	}

    // Create infowindows for markers
    function attachInfoWindow(marker, map, obj) 
    {
        var content = " ";
        content = "<h3>" + obj.osoite.toString() + "</h3> <ul> <li>" + obj.vuokra.toString() + " €/kk </li> <li>" + obj.neliot.toString() + " m2 </li> <li>" + obj.tyyppi.toString() + "</li> <li> <a href=" + obj.linkki.toString() + "> Kohteen tarjoaja </a> </li> </ul>";
     
        google.maps.event.addListener(marker, 'click', function() {
            
            // Close any open infowindows if a new is opened
            if (infowindow) infowindow.close();

            infowindow = new google.maps.InfoWindow({
	            content: content
            });
            infowindow.open(map, marker);
        });   
    }

    google.maps.event.addDomListener(window, 'load', initialize);

    function drawMarkers(obj, map) 
    {
        var location = new google.maps.LatLng(obj.lat, obj.lng);
                
        map.setCenter(location);
        var marker = new google.maps.Marker (
        {
            map: map,
            position: location
            
        });
        markers.push(marker);
        attachInfoWindow(marker, map, obj);
                  
    }     

    // Deletes all markers from the map by removing references to them
    function removeMarkers () {  
        setAllMap(null);
        markers = [];
    }

    // Sets the map on all markers in the array.
    function setAllMap(map) {
      for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
      }
    }
