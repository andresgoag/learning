// Funcion normal 

const moneyBox = (coins) => {
    var saveCoins = 0;
    saveCoins += coins;
    console.log(`Moneybox: $${saveCoins}`);
}

// al ejecutar la funcion normal, no se guardara el valor pasado anteriormente,
// lo cual deja inutil el operador de adicionar.
moneyBox(5);
moneyBox(10);






// Closure

const moneyBox = () => {
    var saveCoins = 0;
    const countCoins = (coins) => {
        saveCoins += coins;
        console.log(`Moneybox: $${saveCoins}`);
    }
    return countCoins;
}

let myMoneyBox = moneyBox();

myMoneyBox(4);
myMoneyBox(6);
myMoneyBox(10);