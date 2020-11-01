$('#searcher').keyup(function(){
    $('.box').show();
    var filter = $(this).val(); // get the value of the input, which we filter on
    $('.container-fluid').find(".company:not(:contains(" + filter + "))").parent().css('display','none');
})
$('#but').on('click',function(){

    var filter = $('#searcher').val(); // get the value of the input, which we filter on
    console.log(filter)
    $('.container-fluid').find(".company:not(:contains(" + filter + "))").parent().css('display','none');
})