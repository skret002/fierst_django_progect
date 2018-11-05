$(document).ready(function() {
    $('#hamburger').click(function(event){
        event.preventDefault();
        var item = $("#hamburger");
        var hid_menu = $('.menu-line');
        var nav_back = $('.filter_correct');
        var width = $(window).width();
        if (hid_menu.css('display') == 'none'){
            hid_menu.css('display','block');
            nav_back.css("width",width);
            hid_menu.css("width",(width-30));
            item.removeClass('hamburger-nav').addClass('hamburger-too');
            console.log(width);
        }
        else{hid_menu.css('display','none')
        item.removeClass('hamburger-too').addClass('hamburger-nav');;
        };
        
 });
});
