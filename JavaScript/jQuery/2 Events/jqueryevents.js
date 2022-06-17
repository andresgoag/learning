//Referencia para eventos de jQuery
//https://api.jquery.com/category/events/


//Referencia para efectos de jQuery
//https://api.jquery.com/category/effects/

$('h1').click(function(){
  console.log('click on h1');
})



$('li').click(function(){
  console.log('any li item clicked');
})



$('h1').click(function(){
  $(this).text("I was clicked so i change my text")
})





// Key Press


$('input').keypress(function(){
  $('h3').toggleClass("turnBlue");
})



$('input').keypress(function(event){
  console.log(event);
  if (event.which === 13) {
    $('li').eq(3).toggleClass("turnBlue");
  }
})







// On Method

$('h2').on('dblclick', function(){
  $(this).toggleClass('turnRed');
})


$('li').eq(0).on('mouseenter',function(){
  $(this).toggleClass('turnBlue');
})








// Efects

$('input').eq(1).on("click", function(){
  $(".container").fadeOut(3000);
})



$('p').on("click", function(){
  $(".container").slideUp(3000);
})
