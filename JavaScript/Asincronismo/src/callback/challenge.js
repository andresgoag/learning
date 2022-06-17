let XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest; // instanciar el objeto porque estamos en node, no se requiere para el navegador


let API = 'https://rickandmortyapi.com/api/character/';


function fetchData(url_api, callback) {
    let xhttp = new XMLHttpRequest();
    xhttp.open('GET', url_api, true) // el ultimo true activa el asincronismo en XMLHttpRequest, es el valor por defecto, pero es buena practica ponerlo

    xhttp.onreadystatechange = function (event) {
        // Referencia para ajax response https://www.w3schools.com/xml/ajax_xmlhttprequest_response.asp
        if (xhttp.readyState === 4) {
            if (xhttp.status === 200) {
                callback(null, JSON.parse(xhttp.responseText)) 
            } else {
                const error = new Error('Error ' + url_api);
                return callback(error, null) // por estandar se pasa como argumento primero el error y despues los argumentos.
            }
        }
    }

    xhttp.send();
}


fetchData(API, function(error1, data1) {
    if (error1) return console.error(error1);
    fetchData(API + data1.results[0].id, function (error2, data2) {
        if (error2) return console.error(error2);
        fetchData(data2.origin.url, function (error3, data3) {
            if (error3) return console.error(eerror3);
            console.log(data1.info.count);
            console.log(data2.name);
            console.log(data3.dimension);
        });
    })
})

