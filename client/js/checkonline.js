var offi ;
function offFunction() {
    offi = setInterval(2000,function (){
        malert("Du bist Offline");
    })
}

function onFunction() {
    clearInterval(offi)
    malert("Du bist wieder Online");
}
window.addEventListener("online",onFunction())
window.addEventListener("offline",offFunction())