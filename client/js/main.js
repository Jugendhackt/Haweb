//Tabs
var tablist = ["Home","Fachwissen","Hausaufgaben","Chat"]

function addtab(tab) {
  var tabs = document.getElementById('myTopnav');
  var newtab = document.createElement("a");

  newtab.href = "javascript:void(0)";
  if (button.addEventListener) {  // all browsers except IE before version 9
      button.addEventListener ("mouseup", function () {OnButtonUp (button)}, false);
  }
  else {
    if (button.attachEvent) {   // IE before version 9
       button.attachEvent ("onmouseup", function () {OnButtonUp (button)});
     }
   }
  newtab.innerHTML = tab;

  tabs.appendChild(newtab);



}

function tabcontent(tab,content) {

}

function changetab(tab) {
  tab.className = 'active'
}


for (var tab in tablist) {
    addtab(tablist[tab]);
}
