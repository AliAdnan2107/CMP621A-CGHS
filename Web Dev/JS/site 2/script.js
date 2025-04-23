console.log("Hello World");

function myFunction() {
    var mainnum=document.getElementById("num").value;

    if (mainnum>=10) {
        document.getElementById("main").innerHTML = "That's huge!!";
        document.getElementById("main").style.color = "red";
    }
    else {
        document.getElementById("main").innerHTML = "That's small!!";
        document.getElementById("main").style.color = "blue";
    }
}