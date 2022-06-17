// Crear una lista de listas con key:value de un objeto
const data = {
    frontend: 'oscar',
    backend: 'Isabel',
    design: 'Ana'
}

const entries = Object.entries(data);
console.log(entries);
console.log(entries.lenght);




// Crear lista con los values de un objeto
const data = {
    frontend: 'oscar',
    backend: 'Isabel',
    design: 'Ana'
}

const values = Object.values(data);
console.log(values);
console.log(values.length);





// modificar strings
const string = 'hello';
console.log(string.padStart(7,'hi'));
console.log(string.padEnd(12, ' -------------------------'));






//Async y Await


const helloWorld = () => {
    return new Promise((resolve, reject) => {
        (false)
            ? setTimeout(() => resolve("Hello world"), 3000)
            : reject(new Error ('Test error'))
    })
}


const helloAsync = async () => {
    const hello = await helloWorld();
    console.log(hello);
}

helloAsync();




const anotherFunction = async () => {
    try {
        const hello = await helloWorld();
        console.log(hello);
    } catch (error) {
        console.log(error);
    }
}

anotherFunction();