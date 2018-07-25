//Cookies
function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
function checkCookie(cname) {
    var cookiec = getCookie(cname);
    if (cookiec != "") {
      return true;
    } else {
      return false;
    }
}
//Get and post

function postData(url,data) {
  var XHR = new XMLHttpRequest();
  var urlEncodedData = "";
  var urlEncodedDataPairs = [];
  var name;

  // Turn the data object into an array of URL-encoded key/value pairs.
  for(name in data) {
    urlEncodedDataPairs.push(encodeURIComponent(name) + '=' + encodeURIComponent(data[name]));
  }

  // Combine the pairs into a single string and replace all %-encoded spaces to
  // the '+' character; matches the behaviour of browser form submissions.
  urlEncodedData = urlEncodedDataPairs.join('&').replace(/%20/g, '+');

  // Define what happens on successful data submission
  XHR.addEventListener('load', function(event) {
    alert('Yeah! Data sent and response loaded.');
  });

  // Define what happens in case of error
  XHR.addEventListener('error', function(event) {
    alert('Oops! Something goes wrong.');
  });

  // Set up our request
  XHR.open('POST', url);

  // Add the required HTTP header for form data POST requests
  XHR.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

  // Finally, send our data.
  XHR.send(urlEncodedData);

}
function getData(url) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false );
    xmlHttp.send();
    return xmlHttp.responseText;
}


var content = JSON.parse(getData("/cgi-bin/tabs.py?lang=en"));

//Tabs


function addtab(tabid,tabname) {
  var content = document.getElementById('myTopnav');
  var newtab = document.createElement("a");

  newtab.href = "javascript:void(0)";
  if (newtab.addEventListener) {  // all browsers except IE before version 9
      newtab.addEventListener ("mouseup", function () {changetab(tabid)}, false);
  }
  else {
    console.log("Your Browser don't support addEventListener");
   }
  newtab.innerHTML = tabname;
  newtab.id = tabid ;


  content.appendChild(newtab);



}


function changetab(tabid) {
  for (var oldtab in content.Tabs) {
      document.getElementById(oldtab).className = '';
  }
  document.getElementById(tabid).className = 'active';
  var contentpage = document.getElementById('content');
  contentpage.innerHTML = content.Content[tabid];
}
for (var tab in content.Tabs) {
    addtab(tab,content.Tabs[tab]);
}

changetab("tab1")
