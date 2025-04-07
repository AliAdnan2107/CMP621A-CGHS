console.log("What","Do","Commas","Do?");
console.log("Does",       "Space", "Make     ", "A", "Difference?");
console.log("What about " + "addition?")
console.log("And how about our beautiful integers like", 4)
alert("Hey man you wanna go ahead and hit the ok right there so you can see what happens?")

function ButtonAlert () {
    alert("You clicked the button! \n How did you get it first try?")
}

function DocWrite() {
    document.write("This is a document write test bla bla bla bla first name last name you know the deal")
}

function ButtonDocWrite() { //innerHTML
    document.getElementById("docWrite2").innerHTML = "Noah SUCKS!"+"<br>"
    document.getElementById("docWrite2").innerHTML += "Noah SUCKS! AGAIN!" +"<br>"
    document.getElementById("docWrite2").innerHTML += "Noah SUCKS! ONE MORE TIME!" +"<br>"
}

function ButtonDocUnwrite() { //innerHTML
    document.getElementById("docWrite2").innerHTML = "blablablablablablablablablablablablablablablablablablablablablablablablabla"
    document.getElementById("docWrite2").style.color = "black"
    document.getElementById("docWrite2").style.fontSize = "20px"
    document.getElementById("docWrite2").style.fontFamily = "Times New Roman"
}

function BiggerText() {
    document.getElementById("docWrite2").style.fontSize = "50px"
}

function ComicSans() {
    document.getElementById("docWrite2").style.fontFamily = "Comic Sans MS"
}
function MakeColorRed() {
    document.getElementById("docWrite2").style.color = "red"
}
document.write("This is a document write test <br>")
document.write("Hello World!")


function Add() {
    var a = 1
    var b = 2
    var c = a+b
    document.getElementById("docWrite2").innerHTML = c
}

function Subtract() {
    var a = 1
    var b = 2
    var c = a-b
    document.getElementById("docWrite2").innerHTML = c
}
