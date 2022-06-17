//https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Trabajando_con_objectos

var x;
var value;

var carInfo = {
    make:"Toyota",
    year:1990, 
    model:[1,9,9,1]
}


x = carInfo["make"] // Esto sera Toyota
// otra sintaxis:
x = carInfo.make


value = carInfo["model"][1] // Se puede hacer index del index, esto devolvera 9

carInfo["year"] = 1991; //se puede reasignar valores del objeto

console.dir(carInfo); //para mostrar la estructura del objeto en la consola



// deconstruir un objeto para obtener el parametro para una funcion. 
// En este caso, la funcion accedera al parametro nombre, si el objeto pasado no tiene nombre, genera un error
function imprimirNombre ({ nombre }) {
    console.log(nombre)
}


var obj1 = {
	obj2 : {
		nombre: 'victor',
		edad: 19
	}
}

function saludar(obj){
	var {nombre, edad} = obj.obj2
	console.log(`Hola me llamo ${nombre} y tengo ${edad} años`)
}
saludar(obj1) // Salida ->  Hola me llamo victor y tengo 19 años








// side effects con objetos y funciones
// ====================================

var andres = {
    nombre: 'Andres',
    apellido: 'Gomez',
    edad: 25 
}


// Cuando la funcion recibe un objeto, esta modificara el objeto
function cumpleanos(persona) {
    persona.edad += 1
}

cumpleanos(andres) // incrementa el valor de la edad de andres



// para evitar que la funcion tenga este side effect, se debe devolver un nuevo objeto con el valor modificado:

function cumpleanosNuevoObjeto(persona) { // esta funcion retorna un nuevo objeto identico al que recibe pero con la edad modificada
    return {
        ...persona,
        edad: persona.edad + 1
    }
}


var andresMasViejo = cumpleanosNuevoObjeto(andres)






///////////////////////////////////
////     iterar en un objeto     //

for (key in carInfo){
  console.log(key);
  console.log(carInfo[key]);
}





////////////////////////////////////
////          Methods          /////

// Referencia para el operador this: https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Operadores/this


var simple = {
  prop:"Hello",
  myMethod: function(){
    console.log("The myMethod was called");
  }
}


simple.myMethod(); //Asi se llama al metodo de un objeto




var myObj = {
  name:"Andres",
  greet: function(){
    console.log("Hello " + this.name); //Se refiere al name del objeto
  }
}






// Funcion constructora de objetos

function auto (marca, modelo, annio) {
    this.marca = marca;
    this.modelo = modelo;
    this.annio = annio;
}


// agregar funcion a un objeto
auto.prototype.saludar = function () {
    console.log(`Hola soy un carro ${this.marca} ${this.modelo}`);
}

// NOTA: si la funcion anterior se reemplaza por una arrow function, arrojara un error.
// ya que en las arrow function, this tiene otro contexto
// This en una arrow function hace referencia a lo que sea this en el espacio global




var autoNuevo = new auto("Tesla", "Model 3", 2020);

autoNuevo.saludar()




// Herencia prototipal

// Recordar que todas las funciones tienen el atributo prototype

// forma original (Complicada)

function heredaDe (proptipoHijo, prototipoPadre) {
    var fn = function () {}
    fn.prototype = prototipoPadre.prototype
    proptipoHijo.prototype = new fn
    prototipoHijo.prototype.constructor = proptipoHijo
}


// Prototipo padre

function Persona (nombre, apellido, altura) {
    this.nombre = nombre
    this.apellido = apellido
    this.altura = altura
}

Persona.prototype.saludar = function () {
    console.log(`Hola, me llamo ${this.nombre} ${this.apellido}`);
}

Persona.prototype.soyAlto = function () {
    return this.altura > 1.8
}


// Prototipo hijo

function Desarrollador (nombre, apellido) {
    this.nombre = nombre
    this.apellido = apellido
}

heredaDe(Desarrollador, Persona)

Desarrollador.prototype.saludar = function () {
    console.log(`Hola, me llamo ${this.nombre} ${this.apellido} y soy desarrollador`);
}

// Desarrollador es un prototipo que tiene su propia funcion saludar, pero tambien usa la funcion soy alto, heredada de Persona


var andres = new Persona('Andres', 'Gomez', 1.82)

var juan = new Desarrollador('Juan', 'Gomez')
