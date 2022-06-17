
var stores_p = document.getElementById("p_api");
var boton_pedir_datos = document.getElementById("btn_get_api");
var stores_item = document.getElementById("stores_item");



boton_pedir_datos.addEventListener("click", function () {

  var request = new XMLHttpRequest();

  request.open("GET", "http://127.0.0.1:5000/store");

  request.onload = function () {  // https://developer.mozilla.org/es/docs/Web/API/XMLHttpRequestEventTarget/onload
    if (request.status >= 200 && request.status <= 400) { // Para conocer mas de los HTTP status: https://developer.mozilla.org/es/docs/Web/HTTP/Status
      var datos = JSON.parse(request.responseText);
      agregarHtmlDiv(stores_p,datos);
    } else {
      console.log("No se pudo conectar al servidor");
    }
  }

  request.onerror = function () {
    console.log("No se pudo conectar al servidor");
  }

  request.send();
})





function agregarHtmlDiv (contenedor, datos) {
  contenedor.textContent = ""
  for (i=0; i<datos["stores"].length; i++) {
    contenedor.textContent += datos["stores"][i]["name"]+" // "
  }
}






function agregarHtml (contenedor, datos) {
  contenedor.textContent = ""
  for (i=0; i<datos["items"].length; i++) {
    contenedor.textContent += datos["items"][i]["name"]+ " : " + datos["items"][i]["price"] + " // "
  }
}





function ajax_post () {

  var nombre_tienda = document.getElementById("tienda").value;
  var info = {name: nombre_tienda};
  var info_json = JSON.stringify(info);


  var request = new XMLHttpRequest();

  request.open("POST", "http://127.0.0.1:5000/store");
  request.setRequestHeader("Content-Type", "application/json");


  request.onreadystatechange = function () {          // https://developer.mozilla.org/es/docs/Web/API/XMLHttpRequest/onreadystatechange
    if (request.readyState === 4 && request.status === 200) { // Para conocer mas sobre HTTP readyState visitar: https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState
      alert("Se envio satisafactoriamente la tienda "+nombre_tienda);
    }
  }

  request.send(info_json);

}


// var info = "name="+nombre_tienda+"&last_name="+last_name;
// request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
// request.send(info_json);






function ajax_post_items () {

  var nombre_tienda = document.getElementById("tienda_item").value;



  var request = new XMLHttpRequest();

  request.open("GET", "http://127.0.0.1:5000/store/"+nombre_tienda+"/item");



  request.onreadystatechange = function () {
    if (request.readyState === 4 && request.status === 200) {
      var datos = JSON.parse(request.responseText);
      agregarHtml(stores_item,datos);
    }
  }

  request.send();

}
