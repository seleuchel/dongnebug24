<html>
  <body>
  <div id="demo">
  <button type="button" onclick="loadDoc()"> Change content</button>
    <script>
      function loadDoc(){
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function(){
          if (this.readystate == 4 && this.status == 200){
            document.getElementById("demo").innerHTML =
            this.responseText;
          }
        };
        xhttp.open("GET", "./client.js", true);
        xhttp.send();
      }
    </script>
  </body>
</html>
