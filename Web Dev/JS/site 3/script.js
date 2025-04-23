console.log(1);

function oddEven() {
    var x = document.getElementById("num").value;
    var y = parseInt(x);
    if (y % 2 == 0) {
        document.getElementById("result").innerHTML = y + " is even";
    } else if (isNaN(y)) {
        document.getElementById("result").innerHTML = "Please enter a number";
    } else if (y % 2 != 0) { 
        document.getElementById("result").innerHTML = y + " is odd";
    } else {
        document.getElementById("result").innerHTML = "Please enter a number";
    }
}