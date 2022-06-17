// Explicacion de JSON, JavaScript Object Notation


// Object

var myCat = {
  "name": "Meowsalot",
  "species": "cat",
  "favFood": "tuna"
}


// Array

var myFavColors = ["blue", "gree", "purple"]



// Array of Objects   [{},{}]

var thePets = [
  {
    "name": "Meowsalot",
    "species": "cat",
    "favFood": "tuna"
  },
  {
    "name": "Barky",
    "species": "dog",
    "favFood": "carrots"
  }
]





// AJAX, Asynchronus JavaScript and XML
// Es el proceso de obtener datos nuevos sin recargar la pagina
// La herramienta para hacer AJAX en el buscador es XMLHttpRequest

//Este codigo correra el AJAX call al cargar la pagina

var ourRequest = new XMLHttpRequest(); //Crear un nuevo objeto XMLHttpRequest

ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-1.json'); //Comando para pedir los datos a una URL

ourRequest.onload = function(){ //Funcion para decir que hacer cuando los datos sean recibidos
  var ourData = JSON.parse(ourRequest.responseText); //JSON.parse() es el comando para decirle al buscador que interprete la respuesta en formato JSON. ".responseText" devuelve como string los datos recibidos
  console.log(ourData[0]);
}

ourRequest.send(); //Enviar el requerimiento
