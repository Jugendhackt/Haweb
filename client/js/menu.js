var tabs;

function mobliebutton(y) {
    var x = document.getElementById("myTopnav");
    y.classList.toggle("change");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}
  

function changelanguage(lang){
  setCookie("lang",lang,1000);
  //tabs = JSON.parse(getData("localhost:8000/cgi-bin/tabs.py?lang="+lang));
  cleartabs();
  for (var tab in tabs.Tabs) {
    addtab(tab, tabs.Tabs[tab]);
  }
  changetab("tab1");
}
tabidlist = [];
//Tabs
function cleartabs() {
  var tablist = document.getElementById("left");
  tablist.innerHTML = "";
  setCookie("lang",slang,100);
}

function addtab(tabid, tabname) {
  var tablist = document.getElementById('left');
  var newtab = document.createElement("a");
  tabidlist.push(tabid);
  newtab.href = "javascript:void(0)";
  if (newtab.addEventListener) { // all browsers except IE before version 9
    newtab.addEventListener("mouseup", function () {
      changetab(tabid);
    }, false);
  } else {
    console.log("Your Browser don't support addEventListener");
  }
  newtab.innerHTML = tabname;
  newtab.id = tabid;


  tablist.appendChild(newtab);

}


function changetab(tabid) {
  for (var oldtab in tabs.Tabs) {
    document.getElementById(oldtab).className = '';
  }
  document.getElementById(tabid).className = 'active';
  window.history.pushState(tabs.Tabs[tabid], 'Hausaufgaben Webseite', '#' + tabid);

  var contentpage = document.getElementById('content');
}
function buildtabs() {
    for (var tab in tabs.Tabs) {
        addtab(tab, tabs.Tabs[tab]);
      }
    changetab("tab1");
}