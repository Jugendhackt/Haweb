function opensettings() {
  document.getElementById('settings').style.display='block'
}
function closesettings() {
  document.getElementById('settings').style.display='none'
}
// Get the modal
var modal = document.getElementById('settings');

// When the user clicks anywhere outside of the modal, close it
window.onmouseup = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
document.onkeydown = function(evt) {
    evt = evt || window.event;
    if (evt.keyCode == 27) {
        closesettings();
    }
};
