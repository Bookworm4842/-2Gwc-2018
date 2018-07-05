var ourLoc;
var view;
var map;

function init() {
	// Initalize things here
	ourLoc = ol.proj.fromLonLat([41.043316, 28.862457]);

	view = new ol.View({
		center: ourLoc,
		zoom: 6
	});

	map = new ol.Map({
		target: 'map',
		layers: [
		  new ol.layer.Tile({
		    source: new ol.source.OSM()
		  })
		],
		// Note from the View Animation website:
		// Improve user experience by loading tiles while animating. Will make
		// animations stutter on mobile or slow devices.
		loadTilesWhileAnimating: true,
		view: view
	});
}

function panHome() {
	view.animate({
		center: ourLoc, // "Home" Location
		duration: 2000  // Two seconds
	});
}

function panToCountry() {
	var countryName = document.getElementById("country-name").value;


	var query = "https://restcountries.eu/rest/v2/name/"+countryName
	// Step 3: Let's do some error checks and input modification
	// Explain: When we make requests in a browser, we want to
	// replace spaces with %20.
	query = query.replace(/ /g, "%20")
	alert(query);

	// Step 1: Let's start by making an HTTP GET request:
	var countryRequest = new XMLHttpRequest();
	countryRequest.open('GET', query, false);

	// Step 2: Send the request and see the output:
	countryRequest.send();

	alert("Ready State " + countryRequest.readyState);
	alert("Status " + countryRequest.status);
	alert("Response" + countryRequest.responseText);

	if(countryRequest.readyState != 4 || countryRequest.status != 200 || countryRequest.responseText === "") {
	 	window.console.error("Request had an error!");
	 	return;
	}

	var countryInformation = JSON.parse(countryRequest.responseText);

	// Step 3: We have to figure out where the information is based
	// on the JSON we got back. This can be very tricky sometimes.
	// For instance, this JSON returns an ARRAY of information.
	// Inside the FIRST array element, we have our latlng variable.
	// This variable has the information we need!
	var lat = countryInformation[0].latlng[0];
	var lon = countryInformation[0].latlng[1];

	// Note: If you run into an error like the map
	// disappearing, check that you have your
	// longtidue and latitude variables mapped
	// to the right indexes. Lon is index 1,
	// lat is index 0.
	window.console.log(countryName + ": lon " + lon + " & lat " + lat);

	var location = ol.proj.fromLonLat([lon, lat]);

	// Note: If you run into an error like window
	// not loading, check that you declared VAR
	// before the location variable.

	view.animate({
		center: location, // Location
		duration: 2000  // Two seconds
	});
}

window.onload = init;
