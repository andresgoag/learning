console.log("Hola mundo");


let i = 0;
setInterval(() => {
    console.log(i);
    i++;

    // Forzar un error
    if (i === 5) {
        var a = 3 + z;
    }
}, 1000);


console.log("segunda instruccion");