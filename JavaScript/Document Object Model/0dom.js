//Important attributes

document.URL;
document.body;
document.head;
document.links;

//Important Methods

document.getElementById(); //Retorna el elemento con este id
document.getElementsByClassName(); //Retorna el elemento con esta clase
document.getElementsByTagName(); // Retorna los elementos con este tag
document.querySelector(); // Retorna el primer elemento encontrado con este selector sintaxis de css
document.querySelectorAll(); //Retorna todos los elementos con este selector sintaxis de css




//Cambiar un atributo del HTML, CSS:

var myheader = document.querySelector("h1")
myheader.style.color = "orange" //Esto cambiara el color del header
