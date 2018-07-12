var close = document.getElementsByClassName("closebtn");
var i;

for (i = 0; i < close.length; i++) {
    close[i].onclick = function(){
        var div = this.parentElement;
        div.style.opacity = "0";
        setTimeout(function(){ div.style.display = "none"; }, 600);
    }
}

function malert(type,text) {
  //Type: danger,success,info,warning
  console.log("Test 1");
  var talert =  document.createElement('div');
  div.className = "alert" + type
  talert.innerHTML = "<span class='closebtn'>&times;</span><strong>"+ type.toUpperCase() +"! </stong>" + text;
  console.log(document.getElementById('alerts').innerHtml);
  document.getElementById('alerts').appendChild(talert);
  console.log("Test 3");

}


function addRow() {
    var div = document.createElement('div');

    div.className = 'row';

    div.innerHTML =
        '<input type="text" name="name" value="" />\
        <input type="text" name="value" value="" />\
        <label> <input type="checkbox" name="check" value="1" /> Checked? </label>\
        <input type="button" value="-" onclick="removeRow(this)">';

    document.getElementById('content').appendChild(div);
}

function removeRow(input) {
    document.getElementById('content').removeChild(input.parentNode);
}
