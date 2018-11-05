

var have_url = $('#send_tv_service1').attr('action').replace('/None', '');
$('#select_model').change(function() {
    model_choise = $("#select_model option:selected").text();
    var target_url = $('#send_tv_service1').attr("action", have_url + model_choise +'/');
    console.log(target_url);
});

$(document).ready(function () {
    var form = $('#search_form');
    console.log(form);
    form.on('submit', function (e) {
        //e.preventDefault();
        console.log('123');
        var model = $('#model_tv_id').val();
        console.log(model);

        var data = {};
        data.model = model;
        //var url = form.attr("action");
        console.log(url);
        var url = form.attr("action");
        $.ajax({
            url: url,
            type: 'GET',
            data: data,
            cache: false,
            success: function (data) {
                console.log("ok");
                console.log(url);
            },
        });

    });
});

////////////////////////вкидываем проверку

    $(document).ready(function check(){

        $('#you_name').blur(function(checkname) {
            if ($(this).val() != '') {
                var pattern = /^([а-я_\.-])/i;
                if(pattern.test($(this).val())){
                    window.n=1;
                    $("#you_name").removeClass( "noValid" ).addClass( "phoneValid" ),
                    $("#get_form").removeClass( "hidden" ),
                    $("#mesege_error").addClass( "hidden" );
                    //$("#get_form").prop("disabled", false);

                }else {   
                    window.n=0;     
                    $("#get_form").addClass( "hidden" ),
                    $("#you_name").removeClass( "phoneValid" ).addClass( "noValid" );
                    //$("#get_form").prop("disabled", true);
                        };
            }else {
                    window.n=0;  
                    $(this).css({'border' : '2px solid #ff0000'}),
                    $('#valid').text('Поле email не должно быть пустым'),
                    $("#mesege_error").removeClass( "hidden" );
                    //$("#get_form").prop("disabled", true);
                };
                $("#phone").mask("+7(999) 999 99 99",{completed:function(){ // проверка телефона по маски
                    if($(this).val() != '') {
                        window.p=1;
                        //$("#get_form").prop("disabled", false),
                        $("#phone").addClass("phoneValid"),
                        $("#get_form").removeClass( "hidden" ),
                        $("#mesege_error").addClass( "hidden" );
                        }
                    else{
                        //$("#get_form").prop("disabled", true),
                        $(this).css({'border' : '2px solid #ff0000'}),
                        $('#valid').text('Поле email не должно быть пустым'),
                        $("#mesege_error").removeClass( "hidden" );
                        };

                        $('#you_email').blur(function() {
                            if($(this).val() != '') {
                                var pattern = /^([a-z0-9_\.-])+@[a-z0-9-]+\.([a-z]{2,4}\.)?[a-z]{2,4}$/i;
                                if(pattern.test($(this).val())){
                                window.e=1;  
                                $("#you_email").removeClass( "noValid" ).addClass( "phoneValid" );
                                $("#get_form").removeClass( "hidden" );
                                $("#mesege_error").addClass( "hidden" );
                                }else {
                                    $("#you_email").removeClass( "phoneValid" ).addClass( "noValid" );
                                     $("#get_form").addClass( "hidden" );
                                 };
                            }else{
                                    $(this).css({'border' : '2px solid #ff0000'});
                                    $('#valid').text('Поле email не должно быть пустым');
                                    $("#mesege_error").removeClass( "hidden" );
                               };
                               $('#you_question').blur(function() {
                                    if($(this).val() != '') {
                                        window.q=1;
                                            $("#you_question").removeClass( "noValid" ).addClass( "phoneValid" );
                                            $("#get_form").removeClass( "hidden" );
                                            $("#mesege_error").addClass( "hidden" );
                                    }else {
                                            
                                        
                                            $("#get_form").addClass( "hidden" );
                                            $("#mesege_error").removeClass( "hidden" );
                                            $("#you_question").removeClass( "phoneValid" ).addClass( "noValid" );
                                       };

                                       console.log(window.n)
                                        if (window['n'] == 1 && window['p'] == 1  && window['e'] == 1 && window['q'] == 1){
                                            $("#get_form").prop("disabled", false);
                                       }
                                        else{
                                            $("#get_form").prop("disabled", true);
                                            $("#mesege_error_field").removeClass( "hidden" );
                                       };  
                                });                          
                            });
                    }}
                    )   
            });
    });

  


