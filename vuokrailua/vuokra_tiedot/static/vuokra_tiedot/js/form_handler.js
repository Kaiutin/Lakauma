function sendSearchData() {
    removeMarkers();
    var vuokra_min = $( "#slider-range-vuokra" ).slider( "values", 0 );
    var vuokra_max = $( "#slider-range-vuokra" ).slider( "values", 1 );
    var neliot_min = $( "#slider-range-neliot" ).slider( "values", 0 );
    var neliot_max = $( "#slider-range-neliot" ).slider( "values", 1 );        

    var url = "/vuokra_tiedot/get_json?vuokra_min=" + vuokra_min + "&vuokra_max=" + vuokra_max + "&neliot_min=" + neliot_min + "&neliot_max=" + neliot_max;
    alert(url);

    var request = new XMLHttpRequest();
    request.onreadystatechange = function() {
            if (request.readyState == 4) 
            {
                var object = JSON.parse(request.responseText);           
                for (var i in object) {
                    drawMarkers(object[i], map);
                };
            };
        };

    // Get json object from server. 
    request.open('GET', url, true);
    request.send(null);       
}   
