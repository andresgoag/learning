const saludar = (nombre, miCallback) => {
    setTimeout(() => {
        console.log(`Hola, ${nombre}`);
        miCallback(nombre);
    }, 1500);
}

const hablar = (callbackHablar) => {
    setTimeout(() => {
        console.log("Bla bla bla bla...");
        callbackHablar();
    }, 1000);
}

const despedida = (nombre, otroCallback) => {
    setTimeout(() => {
        console.log(`Adios, ${nombre}`);
        otroCallback();
    }, 1000);
}

// Funcion recursiva
const conversacion = (nombre, veces, callback) => {
    if (veces > 0) {
        hablar(() => {
            conversacion(nombre, --veces, callback);
        })
    } else {
        despedida(nombre, callback);
    }
}

// Forma correcta de ejecutar funciones asioncrona
console.log("Iniciando proceso...");
saludar("Andres", (nombre) => {
    conversacion(nombre, 3, () => {console.log('terminado');});
})

// saludar("Andres", (nombre) => {
//     hablar(() => {
//         hablar(() => {
//             hablar(() => {
//                 despedida(nombre, () => console.log('Terminando proceso'));
//             });
//         });
//     });
// });



// de forma sincrona se ejecuta primero adios porque es mas rapida:
// saludar("Andres", () => {});
// despedida("Andres", () => {})
