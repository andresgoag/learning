//Ejecutar un AJAX call cuando se presione un boton y formatear un string desde JSON


var pageCounter = 1;


var animalContainer = document.getElementById("animal_info");



var btn = document.getElementById("btn"); //tomar el elemento boton

//Agregar event listener
btn.addEventListener("click", function getStore(){
  var ourRequest = new XMLHttpRequest();
  ourRequest.open("GET",'https://learnwebcode.github.io/json-example/animals-'+ pageCounter +'.json');
  ourRequest.onload = function(){
    if (ourRequest.status >= 200 && ourRequest.status<= 400) {   // Para conocer mas de los HTTP status: https://developer.mozilla.org/es/docs/Web/HTTP/Status
      var ourData = JSON.parse(ourRequest.responseText);
      renderHTML(ourData);
    } else {
      console.log("We connected to the server but it returned an error");
    }

  }

  ourRequest.onerror = function(){
    console.log("connection error");
  };

  ourRequest.send();
  pageCounter++;
  if (pageCounter > 3) {
    btn.style.visibility = "hidden";
  }
});







function renderHTML(data) {
  var htmlString = "";

  console.log(data);

  for (i=0; i < data.length; i++) {
    htmlString += "<p>" + data[i].name + " is a " + data[i].species +"</p>";
  }

  animalContainer.insertAdjacentHTML("beforeend", htmlString);
}



// handlebars.js
