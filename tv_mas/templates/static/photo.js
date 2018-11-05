$(document).ready(function() {
    $( '#select_document' ).change(function() {
        var select_value = $('#select_document').val();
        form = $(this).closest('form')
        var formAction = $(form).attr('action');
        $('#ukazatel').addClass("hidden");
        

        $.post(formAction, { id_doc:select_value,}, function (data) { 
            var name_document = data.name_document;
            var count = data.count;
            var options_photo = data.options_photo;
            var full_price_photo = data.full_price_photo;
            var edit_price_photo = data.edit_price_photo;
            var image_preview = data.image_preview;
            $('#img_prev').attr('src', '/static/media/' + image_preview);
            $('.name_document').empty().append('Вы выбрали:'+' ' + '<stromg style="color:#FBB100;font-weight: 700;">'+ name_document +'</strong>');
            $('.count').empty().append('Кол-во фото в блоке:'+' ' + '<stromg style="color:#FBB100;font-weight: 700;">'+ count +'</strong>');
            $('.options_photo').empty().append('Параметры фото:'+' ' + '<stromg style="color:#FBB100;font-weight: 700;">'+ options_photo +'</strong>');
            $('.full_price_photo').empty().append('Цена (обработка и печать блока) -'+' ' + '<b style="color:#FBB100;font-weight: 700;">'+full_price_photo+' '+'руб.'+'</b>');
            $('.edit_price_photo').empty().append('Цена (обработка) -'+' ' +  '<b style="color:#FBB100;font-weight: 700;">'+edit_price_photo +' '+'руб.'+'</b>');
            $('#id_order').empty().append('фото на'+' ' +name_document);
            $('#show_order').removeClass( "hidden" );
    });
});

});

$('#img').change(function () {
    var input = $(this)[0];
    if (input.files && input.files[0]) {
        if (input.files[0].type.match('image.*')) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#reset-img-preview').removeClass("hidden");
                $('#img_primer_chaild').addClass("hidden");
                $('#img-preview').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        } else {
            console.log('');
        }
    } else {
        console.log('');
    }
});

$('#reset-img-preview').click(function() {
    $('#reset-img-preview').addClass("hidden");
    $('#img').val('');
    $('#img-preview').attr('src', '{% static'+'' + 'primer_photo_child.jpg'+'' +'%}');
});

$('#form').bind('reset', function () {
    $('#reset-img-preview').addClass("hidden");
    
    $('#img-preview').attr('src', '{% static'+'' + 'primer_photo_child.jpg'+'' +'%}');
});

$("#submit").click( function(event) {
    event.preventDefault();

    var phone_validate= $("#phone").val().length;
    if (phone_validate!=12){
        alert("Номер тел. заполнен не верно! Формат +7xxxxxxxxxx");
        $('#phone').css( {"color": "white", "background-color":"red" });
        throw new Error("stop");
    };
    if(($("#img").val().length)<1){
        alert("Вы забыли приложить фото!");
        throw new Error("stop");
    };
    if(($("#first_name").val().length)<1){
        alert("Заполните поле - Имя ");
        throw new Error("stop");
    };
    if(($("#email").val().length)<4){
        alert("Заполните поле - E-Mail ");
        throw new Error("stop");
    };

    var formData = new FormData($('#order_photo')[0]);
    
    
    var form = $(this).closest('form')
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
            edit_price_photo = data.edit_price_photo;
            full_price_photo =  data.full_price_photo;
            $(".num_order").append(data.number_order);
            $(".sber").append(data.namber_bank_respondent);
            $(".sber_phone").append(data.phone_respondent);
            $(".corespondent").append(data.name_respondent);
            $('#order_photo input:checkbox:checked').each(function(){
                check_task=($(this).val());
                });
                if(check_task== 1){
                    $('#s_two').addClass("hidden");
                }else{
                    $('#s_one').addClass("hidden");
                }
            $( '#order_photo').slideToggle( 1000, function() {
                $('#success_message').removeClass( "hidden" );  
            });
               $('#order_photo input:checkbox:checked').each(function(){
                check_task=($(this).val());
            });
            if(check_task== 1){
                $('#s_two').addClass("hidden");
            }else{
                $('#s_one').addClass("hidden");
            };
            if (check_task == 1){
                $('#check_price').append(edit_price_photo + 'руб.');
            };
            if  (check_task == 2){
                $('.check_price').empty().append(full_price_photo + 'руб.');
            };
            if  (check_task == 3){
                var sum = (parseInt(edit_price_photo) + parseInt(full_price_photo));
                $('.check_price').empty().append(sum + 'руб.');
            };
            
              
         }, 
        error: function () {
            alert("Заказ не оформлен! Что то заполнено не верно!")
        
        }});    
    });