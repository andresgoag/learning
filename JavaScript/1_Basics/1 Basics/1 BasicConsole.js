//Asi se hace un comentario en javascript
//Estos comandos son para correr en la consola del navegador para escribir las primeras lineas de javascript

alert("Hello World!")


//Number types
10
20.2
-13.4

//Operaciones
2+2
2-2
2*2
2/2
15%14 //modulo



//Strings
"Hello World 10"

"Django " + "Is super cool" //Concatenar
"django".lenght //verificar la longitud de la cadena
"django\nstart a new line" //new line
"django\tgive me a tab" //tabulacion
"hello\" jelly" //quote character
"Hello"[0] //index



//Booleans
true
false

//Undefined and null
undefined
null


console.clear() //Para limpiar la consola





// Coercion

// convertir de entero a cadena
var entero = 20;
var cadena = String(entero);

// convertir de cadena a entero
var numero = Number(cadena)











//Variables

//format: var varName = value;


// let: es solo accesible en el scope que fue declarado
// const: para definir espacio en memoria que no va a cambiar. no se puede reasignar

var bankAccount = 100;
var deposit = 50;
var total = bankAccount + deposit;

var greeting = "Welcome back: ";
var name = "Andres";
alert(greeting + name);


var myVariable; //esta sera Undefined
var bonus = null; // se asigna aproposito el valor de nada


// Scope
// Global: una variable definida al inicio del script será globalThis, y se puede acceder a su valor dentro de una funcion.
// Local: una variable definida al interior de una funcion solo se podra acceder a su valor en el interior de la funcion.
//         esta debe ser declarada explicitamente con los keyword "var", "let", "const". Si se hace una declaracion de variable sin estos
//         keywords, sera una variable global y probablemente bloqueada por algunos navegadores



//General metods

alert("Hola") // Para mostrar un mensaje en el navegador
console.log("Hola") //Para escribir un mensaje en la consola
var age = prompt("Enter your age: ") //input del usuario





// Operaciones de strings

var nombre = 'Andres', apellido = 'Gomez'

var nombreEnMayusculas = nombre.toUpperCase() // mayusculas

var apellidoEnMinusculas = apellido.toLowerCase() // minusculas

var primeraLetraDelNombre = nombre.charAt(0) // caracter en la posicion ()

var cantidadDeLetras = nombre.length // longitud de la cadena

var nombreCompleto = `${nombre} ${apellido}` // Interpolacion de texto

var str = nombre.substr(1, 2) // sub string, (posicion inicial, longitud)








// Operaciones de numeros

edad = 27

edad = edad + 1 // incremento
edad += 1 // incremento


peso = 80

peso = peso - 2 //decremento
peso -= 2 //decremento



// decimales

var precioDeVino = 200.3

var total = precioDeVino * 3 // = 600.9000000000001

var total = Math.round(precioDeVino * 100 * 3) / 100 // 600.9

var totalStr = total.toFixed(3) // pasar numero a string con 3 decimales

var total2 = parseFloat(totalStr) // string a float


// division 
var pizza = 8 
var personas = 2

var cantidadPorcionesPorPersona = pizza / personas





// debugger

// cuando el navegador encuentra esta palabra detiene la ejecucion.
// desde las herramientas de developer se puede controlar la ejecucion del programa cuando se encuentra esta palabra





/*
Valores falsy (valores falsos) en Javascript:

false

0

null

""

undefined

NaN

Los demás son valores Truthy (valores verdaderos).
*/






//dates

function diasEntreFechas(fecha1, fecha2) {
    const unDia = 1000 * 60 * 60 * 24 // milisegundos del dia
    const diferencia = Math.abs(fecha1 - fecha2) // la resta de fechas se da en milisegundos

    return Math.floor(diferencia / unDia)
}


const hoy = new Date()
const nacimiento = new Date(1995, 5, 30) // Enero es el mes 0

console.log(diasEntreFechas(hoy, nacimiento));



