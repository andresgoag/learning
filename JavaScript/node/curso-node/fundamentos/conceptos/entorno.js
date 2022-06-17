// Acceder a variables de entorno
// Ejecutar el programa designando las variables de entorno NOMBRE=Andres node conceptos/entorno.js 
// Las variables de entorno van en mayusculas y espacios con _
let nombre = process.env.NOMBRE || 'Sin nombre'; // Valor alterno a la variable de entorno
let web = process.env.WEB || 'no tengo web';
console.log(`Hola ${nombre}`);
console.log(`Mi web es ${web}`);