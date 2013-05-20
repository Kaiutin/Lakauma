// This file is part of Loukku, an application to display available rental apartments on Google Maps map.
// Copyright (C) 2013  Anton Laurila, Jari-Matti Kankaanpää, Samuel Uusi-Mäkelä
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as
// published by the Free Software Foundation, either version 3 of the
// License, or (at your option) any later version.
// For more information, please refer to LICENCE file found in /Lakauma,
// or <http://www.gnu.org/licenses/> and GNU Affero General Public License


$(function() {
    $( "#slider-range-vuokra" ).slider({
      range: true,
      min: 0,
      max: 1500,
      values: [ 0, 1500 ],
      slide: function( event, ui ) {
        $( "#vuokra" ).val( "€" + ui.values[ 0 ] + " - €" + ui.values[ 1 ] );
      }
    });
    $( "#vuokra" ).val( "€" + $( "#slider-range-vuokra" ).slider( "values", 0 ) +
      " - €" + $( "#slider-range-vuokra" ).slider( "values", 1 ) ); 
  });

$(function() {
    $( "#slider-range-neliot" ).slider({
      range: true,
      min: 1,
      max: 150,
      values: [ 1  , 150 ],
      slide: function( event, ui ) {
        $( "#neliot" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#neliot" ).val($( "#slider-range-neliot" ).slider( "values", 0 ) +
      " - " + $( "#slider-range-neliot" ).slider( "values", 1 ) );
  });
