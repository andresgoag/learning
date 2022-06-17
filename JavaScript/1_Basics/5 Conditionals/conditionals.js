var hot = false;
var temp = 90;





if (temp>80) {
  console.log("Very Hot");
}
else if (temp<=80 && temp>=50) {
  console.log("Average temp outside");
}
else if (temp<50 && temp>=32) {
  console.log("Its pretty cold outside");
}
else {
  console.log("Super cold");
}




// Switch

var numero = 1

switch (numero) {
  case 1:
    console.log("soy uno"); // Se ejecutaria esta sentencia   
    break;

  case 2:
    console.log("soy dos");
    break;

  default:
    console.log("No se ejecuto ningun caso, soy el default");
    break;
}




// Condicional ternario

(true) 
  ? console.log('Verdadero') 
  : console.log('Falso');



// Se puede utilizar para asignar valor a una variable dependiendo de una condicion
var frecuencia = (contador===1)
    ? "vez"
    : "veces";




    view
    ? null
    : (
      <p>
        <input
          onChange={this.handleChange}
          value={this.state.inputText} />
      </p>
    )