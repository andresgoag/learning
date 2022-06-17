const number = 1;
const num2 = number;

console.log(num2); // En este caso, se copia el valor de 1 a la variable num2




const person = {
    name: 'Max'
};

const secondPerson = person;

person.name = 'Manu';


console.log(secondPerson); // En este caso el primer objeto fue guardado en memoria y la variable person guarda un puntero a ese espacio en memoria
// por lo tanto al cambiar el valor del primer objeto el segundo hace referencia al mismo objeto.



// Para realmente copiar un objeto inmutable:

const secondPerson = {
    ...person
}; // Este no se vera afectado
