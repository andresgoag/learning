
// Variables definidas en un scope global
var hello = "Hello";
let world = "Hello World (let)";
const helloWorld = "Hello World! (const)";

// acceder a una variable en el scope global
console.log(hello);


const anotherFunction = () => {
    // aqui se podra acceder a las variables definidas en el scope global
    console.log(hello);
    console.log(world);
    console.log(helloWorld);
}

anotherFunction();





// Redeclaracion de variables

var hello = "nuevo valor para hello"  // var permite redeclarar una variable
// let world = "nuevo valor para world" // esta linea da un error, let y const no permiten redeclarar variables

console.log(hello);
console.log(world);





// Malas Practicas !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

// Crear variables globales en funciones
const nuevaFuncion = () => {
    globalVar = 'im global' // si dentro de una funcion se crea una nueva variable sin las palabras var, let o const, esta sera una variable global
}

nuevaFuncion()
console.log(globalVar); // estoy accediendo en scope global a una variable definida en una funcion
