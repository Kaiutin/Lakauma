    var geocoder;
    var map;   
    var marker;
    function initialize() {	
        
        var mapOptions = {
          center: new google.maps.LatLng(62.2500, 25.7600),
          zoom: 12,
          mapTypeId: google.maps.MapTypeId.ROADMAP       
        };

        map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);

        geocoder = new google.maps.Geocoder();
          
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
        request.open('GET', '/vuokra_tiedot/get_json', true);
        request.send(null);      
	}

    function attachInfoWindow(marker, map) 
    {
        content = "<h1>uliuli</h1>";
        
        var infowindow = new google.maps.InfoWindow({
	        content: content
        });  

        google.maps.event.addListener(marker, 'click', function() {
	        infowindow.open(map, marker);
        });   
    }

    google.maps.event.addDomListener(window, 'load', initialize);

    function drawMarkers(obj, map) 
    {
        alert(obj.osoite);
        var address = obj.osoite.toString() + "Jyväskylä";
        geocoder.geocode({'address': address}, function(results, status)
        {
            if (status == google.maps.GeocoderStatus.OK) 
            {
                map.setCenter(results[0].geometry.location);
                marker = new google.maps.Marker (
                {
                    map: map,
                    position: results[0].geometry.location
                });
                //attachInfoWindow(marker, map);
            } 
            else 
            {
              alert("Geocode was not succesful for the following reason: " + status);
            }  
         });                
    }       
