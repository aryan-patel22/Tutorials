//JavaScript for Tutorial

var button = document.querySelector("button");
var box = document.getElementById("changeMe");


function changeColor(){ //Can also say button.onclick = if you don't reference in html
    if(box.style.background == 'red'){
        box.style.background = "blue";
    }

    else{
        box.style.background = "red";
    }
}