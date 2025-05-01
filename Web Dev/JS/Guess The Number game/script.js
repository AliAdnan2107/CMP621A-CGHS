//Ali Adnan
let secretNumber = Math.trunc(Math.random() * 20) + 1; //Secret number between 1 and 20
let score = 20; // Initial score
let highscore = 0; // Highscore
console.log(secretNumber) // For testing purposes

function guessNum() {
    numguess = Number(document.getElementById("guess").value); // Get the guessed number from the input field
    console.log(numguess);
    if (numguess == secretNumber) { // If the guessed number is equal to the secret number
        document.getElementById("message").innerHTML = " 🎉 Correct Number!"; 
        document.getElementById("number").innerHTML = secretNumber;
        document.querySelector("body").style.backgroundColor = "limegreen";
        if (score > highscore) { // If the current score is greater than the highscore
            highscore = score;
            document.getElementById("highscore").innerHTML = highscore;
        }
    } else if (numguess > secretNumber) { // If the guessed number is greater than the secret number
        if (score > 1) { // If the score is greater than 1
            document.getElementById("message").innerHTML = " 📈 Too High!";
            score--;
            document.getElementById("score").innerHTML = score;
        } else { // If the score is 0 or less
            document.getElementById("message").innerHTML = " ☹️ You lost the game!";
            document.getElementById("score").innerHTML = 0;
            document.querySelector("body").style.backgroundColor = "red";
        }
    } else if (numguess < secretNumber) { // If the guessed number is less than the secret number
        if (score > 1) { // If the score is greater than 1
            document.getElementById("message").innerHTML = " 📉 Too Low!";
            score--;
            document.getElementById("score").innerHTML = score;
        } else { // If the score is 0 or less
            document.getElementById("message").innerHTML = " ☹️ You lost the game!";
            document.getElementById("score").innerHTML = 0;
            document.querySelector("body").style.backgroundColor = "red";
        }
    }
}

function again() { // Function to reset the game
    score = 20;
    secretNumber = Math.trunc(Math.random() * 20) + 1;
    document.getElementById("score").innerHTML = score;
    document.getElementById("message").innerHTML = "Start guessing...";
    document.getElementById("number").innerHTML = "?";
    document.querySelector("body").style.backgroundColor = "#222";
    document.getElementById("guess").value = "";
    console.log(secretNumber);
}