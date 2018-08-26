 window.addEventListener("load", function() {
    // create websocket instance
    var mySocket = new WebSocket("ws://"+location.hostname+":8888/ws");
    // add event listener reacting when message is received
    mySocket.onmessage = function (event) {
        var output = document.getElementById("chatcontent");
        // put text into our output div
        var newmessage = JSON.parse(event.data);
        console.log(newmessage);
        
        var newmessage_html = document.createElement('div');
        newmessage_html.innerHTML = '<div class="chatcontent"><div class="container"><span>'+newmessage.message.user+'</span><p>'+newmessage.message.text+'</p><span class="time">'+newmessage.message.time+'</span></div>';
        output.appendChild(newmessage_html);
    };
    var formchat = document.getElementById("chatsend");
    var input = document.getElementById("input"); 
    formchat.addEventListener("submit", function (e) {
        // on forms submission send input to our server
        input_text = input.value;
        mySocket.send(input_text);
        e.preventDefault();
        input.value = "";
        return false;
 });
});