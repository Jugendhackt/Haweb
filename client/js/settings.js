var settingsstatus = false
function togglesettigs(esc) {
  if(settingsstatus == false && !esc){
    document.getElementById('settings').style.display='block';
    settingsstatus = true;
  }else if (settingsstatus == true || esc) {
    document.getElementById('settings').style.display='none';
    settingsstatus = false;
  }
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
        togglesettigs(true);
    }
};
