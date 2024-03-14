var marker;
var map;

function initMap() {

    var myLatLng = { lat: 43.2269, lng: 15.3832 };

    map = new google.maps.Map(document.getElementById('map'), {
        center: myLatLng,
        zoom: 15
    });

    marker = new google.maps.Marker({
        map: map,
        position: myLatLng,
        title: 'Moje auto'
    });
}

function updateMarker(lat, long) {
    var newLatLng = new google.maps.LatLng(lat, long);
    marker.setPosition(newLatLng);
    map.panTo(newLatLng);
}
