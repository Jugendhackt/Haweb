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

function includeHTML() {
  var z, i, elmnt, file, xhttp;
  /*loop through a collection of all HTML elements:*/
  z = document.getElementsByTagName("*");
  for (i = 0; i < z.length; i++) {
    elmnt = z[i];
    /*search for elements with a certain atrribute:*/
    file = elmnt.getAttribute("html-scr");
    if (file) {
      /*make an HTTP request using the attribute value as the file name:*/
      xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
          if (this.status == 200) {elmnt.innerHTML = this.responseText;}
          if (this.status == 404) {elmnt.innerHTML = "Page not found.";}
          /*remove the attribute, and call this function once more:*/
          elmnt.removeAttribute("html-scr");
          includeHTML();
        }
      }
      xhttp.open("GET", file, true);
      xhttp.send();
      /*exit the function:*/
      return;
    }
  }
};

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

function httprequest_get(url) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", url, true );
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4) {
      if (xmlHttp.status == 200) {
        console.log(xmlHttp);
      }

    }
  }
  xmlHttp.send();
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
  window.history.pushState(content.Tabs[tabid], 'Hausaufgaben Webseite', '#'+content.Tabs[tabid]);

  var contentpage = document.getElementById('content');
}
for (var tab in content.Tabs) {
    addtab(tab,content.Tabs[tab]);
}

changetab("tab1")
