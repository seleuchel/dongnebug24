var ws = new WebSocket('http://168.131.151.165/p2p/jsonserver/bye.html');

ws.onopen = function(){
  ws.send('seleuchel! hello!');
};

ws.onmessage = function(e){
  console.log(e.data);
};

ws.onerror = function(e){
  console.log(e.message);
};

ws.onclose = function(e){
  console.log(e.code, e.reason);
};
