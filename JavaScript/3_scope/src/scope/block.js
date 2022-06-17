// Las variables declaradas con let y const solo estaran disponibles dentro del bloque en el que se hagan.


const fruits = () => {
    if (true) {
        var fruits1 = 'apple';
        let fruits2 = 'banana';
        const fruits3 = 'kiwi';
        console.log(fruits1);
        console.log(fruits2);
        console.log(fruits3);
    }

    console.log(fruits1);
    // console.log(fruits2); Esto generara un error al estar fuera del bloque de declaracion
    // console.log(fruits3);

}

fruits();









// Ejemplo 2:

var x = 1;
{
    var x = 2;
    console.log(x); // imprime 2
}

console.log(x); // imprime 2



let x = 1;
{
    let x = 2;
    console.log(x); // imprime 2
}

console.log(x); // imprime 1






// Ejemplo 3

const anotherFunction = () => {
    for (var i = 0; i < 10 ;i++) { // declaracion var
        setTimeout(() => {
            console.log(i); // imprime unicamente el ultimo valor
        }, 1000)
    }
}

anotherFunction();






const anotherFunction = () => {
    for (let i = 0; i < 10 ;i++) { // declaracion let
        setTimeout(() => {
            console.log(i); // imprime todo el recorrido del for
        }, 1000)
    }
}

anotherFunction();