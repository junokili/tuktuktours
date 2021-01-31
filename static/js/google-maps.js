// code validated through JSHint: https://jshint.com/
// google maps API for office location
function initMap() {
            var map = new google.maps.Map(document.getElementById("location-map"),{
                zoom: 12,
                center: {
                    lat: -7.79,
                    lng: 110.365,
                }
            });    
        var labels = "ABCDEFGHIJKLMNOPQPRSTUVWXYZ";
        var locations = [
            {lat: -7.79160, lng: 110.36371},
        ];
        var markers = locations.map(function(location, i){
            return new google.maps.Marker({
                position: location,
                label: labels[i % labels.length]
            });
            }); 
            var markerCluster = new MarkerClusterer(map, markers,
            {imagePath: "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m"});
        }