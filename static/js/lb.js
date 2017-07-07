$(document).ready(function(){
  myVar = "";
  $('.number').first().css("color", "#64dc64");
  $('.assign').click(function(){
    myVar = setInterval(function(){var i = 0;
    while (i < 4){
      var r = Math.floor((Math.random() * $('ul li').length) + 1);
    console.log(r);
    var $thisLi = $('li:nth-child(' + r + ')');
    var setNum = $thisLi.find("span.number").html()
    var randNum = Math.floor(Math.random() * 6) + 5;
    var newNum = parseInt(setNum) + randNum;
    $thisLi.find("span.number").text(newNum);
      i++;
    }}, 200);  
  });
  $('.stop').click(function(){
    clearInterval(myVar);
  });
});