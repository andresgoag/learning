var countries = ["USA", "Germany", "China"]

x = countries[0]; // Esto sera "USA"

countries[2] = "Colombia"; // Esto cambiara a China por Colombia



// Array Iteration

var arr = ["A", "B", "C"]

for (var letter of arr) {
  console.log(letter);
} //Esto imprimira cada elemento el array "arr"


arr.forEach(alert); //Esto ejecutara la funcion alert, con parametro cada elemento de "arr", mostrara en el navegador 3 alertas: "A" , "B" , "C"


function awesome(name){
  console.log(name + " is awesome");
}

var arreglo = ["Python", "Django", "Science"]

arreglo.forEach(awesome)





// Metodos del array
// https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Objetos_globales/Array

var frutas = ["Manzana", "Platano", "Cereza", "Fresa"];

// Agregar al final del array
frutas.push("Uvas");

// Eliminar el ultimo elemento del array
var lastItem = frutas.pop();

// Agregar elemento al inicio de la lista
frutas.unshift("Peras");

// Eliminar el elemento del inicio
frutas.shift();

// Posicion de un elemento en un array
var posicion = frutas.indexOf("Cereza")





var articulos = [
  { nombre: 'Bici', costo: 3000 },
  { nombre: 'TV', costo: 2500 },
  { nombre: 'Libro', costo: 320 },
  { nombre: 'Celular', costo: 10000 },
  { nombre: 'laptop', costo: 20000 },
  { nombre: 'teclado', costo: 500 },
  { nombre: 'audifonos', costo: 1700 }
]



//   Metodo Filter  
/* Válida si es un true o false para poder meterlos al nuevo array, y éste método no modifica el array original */

var articulosFiltrados = articulos.filter( function (articulo) {

  return articulo.costo <= 500  /* Menor o igual a 100 */ 

} );

console.log(articulosFiltrados);




//   Metodo Map 

var nombreArticulos = articulos.map( function (articulo) {
  
    return articulo.nombre

} );

console.log(nombreArticulos); // una nuevo array con todos los nombres del array principal


// The function of map gets 3 optional parameters (item, index, originalArray)

let arr = [1,2,3,4];

let newArr = arr.map( (number, index, theArray) => {
  theArray[index] = number + 1;
} )

// this will modify the original array adding one to each item





//   Metodo Find
/* De igual forma, con este método se valida un true o false para encontrar un elemento y si está lo regresa y si no, no pasa nada */

var encuentraArticulos = articulos.find(function(articulo){
  return articulo.nombre === 'laptop';
});

console.log(encuentraArticulos);





//   Metodo forEach

// The function of foreach gets 3 optional parameters (item, index, originalArray), the difference with map is that it won't return anything

articulos.forEach(function(articulo){
  console.log(articulo.nombre);
});




//   Metodo Some
/* Este método nos regresa un false o un true para validar si hay o no artículos que cumplan la validación */

var articulosBaratos = articulos.some(function(articulo){
  return articulo.costo <= 700;
});

console.log(articulosBaratos); 





//   Metodo Every

/* Este método checa que todos los elementos en el array cumplan con la validación que ponemos, y al final nos regresa un true o un false */

var articulosBaratos = articulos.every(function(articulo){
  return articulo.costo <= 700;
});

console.log(articulosBaratos); 





//   Metodo Reduce
/* Este método corre una función en cada elemento del array, para comenzar a sumar los costos de cada elemento. */

// la funcion debe recibir 2 argumentos, el acumulador y la variable que tendra el valor de cada elemento del array

var costoTotal = articulos.reduce(function(totalActual, articulo){
  return articulo.costo + totalActual;
}, 0); // El 0 será la cantidad inicial con la que comenzará el totalActual

console.log(costoTotal); 





//   Metodo Includes

var numeros = [1, 2, 3, 4, 5, 6];

var incluyeNumero = numeros.includes(2); 

console.log(incluyeNumero);






// Array from html collection
var arr = Array.from(htmlCollection);



// Splice: se puede utilizar para agregar elementos, o remover elementos en la posicion que queramos.

















// Splice and slice -> splice se puede usar para cambiar los elementos del array


// Concatenar dos arrays concat()

const hege = ["Cecilie", "Lone"];
const stale = ["Emil", "Tobias", "Linus"];
const children = hege.concat(stale);