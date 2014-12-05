"use strict";

var registerStaff_controller = (function($){

    var name = 'register-staff_controller';

    var store_array = [];

    return {
        init: function(){

            this._setTreeLeaf();

            $('#submit-button').on('click', function(){

//                var input =
//
//                $('#staff-form').attr('name', 'store').val('lifeplus');
//                event.preventDefault();
            });

//            var self = this;

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

        _setTreeLeaf: function(){

            $('.leaf').on('click', function(){

                /* set ui */
                $(this).toggleClass('selected-leaf');

                /* leaf operation */
                var isSelected = $(this).hasClass('selected-leaf');

                if( isSelected ){
                    /* add leaf to list */
                }else{
                    /* remove leaf to list */
                }
            });
        },

        _addStore: function( store ){

            this.store_array.push(store);
        },

        _removeStore: function( store ){


        }
    };

})(jQuery);

// document ready
$(function(){
    registerStaff_controller.init();
});
