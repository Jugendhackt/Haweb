function offFunction() {
    malert("Du bist Offline");
}

function onFunction() {
    malert("Du bist wieder Online");
}

window.addEventListener('online',  onFunction());
window.addEventListener('offline', offFunction());