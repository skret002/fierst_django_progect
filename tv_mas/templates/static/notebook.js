$(document).ready(function() {
    $('#search_form').keydown(function(event){
      if(event.keyCode == 13) {
        event.preventDefault();
        return false;
    }
 });
});

var Search = (function(){
    $('#search_form').trigger('reset');
    $("#input_model").on('keyup  blur paste mouseenter mouseleave ', function(event) {
        event.preventDefault();
        var formData = $('#search_form').serialize();
        var path = "?"+formData
        $.ajax({
               url: this.action, 
               data: formData,
               async: true,
               contentType: false,
               processData: false,
               cache: false,
               type: 'GET',
            success: function (data) {
                window.history.pushState({route: path}, "EVILEG", path); // устанавливаем URL в строку браузера;
                    
            }, 
            error: function () {
            
            }});    

          
        });
        
            $("#input_model").on('keyup paste', function() {
            var formData = $('#result_form').serialize(); // result_form пустая форма скрытая с урлом

            setTimeout(function () {
            $.ajax({
                   url: '/remont_notebook_result.html/', 
                   data: formData,
                   async: true,
                   contentType: false,
                   processData: false,
                   cache: true,
                   type: 'GET',
                   success: function (json_dict) {

                    $("#alert_count_val").text(json_dict.count_val)
                    $(".quote_in_head").removeClass("hidden");
                    if (json_dict.count_val > 10){
                        $("#text-alert").removeClass( 'hidden');
                        $(".search").css('margin-top', 10);
                        $(".quote_in_head").removeClass("hidden");
                        $("#search_result").addClass( "hidden" );
                         }
                    else{
                        $("#text-alert").addClass("hidden");
                        $(".search").css('margin-top', 100);
                        $(".quote_in_head").addClass("hidden");
                        $("#search_result").removeClass( 'hidden');

                        //// Работаем с результатом в SELECT
                        $(".form_result_search").empty();
                        $(".form_result_search").append($("<option selected=selected> </option>").attr("class", "option_info" ).text("Подтвердите модель"));
                        $.each(json_dict.smarfon_data, function(index, value){
                            $(".form_result_search").append($("<option> </option>").attr("value", this.brend +'/'+ this.name + '/' + this.id).attr("id", "result_smartfon_search").text(this.name).append($("<div> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>").attr("class", "split" )).append($("<span> </span>").attr("id", "result_option_right").text(this.brend)));           
                            });
                        $.each(json_dict.smarfon_data_brend, function(index, value){
                            });
                                                  
                    };
                    if (json_dict.count_val == 'error_count_val'){
                        $("#text-alert").addClass( "hidden" );
                        $(".header_with_search").css('height', 500);
                        $("#error_count_val").removeClass( 'hidden');
                        $(".search").css('margin-top', 10);
                        $("#search_result").addClass( "hidden" );
                    }
                    else{
                    };

                },
                error: function () {
                }});    
    
            }, 1000);

            });
  
            $("select").change(function(){
                var url = ($(this).val());
                var paf = document.location.host +'/'+'remont_notebook'+'/' + url;
                location.replace("http://"+paf + '/1');  // устанавливаем URL в строку браузера + № страницы;
            });
        
})();

