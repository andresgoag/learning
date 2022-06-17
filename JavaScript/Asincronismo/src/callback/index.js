// Callbacks
// crear una funcion que recibe como argumento otra funcion


function sum(num1, num2) {
    return num1 + num2;
}


function calc(num1, num2, callback) {
    return callback(num1, num2)
}


console.log(calc(2, 7, sum));




function printDate(dateNow) {
    console.log(dateNow);;
}

function date(callback) {
    console.log(new Date);
    setTimeout(function () {
        let date = new Date;
        callback(date);
    }, 3000)
}


date(printDate);