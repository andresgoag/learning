const saludar = (nombre, miCallback) => {
    setTimeout(() => {
        console.log(`Hola, ${nombre}`);
        miCallback(nombre);
    }, 1500)
}

const despedida = (nombre, otroCallback) => {
    setTimeout(() => {
        console.log(`Adios, ${nombre}`);
        otroCallback();
    }, 1000)
}

// Forma correcta de ejecutar funciones asioncrona
console.log("Iniciando proceso...");
saludar("Andres", (nombre) => {
    despedida(nombre, () => console.log('Terminando proceso'))
});



// de forma sincrona se ejecuta primero adios porque es mas rapida:
// saludar("Andres", () => {});
// despedida("Andres", () => {})
