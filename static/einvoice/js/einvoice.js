$(function() {

    $('#sidebar-btn').on('click', function () {
        $('#sidebar').toggleClass('lifeplus-sidebar lifeplus-sidebar-toggle');
        $('#page-wrapper').toggleClass('col-md-12 col-md-9');
    });

    $('#page-wrapper').click(function(){
        var sidebar_class = $('#sidebar').attr('class');
        if( sidebar_class.indexOf('lifeplus-sidebar-toggle') != -1 ){
            $('#sidebar').toggleClass('lifeplus-sidebar lifeplus-sidebar-toggle');
            $('#page-wrapper').toggleClass('col-md-12 col-md-9');
        }
    });
});

