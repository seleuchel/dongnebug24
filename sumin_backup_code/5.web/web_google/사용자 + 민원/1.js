<!-- connet to read json server and set markup in google map -->
<!DOCTYPE html>
<html>
  <head>
    <style>
       /* Set the size of the div element that contains the map */
      #map {
        height: 400px;  /* The height is 400 pixels */
        width: 50%;  /* The width is the width of the web page */
       }
    </style>
  </head>
  <body>

    <!--The div element for the map -->
    <div id="map"></div>
    <script>
      let url = 'http://168.131.153.40:8000/api/locations/1/';
      let bukurl = 'https://storage.googleapis.com/maps-devrel/google.json';

      var leti = '';
      var loni = '';

      var M = [];
      var test= '';
      var buks = [];

// Initialize and add the map
async function initMap() {
  // The location of Uluru
  var uluru = {lat: -25.793279, lng: 124.710349};
  //var demon = ;
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 5, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});
  //test = new google.maps.Marker({position:{lat:-28.57, lng :119.22 }, map: map});

 setInterval(async function (){
   deleteMarkers();
   //!
   fetch(url, { // URL인자값 더하기
  method: 'GET'
  }).then(
       function(response) {
         if (response.status !== 200) {
           console.log('Looks like there was a problem. Status Code: ' +
             response.status);
           return;
         }

         // Examine the text in the response
         response.json().then(function(data) {
           console.log(data);

            lati = parseFloat(data.latitude);
            lngi = parseFloat(data.longitude);
            var pos = {lat:lati, lng:lngi};
             console.log(pos);

            test = new google.maps.Marker({position: pos, map: map});
            M.push(test);

         });
       }
     )
     .catch(function(err) {
       console.log('Fetch Error :-S', err);
     });


     //// bukss
     fetch(bukurl, { // URL인자값 더하기
    method: 'GET'
    }).then(
         function(response) {
           if (response.status !== 200) {
             console.log('Looks like there was a problem. Status Code: ' +
               response.status);
             return;
           }

           // Examine the text in the response
           response.json().then(function(data) {

             console.log(data.features[0].geometry.coordinates[0]);
             buks = data.features[0].geometry.coordinates[0];
             var num = buks.length;
             for(var i = 0 ; i < num; i++){
               var lats = parseFloat(buks[i][1]);
               var lngs = parseFloat(buks[i][0]);
               var bukpos = {lat:lats, lng:lngs};
              //console.log('thisis ',bukpos);
              console.log('here',buks[0][i]);

               var bukmark = new google.maps.Marker({
                 position: bukpos,
                 map: map,
               });
               M.push(bukmark);
             }


           });
         }
       )
       .catch(function(err) {
         console.log('Fetch Error :-S', err);
       });


 }, 1000);



}

function clearMarkers() {
  setMapOnAll(null);
}

function deleteMarkers() {
  for (var i = 0; i < M.length; i++) {
      M[i].setMap(null);
  }
  M = [];
}


    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDA43UhrvuE1LtRYbHYwbfoBJ3UPLLPbGc&callback=initMap">
    </script>
  </body>
</html>

//#막 깜박깜박거림
//#이렇게하면 서버에서 계산된 민원 목록을 (위치 정보와 함께 배열로 받아야함)
//#{}의 배열 (2차원 배열)
//#민원 이름도 받아오기.
