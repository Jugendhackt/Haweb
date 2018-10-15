var settingsstatus = false;

var slangs = document.getElementById('slang');
var slang = slangs.options[slangs.selectedIndex].value;
slangs.value = getCookie("lang");

function togglesettigs(esc) {
    if (settingsstatus == false && !esc) {
        console.log("Open Settings");

        document.getElementById('settings').style.display = 'block';
        settingsstatus = true;
    } else if (settingsstatus == true || esc) {
        console.log("Closing Settings");

        document.getElementById('settings').style.display = 'none';
        settingsstatus = false;
    }
}

function savesettings() {
    console.log("Save Settings");
    changelanguage(slang);
    togglesettigs();
}
// Get the modal
var modal = document.getElementById('settings');

// When the user clicks anywhere outside of the modal, close it
window.onmouseup = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};
document.onkeydown = function (evt) {
    evt = evt || window.event;
    if (evt.keyCode == 27) {
        togglesettigs(true);
    }
};