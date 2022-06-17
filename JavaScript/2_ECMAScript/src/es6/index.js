////////////////////////////
// Parametros por defecto //


// normal javascript

function newFunction(name, age, country) {
    var name = name || 'oscar';
    var age = age || 32;
    var country = country || 'MX';
    console.log(name, age, country);
}


// es6

function newFunction2(name = 'oscar', age = 32, country = 'MX') {
    console.log(name, age, country);
}

newFunction2();
newFunction2('Ricardo', 23, "CO");






///////////////////////
// Template literals //

// normal javascript
let hello = "Hello";
let world = "World";
let epic = hello + " " + world
console.log(epic);


// es6
let epic2 = `${hello} ${world}`;
console.log(epic2);





////////////////////////
// Strings multilinea //

//normal javascript
let lorem = "lorem ipsum quiero escribir una frase epica que podemos separar \n"
+ "otra frase epica que necesitamos."


// es6

let lorem2 = `nueva frase epica en es6
ahora es otra frase epica sin concatenar
`;

console.log(lorem);
console.log(lorem2);





///////////////////////////////////
// Deestructuracion de elementos //


let person = {
    'name': 'oscar',
    'age': 32,
    'country': 'MX'
}

// normal javascript
console.log(person.name, person.age);

// es6
let { name, age } = person;
console.log(name, age);










/////////////////////
// Spread Operator //

let team1 = ['Oscar', 'Julian', 'Ricardo'];
let team2 = ['Valeria', 'Yesica', 'Camila'];

let education = ['David', ...team1, ...team2]; //agregara los elementos de team 1 y team 2 a este nuevo arreglo

console.log(education);









//////////////////////////////
// Declaracion de variables //

// normal javascript
var hola = 'hola' // declarando con var esta disponible de forma global

// es6
let hola2 = 'hola2' // solo esta disponible en el scope, es decir en el bloque



{
    var globalVar = "Global Var";
}


{
    let globalLet = "Global Let"
    console.log(globalLet);
}

 
console.log(globalVar); // Se puede acceder a globalVar
console.log(globalLet); // Esto sera un error ya que no se puede acceder a globalLet





///////////
// Const //



const a = 'b'; // Declara una variable que no puede cambiar de valor

a = 'a' // sera un error








/////////////////////////////
// Construccion de objetos //


let name = 'oscar';
let age = 32;

// normal javascript
obj = {name: name, age: age};
console.log(obj);

// es6
obj2 = { name, age }
console.log(obj2);







/////////////////////
// Arrow functions //


// declarar de forma sencilla funciones que reciben parametros y retornan un valor sin necesidad de usar el return statement

const names = [
    {name: 'oscar', age: 32},
    {name: 'Yesica', age:27}
]

// normal javascript
let listOfNames = names.map( function (item) {
    return item.name;
})

console.log(listOfNames);


// es6


let listOfNames2 = names.map(item => item.name); 
console.log(listOfNames2);


//sintaxis normal
const listOfNames3 = (names, ages, country) => {
    //...
}

//variantes de la arrow function
const listOfNames4 = name => { //si solo lleva un parametro no requiere de ()
    //...
}


const square = num => num * num; // inline arrow function no requiere de {}



// arrow function que retorna objetos:

// funcion recibe un objeto persona
const alturaCms = persona => {
    return {
        ...persona,
        altura: persona.altura * 100
    }
}

// como es una funcion que solo devuelve un objeto, se puede escribir asi

const alturaCms = persona => ({
    ...persona,
    altura: persona.altura * 100
})













/////////////
// Promise //


const helloPromise = () => {

    return new Promise((resolve, reject) => {
        if (true) {
            resolve('Resultado positivo');
        } else {
            reject("Resultado negativo");
        }
    })
    
}



helloPromise()
    .then(response => console.log(response)) // ejecuta con una arrow function si se ejecuto el resolve
    .then(() => console.log("Hola"))
    .catch(error => console.log(error)); // ejecuta con una arrow function si se ejecuto el reject 








// Clases 


class calculator10 {
    constructor(value) {
        this.valueA = value;
    }

    sumar(valueA, valueB) {
        return valueA + valueB + this.valueA;
    }
}

const calc = new calculator10();
console.log(calc.sumar(2,2));


// Existen los metodos que se llaman getters y setter.
// getter: es para tomar un valor
// setter: es para modificar un valor




// Herencia

class calculator20 extends calculator10 {
    constructor(value) {
        super(value);
    }
}


// la clase calculator ya puede usar la funcion sumar






// Import & Export

// ver archivo module.js para exports

import { hello } from './module';

hello();








// Generators

function*helloWorld() {
    if(true) {
        yield 'Hello, ';
    } 

    if (true) {
        yield 'World';
    }
}

const generatorHello = helloWorld();
console.log(generatorHello.next().value); // Hello,
console.log(generatorHello.next().value); // World
console.log(generatorHello.next().value); // undefined porque ya no retorna mas
