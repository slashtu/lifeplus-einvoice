$(function() {

    $('#sidebar-btn').on('click', function () {
        $('#sidebar').toggleClass('hidden col-md-3');
        $('#page-wrapper').toggleClass('col-md-12 col-md-9');
    });

});

