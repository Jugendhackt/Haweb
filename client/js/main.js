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
