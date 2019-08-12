function RequestHttp(){
    return fetch('https://facebook.github.io/react-native/movies.json', { //여기다 요청할 url넣으면
    method: 'GET' //겟방식으로 보내는데
    })
    .then((response) => response.json()) //리스폰스가 올때까지 기다렸다가 오면 json으로 바꾸고
    .catch((error) => { //에러뜨면 에러표시해주고(꼭넣어줘야한다고함)
       console.error(error);
    });
}

function SendData(data1){
   fetch('http://168.131.151.165/p2p/socket', {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    location: 'data1',
  })
})
}
export { RequestHttp, SendData };
