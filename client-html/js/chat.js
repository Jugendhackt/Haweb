var formchat = document.getElementById ("chatsend");
var input = document.getElementById("input");
var output = document.getElementById("chatcontent");
formchat.addEventListener("submit", function (e) {
    // on forms submission send input to our server
    input_text = input.value;
    sendsocket("chat",input_text);
    e.preventDefault();
    input.value = "";
    return false;
});

function getMessage(json){
    if (json.message.user == "SERVER") {
        malert("Chat wurde gelöscht");
        output.innerHTML = "";
    }
    var newmessage_html = document.createElement('div');
    notifiy(json.message.user + " | " +json.message.text);
    json.innerHTML = '<div class="chatcontent"><div class="container"><span>' + json.message.user + '</span><p>' + json.message.text + '</p><span class="time">' + json.message.time + '</span></div>';
    output.appendChild(newmessage_html);   
}