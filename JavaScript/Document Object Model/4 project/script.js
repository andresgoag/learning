//Restart Game button
var boton = document.querySelector("#b");

// Grab all the squares
var squares = document.querySelectorAll("td");

// Clear all the squares
function clearBoard(){
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = "";
  }
}

boton.addEventListener("click", clearBoard);



// Check the square value
function changeValue(){
  if (this.textContent === "") {
    this.textContent = "X";
  }else if (this.textContent === "X") {
    this.textContent = "O";
  }else {
    this.textContent = ""
  }
}

//For loop to add event listeners to all the squares
for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener("click",changeValue)
}
