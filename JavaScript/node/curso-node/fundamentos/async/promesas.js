const saludar = (nombre) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(`Hola, ${nombre}`);
            resolve(nombre);
        }, 1500);
    });
}

const despedida = (nombre) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(`Adios, ${nombre}`);
            resolve()
        }, 1000);
    })
}

const hablar = (nombre) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("Bla bla bla bla...");
            // resolve(nombre);
            reject("Hay un error");
        }, 1000);
    })
}


console.log('Iniciando el proceso...');
saludar("Andres")
    .then(hablar)
    .then(hablar)
    .then(hablar)
    .then(hablar)
    .then(despedida)
    .then((nombre) => {
        console.log('Terminado el proceso');
    })
    .catch(error => console.error(error))
