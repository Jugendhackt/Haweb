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
    xmlHttp.open( "GET", url, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}


//Tabs

var content = JSON.parse(getData("/cgi-bin/content.py?lang=de"));


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
  console.log(content.Content[tabid]);
  contentpage.innerHTML = content.Content[tabid];
}
console.log(content.Tabs);
console.log(content.Content);
for (var tab in content.Tabs) {
    addtab(tab,content.Tabs[tab]);
}

changetab("tab1")
