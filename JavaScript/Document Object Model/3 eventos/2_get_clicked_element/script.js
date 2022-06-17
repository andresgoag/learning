document.getElementById("divId").addEventListener("click", someFunction);

function someFunction(clickedElement) {
  console.log(clickedElement.target.id);
}



// target is the element that triggered the event (e.g., the user clicked on)
// currentTarget is the element that the event listener is attached to.