////////////////////////вкидываем проверку




////////////////////////////////SEND FORM AT DJANGO///////////////////////////////////////////////

        $("#get_form").click( function(event) {
        event.preventDefault();
        console.log('form_q=EVENT');
        var formData = new FormData($('.form_q')[0]);
        console.log(formData);
        $.ajax({
               url: this.action, 
               data: formData,
               async: false,
               contentType: false,
               processData: false,
               cache: false,
               type: 'POST',
            success: function (data) {

                console.log("ok");
                $("#mesege").removeClass( "hidden" );
                $("#form_q").fadeToggle(300);
             }, 
            error: function () {
                console.log("ПОСТ НЕ УХОДИТ");
                $("#mesege_error").removeClass( "hidden" );
            
            }

             });    
        });

/////////////////////////////////////////////////////////////////////////////////


////////////////////////////////SEND FORM ZVONKA AT DJANGO///////////////////////////////////////////////


$('#id_name').blur(function(checkname) {
    if ($(this).val() != '') {
        var pattern = /^([а-я_\.-])/i;
        if(pattern.test($(this).val())){
            window.n=1;
        $("#id_name").addClass( "valid_m" ); 
        $("#valid").removeClass( "hidden" );
        $("#No_valid").addClass( "hidden" ); 
        $('#send_form').attr("value","name_valid");
        $("#send_form").prop("disabled", false);
        $("#alert").addClass("hidden");

        

        }else {   
            window.n=0;     
            $('#send_form').attr("value","no_valid");
            $("#id_name").addClass( "valid_m" );
            $("#No_valid").removeClass( "hidden" );
            $("#valid").addClass( "hidden" );
            $("#send_form").attr("disabled", true);
            $("#send_form").prop("disabled", true);
            $("#alert").removeClass("hidden");
                };
    }else {
            window.n=0;  
            $('#send_form').attr("value","no_valid");
            $("#id_name").addClass( "valid_m" );
            $("#No_valid").removeClass( "hidden" );
            $("#valid").addClass( "hidden" );
            $("#send_form").attr("disabled", true);
            $("#send_form").prop("disabled", true);
            $("#alert").removeClass("hidden");
        };
    });

    $("#id_phone").mask("+7(999) 999 99 99",{completed:function(){ // проверка телефона по маски
        if($(this).val() != '') {
            window.p=1;
            //$("#get_form").prop("disabled", false),
            $("#id_phone").addClass( "valid_m" ); 
            $("#valid_phone").removeClass( "hidden" );
            $("#No_valid_phone").addClass( "hidden" ); 
            $('#send_form').attr("value2","phone_valid");
            $("#send_form").prop("disabled", false);
            $("#alert").addClass("hidden");
            }
        else{
            //$("#get_form").prop("disabled", true),
            $('#send_form').attr("value","no_valid");
            $("#id_phone").addClass( "valid_m" );
            $("#No_valid_phone").removeClass( "hidden" );
            $("#valid_phone").addClass( "hidden" );
            $("#send_form").prop("disabled", true);
            $("#alert").removeClass("hidden");
            };
        }});

        $('#id_time_0, #id_time_1, #id_time_2, #id_time_3, #id_time_4, #id_time_5, #id_time_6').click(function(checkbox) {
           if ($(this).prop('checked') == true) {
                $('#send_form').attr("value3","time_valid");
                $("#send_form").prop("disabled", false);
                $("#alert").addClass("hidden");
              
           }
         else{
                $('#send_form').attr("value3","time_no_valid");
                $("#send_form").prop("disabled", true);
                $("#alert").removeClass("hidden");
               
            }

        });




$("#send_form").click( function(event) {
    event.preventDefault();
    console.log('form_q=EVENT');
    var formData = new FormData($('#call_order')[0]);
    console.log(formData);
    $.ajax({
           url: this.action, 
           data: formData,
           async: true,
           contentType: false,
           processData: false,
           cache: false,
           type: 'POST',
        success: function (data) {


        $(".call_order").fadeToggle(500);
        $("#post_form").show('600','swing')
         }, 
        error: function () {

        //    $("#mesege_error").removeClass( "hidden" );
        
        }

         });    
    });

