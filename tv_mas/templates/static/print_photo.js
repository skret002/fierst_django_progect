'use strict';
var FullPrice = 0
$(document).ready(function() {
	var add_photo_h = $('#add_photo').innerHeight();
	if (screen.width <= '760'){
		console.log(add_photo_h);
		$('.add_file span').text('фото');
	};
	// Прослушка события смены ориентации
	window.addEventListener("orientationchange", function() {
    // Выводим числовое значение ориентации
		orient = window.orientation;
		if ((orient = 0) && (screen.width <= '568')) {
			location.reload();
		};
	}, false);
});
$(document).ready(function() {
	var height_animate = $('.top_animate').height();
	$('.top_animate').height(0);
    $(".particles-button").click( function() {
        $('.left').delay(650).animate({
            left: '-=9999',
          }, 2500, function() {
            // Закончили анимацию.
          });
        $('.right').delay(650).animate({
          left: '+=9999',
        }, 2500,function() {
          // Закончили анимацию.
		});
		$('.top_animate').delay(650).animate({
			height: height_animate,
		  }, 2500,function() {
			$('.right').css('display','none');
			$('.left').css('display','none');			// Закончили анимацию.
		  });

});
});
//*************CASTOM INPUT FILE*************** */
;( function( $, window, document, undefined )
{
	$( '.inputfile' ).each( function()
	{
		var $input	 = $( this ),
			$label	 = $input.next( 'label' ),
			labelVal = $label.html();

		$input.on( 'change', function( e )
		{
			var fileName = '';

			if( this.files && this.files.length > 1 )
				fileName = ( this.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', this.files.length );
			else if( e.target.value )
				fileName = e.target.value.split( '\\' ).pop();

			if( fileName )
				$label.find( 'span' ).html( fileName );
			else
				$label.html( labelVal );
		});

		// Firefox bug fix
		$input
		.on( 'focus', function(){ $input.addClass( 'has-focus' ); })
		.on( 'blur', function(){ $input.removeClass( 'has-focus' ); });
	});
})( jQuery, window, document );

//*****CASTOM SELECT****** */
$(document).ready(function() {
	$('.dropdown').click(function() {
  $(this).attr('tabindex', 1).focus();
  $(this).toggleClass('active');
  $(this).find('.dropdown-menu').slideToggle(300);
});
$('.dropdown').focusout(function () {
  $(this).removeClass('active');
  $(this).find('.dropdown-menu').slideUp(300);
});
$('.dropdown .dropdown-menu li').click(function () {
	$(this).parents('.dropdown').find('span').text($(this).text()).attr('data-price1',$(this).data("price1"))
																												.attr('data-price2',$(this).data("price2"))
																												.attr('data-price3',$(this).data("price3"))
																												.attr('value',$(this).val())
																												.attr('id','take_data');

  $(this).parents('.dropdown').find('input').attr('value', $(this).attr('value'));
});
$('.dropdown-menu li').click(function () {
	var input = '<strong>' + $(this).parents('.dropdown').find('input').val() + '</strong>',
	msg = '<span class="msg">Hidden input value: ';
	$('.msg').html(msg + input + '</span>');
	});
	});
/*End Dropdown Menu*/

																/***ADD INLINE ADDCARD*** */
	var id = 0;
	$("#psevdo_click").on('click', function(){
			id = id+1;
			//console.log(id);
			$("#line_order_clear").clone().removeClass('hidden').removeAttr("id").attr('id',id).addClass("line_order").appendTo(".in_line_add");
			$("#psevdo_click").appendTo("#"+id);
			$(".line_order:last-child  div.add_file input").attr('id','file-'+ id);
			$(".line_order:last-child  div.add_file label").attr('for','file-'+ id);
			$(".line_order:last-child  div.add_file input").attr('name','file-'+ id);
			$(".line_order:last-child  div.count_copy input").attr('name','count_copy_'+ id);
			$(".line_order:last-child  div.type_photo input").attr('name','type_photo_'+ id);
			$(".line_order:last-child  div.field_select input").attr('name','field_select_'+ id);
			$(".line_order:last-child  div.time input").attr('name','time_'+ id);
			$(" div.count_line input").val(id);

			/******** тут пришлось отдублировать функции сверху************ */

//*************CASTOM INPUT FILE*************** */
	;( function( $, window, document, undefined )
	{
		$( '.inputfile' ).each( function()
		{
			var $input	 = $( this ),
				$label	 = $input.next( 'label' ),
				labelVal = $label.html();
			$input.on( 'change', function( e )
		{
				var fileName = '';

				if( this.files && this.files.length > 1 )
					fileName = ( this.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', this.files.length );
				else if( e.target.value )
					fileName = e.target.value.split( '\\' ).pop();

				if( fileName )
					$label.find( 'span' ).html( fileName );
				else
					$label.html( labelVal );
		});

		// Firefox bug fix
		$input
			.on( 'focus', function(){ $input.addClass( 'has-focus' ); })
			.on( 'blur', function(){ $input.removeClass( 'has-focus' ); });
		});
})( jQuery, window, document );

//*****CASTOM SELECT TWO****** */

	$('.dropdown').click(function() {
  	$(this).attr('tabindex', 1).focus();
	$(this).toggleClass('active');
	$(this).find('.dropdown-menu').slideToggle(300);
									});
	$('.dropdown').focusout(function () {
	$(this).removeClass('active');
	$(this).find('.dropdown-menu').slideUp(300);
										});
	$('.dropdown .dropdown-menu li').click(function () {
	$(this).parents('.dropdown').find('span').text($(this).text()).attr('data-price1',$(this).data("price1"))
																												.attr('data-price2',$(this).data("price2"))
																												.attr('data-price3',$(this).data("price3"))
																												.attr('value',$(this).val())
																												.attr('id','take_data');

  $(this).parents('.dropdown').find('input').attr('value', $(this).attr('value'));
														});
	$('.dropdown-menu li').click(function () {
		var input = '<strong>' + $(this).parents('.dropdown').find('input').val() + '</strong>',
		msg = '<span class="msg">Hidden input value: ';
		$('.msg').html(msg + input + '</span>');
										});

/*End Dropdown Menu*/
});

var count =0;
var idh = ($('.line_order:last-child').attr('id'));
	if (idh==0){
		$('#'+idh+' input[type=file]').on('change', function() {
			count = (this.files.length);
			console.log('ID'+idh);
			console.log(count);
	});

//	$('#'+idh+'.dropdown .dropdown-menu li').click(function () {
//		$(this).parents('.dropdown').find('span').text($(this).text());
//		$(this).parents('.dropdown').find('input').attr('value', $(this).attr('id'));
//	});
//	$('#'+idh+'.dropdown-menu li').click(function () {
//				var input = '<strong>' + $(this).parents('.dropdown').find('input').val() + '</strong>',
//				msg = '<span class="msg">Hidden input value: ';
//				$('.msg').html(msg + input + '</span>');
//	});

$('#'+idh+' ul:eq(0) li').on('click', function() {
	$('#'+idh+' ul:eq(0)').on('click', function (event) {
		var copy = $('#'+idh+' #select1-1 input').val(); 
		var el = event.target || e.srcElement;
		var p1 = parseInt($(el).data('price1'));
		var p2 = parseInt($(el).data('price2'));
		var p3 = parseInt($(el).data('price3'));
		if((count * copy) <= 20){
			var ready_price = ((p1 * copy) * count);
		}
		else if((count * copy) > 20 && (count * copy) <= 100){
			var ready_price = ((p2 * copy) * count);
		}else if((count * copy) > 100){
			var ready_price = ((p3 * copy) * count);
		};
		FullPrice = FullPrice + ready_price;
		if (screen.width <= '760'){
			$('.line_order:last-child .price_in_line p').text(ready_price + "р"+" ");
		}else{
			$('.line_order:last-child .price_in_line p').text(ready_price + " " + "руб.");
		};

});});};
$('.copy_line').on('click' ,function LineOrder(idh){
	idh = ($('.line_order:last-child').attr('id')); 
	var count = 0;
	function CountFile(idh){$('#'+idh+' input[type=file]').on('change', function() {
	count = (this.files.length);
});};
	CountFile(idh);
	function OrderSum(idh){$('#'+idh+' ul:eq(0) li').on('click', function() {
	$('#'+idh+' ul:eq(0)').on('click', function (event) {
		var copy = $('#'+idh+' #select1-1 input').val();
		var el = event.target || e.srcElement;
		var p1 = parseInt($(el).data('price1'));
		var p2 = parseInt($(el).data('price2'));
		var p3 = parseInt($(el).data('price3'));
		if((count * copy) <= 20){
			var ready_price = ((p1 * copy) * count);
		}
		else if((count * copy) > 20 && (count * copy) <= 100){
			var ready_price = ((p2 * copy) * count);
		}else if((count * copy) > 100){
			var ready_price = ((p3 * copy) * count);
		};
		FullPrice = FullPrice + ready_price;
		if (screen.width <= '760'){
			$('.line_order:last-child .price_in_line p').text(ready_price + "р"+" ");
		}else{
			$('.line_order:last-child .price_in_line p').text(ready_price + " " + "руб.");
		};
});})};
	OrderSum(idh);
});


$("#psevdo_click").click(function(){
	var height_block = $('.top_animate').height();
	var height_line = $('.line_order').outerHeight(true);
	$('.top_animate').height(height_block+height_line);
});

//* SEND FORM  */
$("#submit").click( function(event) {
	$(".content").css('opacity','-2');
	$("body").css('background','linear-gradient(278deg, #051017, #101552)');
	$("#preload").removeClass('hidden');
	$("#loader").css('top',(screen.height/2));
	event.preventDefault();
	$('#fullprice').val(FullPrice);
	var formData = new FormData($('#order_photo')[0]);
	var form = $('form');
	var formAction = $(form).attr('action');
    $.ajax({
           url: formAction, 
           data: formData,
           async: false,
           contentType: false,
           processData: false,
           cache: false,
           type: 'POST',
        success: function (data) {
			console.log(data);
			$('.top_animate').delay(650).animate({
				height: '0',
			  }, 2500,function() {
				// Закончили анимацию.
			  });
		setTimeout(function() {
			$(".content").css('opacity','2');
			$("body").css('background','none');
			$("#preload").addClass('hidden');

			$('#success_message').removeClass('hidden');
            $(".num_order").append(' '+data.number_order_new+' ');
            $(".sber").append(' '+data.namber_bank_respondent);
            $(".sber_phone").append(' '+data.phone_respondent);
			$(".corespondent").append(' '+data.name_respondent);  
			$(".check_price").append(' '+FullPrice);
		}, 2000);
         }, 
        error: function () {
			$(".content").css('opacity','2');
			$("body").css('background','none');
			$("#preload").addClass('hidden');
            alert("Заказ не оформлен! Что то заполнено не верно!");
        }});    
    });