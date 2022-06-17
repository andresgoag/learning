var spy = false;

var first = prompt("What's your first name?");
var last = prompt("What's your last name?");
var age = prompt("How old are you?");
var height = prompt("How tall are you in cm?");
var pet = prompt("What's your pets name?");
alert("Thank you for your information");


if (first[0]==last[0]) {
  if (age>20 && age<30) {
    if (height>=170) {
      if (pet[pet.length-1]==="y") {
        spy = true;
      }
    }
  }
}


if (spy) {
  console.log("Welcome secret agent");
}else {
  console.log("Nothing to see here");
}
