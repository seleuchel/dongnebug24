function ReadLocation(){
    return fetch('http://168.131.153.40:8000/location/', { 
    method: 'GET'
    })
    .then((response) => response.json()) 
    .catch((error) => {
       console.error(error);
    });
}

function CreateLocation(data1){ //위치정보 json으로 받기
  //data1={"timestamp":1565450043041,"mocked":true,"coords":{"altitude":46.02571105957031,"heading":0,"longitude":127.15868196733577,"latitude":37.49609393127839,"speed":0.42205262184143066,"accuracy":1.3326040506362915}}
  data2=data1['coords']
  timestamp=data1['timestamp']
  mocked=data1['mocked']
  altitude=data2['altitude']
  heading=data2['heading']
  longitude=data2['longitude']
  latitude=data2['latitude']
  speed=data2['speed']
  accuracy=data2['accuracy']

  fetch('http://168.131.153.40:8000/location/', {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({  
    'timestamp': timestamp,
    'mocked': mocked,
    'altitude': altitude,
    'heading': heading,
    'longitude': longitude,
    'latitude': latitude,
    'speed': speed,
    'accuracy': accuracy,
  })
})
}

function UpdateLocation(){
  data1={"timestamp":1565450043041,"mocked":true,"coords":{"altitude":46.02571105957031,"heading":0,"longitude":127.15868196733577,"latitude":37.49609393127839,"speed":0.42205262184143066,"accuracy":1.3326040506362915}}
  data2=data1['coords']
  timestamp=data1['timestamp']
  mocked=data1['mocked']
  altitude=data2['altitude']
  heading=data2['heading']
  longitude=data2['longitude']
  latitude=data2['latitude']
  speed=data2['speed']
  accuracy=data2['accuracy']

  fetch('http://168.131.153.40:8000/location/', { // URL인자값 더하기
  method: 'PUT',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({  
    'timestamp': timestamp,
    'mocked': mocked,
    'altitude': altitude,
    'heading': heading,
    'longitude': longitude,
    'latitude': latitude,
    'speed': speed,
    'accuracy': accuracy,
  })
})
}

function DeleteLocation(){
  fetch('http://168.131.153.40:8000/location/', { // URL인자값 더하기
  method: 'DELETE',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  }
})
}

export { ReadLocation, CreateLocation, UpdateLocation, DeleteLocation };
