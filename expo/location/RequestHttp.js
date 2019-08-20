function ReadLocation(){
    return fetch('http://168.131.153.40:8000/location/7/', {
    method: 'GET'
    })
    .then((response) => response.json())
    .catch((error) => {
       console.error('[ERR] something error in ReadLocation'); //error -> "[ERR] something error in ReadLocation"
    });
}

//sumin-edit : POST
function CreateLocation(token,latitude, longitude){ //위치정보 json으로 받기
  fetch('http://168.131.151.162:8000/api/locations/', {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    'token' : '5FaxCb8Aodo',
    'latitude': latitude,
    'longitude': longitude,
  })
})
}

//sumin-edit : PUT
function UpdateLocation(token,latitude, longitude){
  //귀주 : http://168.131.153.40:8000/api/locations/
  //세옥 : http://168.131.151.162:8000/api/locations/1/
  fetch('http://168.131.151.162:8000/api/locations/1/', { // URL인자값 더하기
  method: 'PUT',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    'token' : token,
    'latitude': latitude,
    'longitude': longitude,
  })
})
}

function DeleteLocation(){
  fetch('http://168.131.151.162:8000/api/locations/', { // URL인자값 더하기
  method: 'DELETE',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  }
})
}

export { ReadLocation, CreateLocation, UpdateLocation, DeleteLocation };
