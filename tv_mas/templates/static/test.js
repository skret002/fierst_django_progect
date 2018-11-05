if ({
        { m }
    } == '1') {
    $("div").removeClass('hidden');
} else {
    $("#choise_field").fadeToggle(1200);
}
if ({
        {
            m
        }
    } == '2') {
    $("div").removeClass('form_is_none_model');
}

$("#searche_again").click('#choise_field', function() {
    $("#choise_field").fadeTo(700, 1, function() {
        $("#param_a").fadeToggle(700);
    })
})