    function malert(text) {
        // Get the snackbar DIV
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