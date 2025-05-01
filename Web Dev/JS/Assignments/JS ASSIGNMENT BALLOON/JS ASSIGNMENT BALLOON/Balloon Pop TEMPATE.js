// ALI ADNAN

// CONSTANTS
const maxSize = 400;
const minSize = 90;
const defaultSize = 200;

// VARIABLES
let size = defaultSize;
let popped = false;

// FUNCTIONS
function updateBalloon() {
  balloon.style.height = size + 'px';
}

function inflate() {
  if (popped) return;
  size = Math.round(size * 1.1);
  console.log(size)
  if (size > maxSize) {
    popBalloon();
  } else {
    updateBalloon();
  }
}

function deflate() {
  if (popped) return;
  console.log (size)
  size = Math.round(size * 0.9);
  if (size < minSize) size = minSize;
  updateBalloon();
}

function popBalloon() {
  popped = true;
  balloon.src = "pop.png"; // Example popped balloon image
  InflateBtn.disabled = true;
  DeflateBtn.disabled = true;
}

function newBalloon() {
  popped = false;
  size = defaultSize;
  balloon.src = "balloon.png"; // Blue balloon image
  updateBalloon();
  InflateBtn.disabled = false;
  DeflateBtn.disabled = false;
}

// Wait for the DOM to fully load before accessing elements and adding event listeners
document.addEventListener('DOMContentLoaded', () => {
  // ELEMENTS
  balloon = document.querySelector('.imgBalloon');
  InflateBtn = document.querySelector('.btnInflate');
  DeflateBtn = document.querySelector('.btnDeflate');
  ResetBtn = document.querySelector('.btnReset');

  // INITIAL EVENT LISTENERS
  InflateBtn.addEventListener('click', inflate);
  DeflateBtn.addEventListener('click', deflate);
  ResetBtn.addEventListener('click', newBalloon);

  // Set initial size
  updateBalloon();
});
