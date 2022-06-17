function add(){
  name = prompt("Enter the student name to add:");
  roster.push(name);
}

function remove(){
  name = prompt("Enter the student name to remove:");
  var index = roster.indexOf(name);
  roster.splice(index,1);
}


function display(){
  console.log(roster);
}





var start;
var action;
var roster = []

start = prompt("Would you like to start the roster web app? y/n");
if (start == "y") {
  while (true) {
    action = prompt("Please select an action: add, remove, display, or quit.");
    if (action == "add") {
      add();
    }else if (action == "remove") {
      remove();
    }else if (action == "display") {
      display();
    }else if (action == "quit") {
      break;
    }
  }
}


else {
  alert("Thank you for using the Web App! Please refresh the page to start over");
}
