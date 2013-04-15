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
          
        var location1 = "Tyyppäläntie 8 F 47, Jyväskylä";
        var location2 = "Väinönkatu 40, Jyväskylä";
        var location3 = "Kauppakatu 18, Jyväskylä";
        var location4 = "Nilatie 4, Muurame";
        var location5 = "Humppakuja 2, Jyväskylä";
             
        var locations = new Array(); 

        locations[0] = location1;
        locations[1] = location2;
        locations[2] = location3;
        locations[3] = location4;  
        locations[4] = location5;

        drawMarkers(locations, map);            
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

    function drawMarkers(locations, map) 
    {
        for (var i = 0; i < locations.length; i++)
        {
            var address = locations[i];
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
                    attachInfoWindow(marker, map);
                } 
                else 
                {
                  alert("Geocode was not succesful for the following reason: " + status);
                }  
             });          
        }       
    }

