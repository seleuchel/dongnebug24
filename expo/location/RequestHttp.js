function ReadLocation(){
    return fetch('http://168.131.153.40:8000/location/7/', {
    method: 'GET'
    })
    .then((response) => response.json())
    .catch((error) => {
       console.error(error);
    });
}

//sumin-edit : POST
//http://168.131.153.40:8000/api/locations/
function CreateLocation(latitude, longitude){ //위치정보 json으로 받기
  fetch('http://168.131.151.165/', {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    'latitude': latitude,
    'longitude': longitude,
  })
})
}


//sumin-edit : PUT
function UpdateLocation(token,latitude, longitude){
  //귀주 : http://168.131.153.40:8000/api/locations/
  //세옥 : http://168.131.151.162:8000/api/locations/1/
  fetch('http://168.131.153.40:8000/api/locations/73/', { // URL인자값 더하기
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
