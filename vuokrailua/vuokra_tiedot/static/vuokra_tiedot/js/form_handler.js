// This file is part of Loukku, an application to display available rental apartments on Google Maps map.
// Copyright (C) 2013  Anton Laurila, Jari-Matti Kankaanpää, Samuel Uusi-Mäkelä
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as
// published by the Free Software Foundation, either version 3 of the
// License, or (at your option) any later version.
// For more information, please refer to LICENCE file found in /Lakauma,
// or <http://www.gnu.org/licenses/> and GNU Affero General Public License


function sendSearchData() {
    removeMarkers();
    var vuokra_min = $( "#slider-range-vuokra" ).slider( "values", 0 );
    var vuokra_max = $( "#slider-range-vuokra" ).slider( "values", 1 );
    var neliot_min = $( "#slider-range-neliot" ).slider( "values", 0 );
    var neliot_max = $( "#slider-range-neliot" ).slider( "values", 1 );        

    var url = "/vuokra_tiedot/get_json?vuokra_min=" + vuokra_min + "&vuokra_max=" + vuokra_max + "&neliot_min=" + neliot_min + "&neliot_max=" + neliot_max;

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
