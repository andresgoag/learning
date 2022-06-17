var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength: function(){ // Add a method called nameLength that prints out the length of the employees name to the console.
    console.log(this.name.length);
  },
  report: function(){ // Write program that will create an Alert in the browser of each of the object's values for the key value pairs. For example, it should alert: Name is John Smith, Job is Programmer, Age is 31.
    alert("Name is: "+this.name+", Job is: "+this.job+", Age is: "+this.age)
  },
  lastName: function(){ // Add a method called lastName that prints out the employee's last name to the console.
    console.log(this.name.split(" ")[1]);
  }
}
