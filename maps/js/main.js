$(document).ready(function(){
	document.getElementById('mapid').style.width = window.innerWidth;
	document.getElementById('mapid').style.height = window.innerHeight;
	var florida_map = L.map('mapid').setView([27.994402, -81.760254], 7)
	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    	maxZoom: 18,
    	id: 'mapbox.streets',
    	accessToken: 'pk.eyJ1IjoibmJvZ2RhIiwiYSI6ImNqOHE1NzY1ajBlZG8zM3FvMXJ6ODFueWEifQ.qLyz3rHrpKmIL8wg3FTaig'
	}).addTo(florida_map);
});

