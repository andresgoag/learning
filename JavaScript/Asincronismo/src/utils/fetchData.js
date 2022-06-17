let XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest; // instanciar el objeto porque estamos en node, no se requiere para el navegador


const fetchData = (url_api) => {

    return new Promise((resolve, reject) => {
        const xhttp = new XMLHttpRequest();
        xhttp.open('GET', url_api, true) // el ultimo true activa el asincronismo en XMLHttpRequest, es el valor por defecto, pero es buena practica ponerlo
        xhttp.onreadystatechange = (() => {
            // Referencia para ajax response https://www.w3schools.com/xml/ajax_xmlhttprequest_response.asp
            if (xhttp.readyState === 4) {
                (xhttp.status === 200)
                    ? resolve(JSON.parse(xhttp.responseText))
                    : reject(new Error('Error ', url_api))
            }
        });
        xhttp.send();
    });
}


module.exports = fetchData;