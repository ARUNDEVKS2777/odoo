odoo.define('website_order_tracking.search_get',function(require){
    'use strict';
    var ajax = require('web.ajax');
    const config = require('web.config');
    const core = require('web.core');

    $('#track_form').on('click', 'button.btn btn-info fa fa-search', function(e) {
    e.preventDefault();
    console.log("eeeee")
    var num_A = $( ".form-control" ).val();
//    var num_B= $( ".num_B" ).val();

    ajax.jsonRpc('/track_view', 'call', {'a': num_A})
            .then(function(result){
                    console.log(result);
//                    var output_data=result['total'];
//                    console.log(output_data);
//                    $("#total").html(output_data);

                });
    });
    })

