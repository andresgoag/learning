const person = () => {
    var saveName = "Name";
    return {
        getName: () => {
            return saveName;
        },
        setName: (name) => {
            saveName = name;
        }
    };
};


newPerson = person();
console.log(newPerson.getName());
newPerson.setName('Oscar');
console.log(newPerson.getName());


// De esta manera saveName se convierte en una variable provada, a la cual no se tiene acceso, solo se podra modificar con los 
// metodos establecidos para esto.