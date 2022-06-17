const saludar = async (nombre) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(`Hola, ${nombre}`);
            resolve(nombre);
        }, 1500);
    });
}

const despedida = async (nombre) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(`Adios, ${nombre}`);
            resolve()
        }, 1000);
    })
}

const hablar = async (nombre) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("Bla bla bla bla...");
            // resolve(nombre);
            reject("Hay un error");
        }, 1000);
    })
}


const main = async() => {
    try {
        const nombre = await saludar("Andres");
        await hablar();
        await hablar();
        await hablar();
        await despedida(nombre);
    } catch (error) {
        console.error(error);
    }
}



console.log("Empezando proceso");
main();
console.log("Terminando proceso");