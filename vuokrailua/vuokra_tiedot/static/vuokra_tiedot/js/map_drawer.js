    var geocoder;
    var map;   
    var infowindow;
    function initialize() {	

        //Center the map to desired location        
        var mapOptions = {
          center: new google.maps.LatLng(62.2500, 25.7600),
          zoom: 12,
          mapTypeId: google.maps.MapTypeId.ROADMAP       
        };
        
        map = new google.maps.Map(document.getElementById("map-canvas"),
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
        content = "<h3>" + obj.osoite.toString() + "</h3> <ul> <li>" + obj.vuokra.toString() + " €/kk </li> <li>" + obj.neliot.toString() + " m2 </li> <li>" + obj.tyyppi.toString() + "</li></ul>";
     
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
        attachInfoWindow(marker, map, obj);
                  
    }       
