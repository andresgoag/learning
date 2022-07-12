let boton = document.getElementById("saludar");
boton.addEventListener("click", (evento) => {
    nombre = document.getElementById("name").value;
    eel.hello(nombre)((ret) => {
        document.getElementById("saludo").textContent = ret['message'];
    })
})