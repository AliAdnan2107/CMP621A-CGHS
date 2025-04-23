console.log("What","Do","Commas","Do?");
console.log("Does",       "Space", "Make     ", "A", "Difference?");
console.log("What about " + "addition?")
console.log("And how about our beautiful integers like", 4)
console.log (typeof 4)
console.log (typeof "4")
console.log (typeof true)
console.log (typeof false)
console.log (typeof ButtonAlert())
console.log (typeof "docWrite2")
alert("Hey man you wanna go ahead and hit the ok right there so you can see what happens?")


var a= prompt ("Enter your favorite number")
var b= prompt ("Enter your favorite color (ENTER IT EXACTLY AS IT IS)")

function FavNumber() {
    document.getElementById("docWrite2").innerHTML = a
    document.getElementById("docWrite2").style.color = b
}   
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

function Lowercase(){
    let text = "Hello World!"
    document.getElementById("docWrite2").innerHTML = text.toLowerCase()
}

function Uppercase(){
    let text = "Hello World!"
    document.getElementById("docWrite2").innerHTML = text.toUpperCase()
}

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

function Add45() {
    var i = 0;

    while (i <= 900) {
        document.getElementById("docWrite2").innerHTML +=  i + " <br>";
        i += 45; // Increment i by 45
    }
}

function Remove20(){
    var i = 300;
    
    while (i>=40) {
        document.getElementById("docWrite2").innerHTML +=  i + " <br>";
        i -= 20;
    }
}

function DoGame() {
    var i;
    do {
        i = prompt("Enter a number between 1 and 10");
        if (i == 5) {
            alert("You guessed the right number! Goodbye");
        } else {
            alert("Wrong guess! Try again.");
        }
    } while (i != 5);
}

function RandMath() {
    var X=Math.random() // Generates a random number between 0 and 1
    var Y=Math.floor(X*101) // Generates a random number between 0 and 100
    document.getElementById("docWrite2").innerHTML = Y
}

function RandMath8090(){
    var X=Math.random() // Generates a random number between 0 and 1
    var Y=Math.floor(X*11) + 80 // Generates a random number between 80 and 90
    document.getElementById("docWrite2").innerHTML = Y
}

function HoverFunction(){
    const element = document.getElementById("hover");
    element.addEventListener("mouseover", MouseOverFunction);
    element.addEventListener("click", MouseClick); 
}

function MouseOverFunction() {
    document.getElementById("docWrite2").innerHTML = "You hovered over the text!";
}

function MouseClick(){
    document.getElementById("docWrite2").innerHTML = "You clicked the text!";
}