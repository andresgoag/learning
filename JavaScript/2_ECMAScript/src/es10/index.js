let array = [1,2,3, [1,2,3, [1,2,3]]];

console.log(array.flat());
console.log(array.flat(2));



let array = [1,2,3,4,5];

console.log(array.flatMap(value => [value, value * 2]));





// Eliminar los espacios en blanco de un string

let hello = '               hello world    '

console.log(hello);
console.log(hello.trimStart());
console.log(hello.trimEnd());




// Manejo de catch
// originalmente
try {

} catch (error) {
    error
}

// es10
try {

} catch { // sin especificar que recibe error, estara disponible dentro del bloque
    error
}




// Construir un objeto apartir de un arreglo
let entries = [["name", "oscar"], ["age", 32]];
console.log(Object.fromEntries(entries));



// Objeto tipo simbolo
let mySymbol = `My symbol`;
let symbol = Symbol(mySymbol);
console.log(symbol.description);

