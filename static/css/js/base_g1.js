
"use strict";

var g1_controller = (function($){

    var name = 'g1_controller';

    return {



        init: function(){

            var self = this;

            // form validation
//            $("form").submit(function( event ) {
//                if(self.validateForm()) return
//                event.preventDefault();
//            });
        },

        validateForm: function(){

            var pass = true;

            if( $("#id_ubn").val().length != 8 ){
                $("#id_ubn_div").addClass("has-error");
                $("#id_ubn").val("");
                return false;
            }
        },
    };

})(jQuery);

// document ready
$(function(){
    g1_controller.init();
});
