
const imprimirLi = (element) => {

    let elemento = element.target;

    let seccion = elemento.parentElement.parentElement;

    console.log(`Hiciste click en ${elemento.textContent} dentro de la ${seccion.querySelector('h3').textContent}`);
}




document.getElementById("lista1").addEventListener('click', imprimirLi);
document.getElementById("lista2").addEventListener('click', imprimirLi);