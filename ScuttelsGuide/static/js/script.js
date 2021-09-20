//Decimal To Hex
function decimalToHex(number){
  if (number < 0){
    number = 0xFFFFFFFF + number + 1;
  }
  return number.toString(16).toUpperCase();
}
// Pop Over
$('i').click(function(){  
  var dem =  $(this).text().charCodeAt(0);
  var code = decimalToHex(dem);
  var popover = '<div class="popover"><span class="close">&times;</span><div> Hex Code <p>&#x<span>'+ code +'</span>;</p></div><div>usage examples <p class="exm">  &lt;p&gt; &#x<span>'+code+'</span>;  &lt;/p&gt;</p></div></div>'
  
  $('.popover').remove();
   $('li').removeClass('active');
  $(this).parent().addClass('active').append(popover);;
});

// Close
$(document).on('click', '.close' ,function(){
  $('.popover').fadeOut();
   $('li').removeClass('active');
});

//Out Click
$(document).on('click', function(event) {
  if (!$(event.target).closest('.popover, i').length) {
  $('.popover').fadeOut();
   $('li').removeClass('active');
  }
});
// Emtt search box

$('.emty').click(function(){
  $('.search').val('');
  $(this).fadeOut().removeClass('hide');
  $('li').show();
});

//search
$('.search').keyup(function(){
 var val = $(this).val().toLowerCase();
  if(0< val.length){
    $('.header').addClass('hide');
    $('.emty').fadeIn();
  }
  else{
     $('.header').removeClass('hide');
    $('.emty').fadeOut();
  }
  
   $('li').each(function()
   {
     var text = $(this).text();
     if(text.indexOf(val)==-1)
       {
         $(this).hide();
       }
     else
       {
           $(this).show();
       }
       
   })
});