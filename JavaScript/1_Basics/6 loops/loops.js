

/////////////////////////////////
//         While Loop          //

var x = 0;

while (x < 5) {
  console.log(x);
  if (x===3) {
    console.log("x is equal to three");
    break;
  }
  x = x+1;
}


var z = 0;

while (z <= 10) {
  if (z%2 == 0 ) {
    console.log(z);
  }
  z = z+1
}




///////////////////////////////
//         For Loop          //

for (var i = 0; i < 5; i++) {
  console.log("Number is "+i);
}



var word = "ABCDEFGHIJK";

for (var i = 0; i < word.length; i++) {
  console.log(word[i]);
}

for (var i = 0; i < word.length; i=i+2) {
  console.log(word[i]);
}






///////////////////////////////
//        Do While           //


var contador = 0;

var llueve = () => Math.random() < 0.25;

do {
  contador++;
} while (!llueve());

var frecuencia = (contador===1)
    ? "vez"
    : "veces";

console.log(`Fui a ver si llovía ${contador} ${frecuencia}`);





////////////////////////////////
//         Excercise 1        //

for (var i = 0; i < 5; i++) {
  console.log("Hello");
}

var i = 0;
while (i<5) {
  console.log("hello");
  i=i+1;
}




////////////////////////////////
//         Excercise 2        //

var x = 1;
while (x <= 25) {
  if (x%2 != 0) {
    console.log(x);
  }
  x += 1
}


for (var i = 1; i <= 25; i++) {
  if (i%2 != 0) {
    console.log(i);
  }
}
