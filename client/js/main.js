//Get and post

function sendData(url,data) {
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


//Tabs
var tablist = ["Home","Fachwissen","Hausaufgaben","Chat"]

function addtab(tab) {
  var tabs = document.getElementById('myTopnav');
  var newtab = document.createElement("a");

  newtab.href = "javascript:void(0)";
  if (newtab.addEventListener) {  // all browsers except IE before version 9
      newtab.addEventListener ("mouseup", function () {changetab(tab)}, false);
  }
  else {
    console.log("Your Browser don't support addEventListener");
   }
  newtab.innerHTML = tab;
  newtab.id = tab ;


  tabs.appendChild(newtab);



}

function tabcontent(tab,content) {

}


for (var tab in tablist) {
    addtab(tablist[tab]);
}

function changetab(tab) {
  for (var oldtab in tablist) {
      document.getElementById(tablist[oldtab]).className = '';
  }
  gettab = document.getElementById(tab);
  gettab.className = 'active';
  var content = document.getElementById('content')
}
changetab(tablist[0])
