$(document).ready(function(){
  $('.number').first().css("color", "#64dc64");
  $('li').click(function(){
    var setNum = $(this).find("span.number").html()
    var randNum = Math.floor(Math.random() * 11) + 10;
    var newNum = parseInt(setNum) + randNum;
    $(this).find("span.number").text(newNum);
  });
});