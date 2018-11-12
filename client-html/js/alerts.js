// This is an special build get the newest at https://github.com/antonk123/haweb
function malert(text) { // Alert in the Bottom of the Page
    // Get the alert DIV
    var alertbox = document.getElementById("alerts");
    var alert = document.createElement('div');
    // Add the "show" class to DIV
    alert.className = "show";
    alert.id = "snackbar";
    alert.innerHTML = text;
    alertbox.appendChild(alert);
    // After 3 seconds, remove the show class from DIV
    setTimeout(function () {
        alert.className = alert.className.replace("show", "");
    }, 3000);
}

function notifiy(message) { // Notification to the system
    // Let's check if the browser supports notifications
    if (!("Notification" in window)) {
        console.log("This Browser can't Display Notification");

    }

    // Let's check whether notification permissions have already been granted
    else if (Notification.permission === "granted") {
        // If it's okay let's create a notification
        var notification = new Notification(message);
    }

    // Otherwise, we need to ask the user for permission
    else if (Notification.permission !== "denied") {
        Notification.requestPermission(function (permission) {
            // If the user accepts, let's create a notification
            if (permission === "granted") {
                var notification = new Notification(message);
            }
        });
    }

    // At last, if the user has denied notifications, and you 
    // want to be respectful there is no need to bother them any more.
}
function modal(text){
    text = JSON.parse(text);
    
}