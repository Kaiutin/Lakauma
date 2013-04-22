function sendSearchData() {
    var vuokra_min = document.getElementById('vuokra_min').value;
    var vuokra_max = document.getElementById('vuokra_max').value;
    var neliot_min = document.getElementById('neliot_min').value;
    var neliot_max = document.getElementById('neliot_max').value;

    if ( document.getElementById('tyyppi1h').checked) {
        var tyyppi1h = document.getElementById('tyyppi1h').value;
    }
    
    if ( document.getElementById('tyyppi2h').checked) {
        var tyyppi2h = document.getElementById('tyyppi2h').value;   
    }

    if ( document.getElementById('tyyppi3h').checked) {
        var tyyppi3h = document.getElementById('tyyppi3h').value;
    }

    if ( document.getElementById('tyyppi4h').checked) {
        var tyyppi4h = document.getElementById('tyyppi4h').value;
    }        

    /*alert(vuokra_min + vuokra_max + neliot_min + neliot_max + tyyppi1h + tyyppi2h + tyyppi3h + tyyppi4h);*/

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
    //alert(window.location.href);
}
