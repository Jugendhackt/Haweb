var formchat = document.getElementById ("chatsend");
var input = document.getElementById("input");
var output = document.getElementById("chatcontent");
var active = false;
function togglechat(mode){
    if(mode == true & active == false){
        malert("Verbunden");
    }else if (mode == false & active == true){
        malert("Getrennt");
    }
    active = mode;
}
function getMessage(json){
    var newmessage_html = document.createElement('div');
    notifiy(json.message.user + " | " +json.message.text);
    newmessage_html.innerHTML = '<div class="chatcontent"><div class="container"><span>' + json.message.user + '</span><p>' + json.message.text + '</p><span class="time">' + json.message.time + '</span></div>';
    output.appendChild(newmessage_html);  
}
formchat.addEventListener("submit", function (e) {
    // on forms submission send input to our server
    if (active == true) {
        input_text = input.value;
        sendsocket("chat",input_text);
        e.preventDefault();
        input.value = "";
        let file = document.getElementById("filebut").files[0];
        let formData = new FormData();
        formData.append("file1", file);
        let xhr = new XMLHttpRequest();
        xhr.open("POST", '/upload');
        xhr.send(formData);

    }else{
        malert("Du bist im Moment nicht mit dem Server verbunden");
    }

    return false;

});