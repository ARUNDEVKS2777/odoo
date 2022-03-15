odoo.define('website_recent_products.recent_view',function(require){
    'use strict';

//    var Animation = require('website.content.snippets.animation');
    var ajax = require('web.ajax');
    const config = require('web.config');
    const core = require('web.core');
    const publicWidget = require('web.public.widget');

    const DynamicSnippetProduct = publicWidget.Widget.extend({
        selector : '.recent_view_product_snippet_class',
        start : function() {
            var self = this;
            ajax.jsonRpc('/get_product', 'call', {})
            .then(function (data) {
                if(data){
                    self.$target.empty().append(data);
                }
            });
        }
        })
        publicWidget.registry.recent_view = DynamicSnippetProduct;

return DynamicSnippetProduct;
})