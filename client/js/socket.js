window.addEventListener("load", connect());
var socket;

 function connect() {
     // create websocket instance
     socket =  new WebSocket("ws://" + location.hostname + ":8888/ws");
     // add event listener reacting when message is received
     socket.onmessage = function (event) {
         var output = document.getElementById("chatcontent");
         // put text into our output div
         console.log(event.data);
         var newmessage = JSON.parse(event.data);
         console.log(newmessage);
         if(newmessage.type == "chat"){
             if(newmessage.message.user == "SERVER"){
                malert("Chat wurde gelöscht");
                output.innerHTML = "";
             }
            var newmessage_html = document.createElement('div');
            newmessage_html.innerHTML = '<div class="chatcontent"><div class="container"><span>' + newmessage.message.user + '</span><p>' + newmessage.message.text + '</p><span class="time">' + newmessage.message.time + '</span></div>';
            output.appendChild(newmessage_html);
         }if(newmessage.type == "tabs"){
             tabs = newmessage;
             cleartabs();
             buildtabs();
         }
     };
     //var formchat = document.getElementById ("chatsend");
     //var input = document.getElementById("input");
     socket.onclose = function (e) {
         console.log("Connection closed");
         console.log("Try to reconnect");
         connect();
     };
     //formchat.addEventListener("submit", function (e) {
         // on forms submission send input to our server
         //input_text = input.value;
         //socket.send(input_text);
         //e.preventDefault();
         //input.value = "";
         //return false;

     //});
     console.log("Connected to Websocket");
 }