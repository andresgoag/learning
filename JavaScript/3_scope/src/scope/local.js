const helloWorld = () => {
    const hello = 'Hello World';
    console.log(hello); // se imprimira hello world
}

helloWorld();
console.log(hello); // Esto sera error, ya que la variable no es global, solo existe dentro de helloworld



// Ambito lexico

var scope = "i am global";

const functionScope = () => {
    var scope = "i am just a local";

    const func = () => {
        return scope; // retornara el valor de scope declarado dentro de la funcion
    }

    console.log(func());
}

functionScope();
console.log(scope); // se imprimira "i am global"