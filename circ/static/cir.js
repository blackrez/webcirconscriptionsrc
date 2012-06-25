var map = new L.Map('map');

var cloudmadeUrl = 'http://{s}.tile.cloudmade.com/c4f3ac020e354df090f93d9225fbd2b7/997/256/{z}/{x}/{y}.png',
	cloudmadeAttribution = 'Map data &copy; 2012 OpenStreetMap contributors, Imagery &copy; 2012 CloudMade',
	cloudmade = new L.TileLayer(cloudmadeUrl, {maxZoom: 18, attribution: cloudmadeAttribution});

map.setView(new L.LatLng(46.920, 2.593), 5).addLayer(cloudmade);

var cirgeojson = new L.GeoJSON();

cirgeojson.on('featureparse', function(e) {
	/**if (e.properties.status){
		color = 'green';
	}
	else{
		color = 'red';
	}**/
	color = 'green';
	e.layer.bindPopup('circonscriptions' + e.properties.name + '<br />' + e.properties.description);
	e.layer.setStyle({ color:  'black', weight: 1, fill: true, fillColor: color, fillOpacity: 0.85 });
});
$.getJSON(
    "/fr",
    function(geojson) {
    $.each(geojson.features, function(i, feature) {
      cirgeojson.addGeoJSON(feature);
    })
});

map.addLayer(cirgeojson);
/**
var wcirgeojson = new L.GeoJSON();
var last = 0;
var colors = ['003300','003333','003366','003399','FFFF33','0033FF','006600','006633','006666','006699','0066CC','0066FF'];
wcirgeojson.on('featureparse', function(e) {
    if (last != e.properties.cir_num){
        last = e.properties.cir_num;
        
    }
    last = e.properties.cir_num;
	e.layer.bindPopup('Circonscription : ' + e.properties.cir_num + '<br>' +  e.properties.name);
	e.layer.setStyle({ color: 'black', weight: 1, fill: true, fillColor: colors[last-1], fillOpacity: 0.85 });
});
$.getJSON(
    "/etr",
    function(geojson) {
    $.each(geojson.features, function(i, feature) {
      wcirgeojson.addGeoJSON(feature);
    })
});

map.addLayer(wcirgeojson);

//var overlayMaps = {'circonscriptions France' : cirgeojson, "circonscriptions de l'étranger" : wcirgeojson};
//layersControl = new L.Control.Layers(overlayMaps);

//map.addControl(overlayMaps);

/**
map.on('click', onMapClick);

var popup = new L.Popup();

function onMapClick(e) {
	var latlngStr = '(' + e.latlng.lat.toFixed(3) + ', ' + e.latlng.lng.toFixed(3) + ')';

	popup.setLatLng(e.latlng);
	popup.setContent("You clicked the map at " + latlngStr);
	map.openPopup(popup);
}**/