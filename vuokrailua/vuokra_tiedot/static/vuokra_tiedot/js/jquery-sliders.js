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
