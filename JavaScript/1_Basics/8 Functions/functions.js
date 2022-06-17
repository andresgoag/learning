// funciones declarativas:
function hello(){
  console.log("hello");
}


function helloYou(name){
  console.log("hello "+name);
}


function addNum(num1, num2){
  console.log(num1+num2);
}


function helloSomeone(name="Frankie"){
  console.log("Hello "+name);
}


function formal(name="Sam", title="Sr"){
  return (title + " " + name);
}


function timesNum(numInput){
  //Local scope, la variavle result no existe fuera de la funcion
  var result = numInput*5;
  return result;
}


// Global scope
var v = "GLOBAL V";
var stuff = "GLOBAL STUFF";


function fun(stuff){ // Cuando se pasa un nombre de variable como argumento de funcion, esto crea una nueva variable con este nombre, com alcance local. no importa que sea el mismo nombre que una variable global
  console.log(v); //JS primero busca si la variable esxiste dentro de la funcion y usaria ese valor, sino esta usa el valor de la variable global
  stuff = "Value reasigned inside the function" //solo se esta reasignando el valor de stuff dentro de la funcion
  console.log("Stuff inside the function:" + stuff);
}

fun();
console.log("stuff outside the function" + stuff); //aqui stuff vale lo que originalmente fue declarada por fuera de la funcion




// funciones expresivas: se usa una variable para almacenar la funcion

var saludo = function (){
  console.log("hello");
}














// Funciones como parametros


function Persona (nombre, apellido, altura) {
    this.nombre = nombre
    this.apellido = apellido
    this.altura = altura
}

Persona.prototype.saludar = function (fn) {
    console.log(`Hola, me llamo ${this.nombre} ${this.apellido}`);

    if (fn) {
        fn(this.nombre, this.apellido)
    }
}


function responderSaludo(nombre, apellido) {
    console.log(`Buen dia ${nombre} ${apellido}`);
}


var andres = new Persona('Andres', 'Gomez', 1.80)

andres.saludar(responderSaludo)










// Cambiar contexto de una funcion 


// funcion bind: el primer parametro es el contexto de la funcion (this), y luego los parametros de la funcion

const sacha = {
    nombre: 'Sacha',
    apellido: 'Lifszyc'
}


function saludar(saludo = 'Hola') {
    console.log(`${saludo}, mi nombre es ${this.nombre}`);
}


const saludarASacha = saludar.bind(sacha)

const saludarASacha_custom = saludar.bind(sacha, 'Hola che')

saludarASacha()

saludarASacha_custom()