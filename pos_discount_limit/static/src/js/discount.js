odoo.define('pos_discount_limit.DiscountLimit', function (require) {
    "use strict";

    var models = require('point_of_sale.models');
    var field_utils = require('web.field_utils');
    const Registries = require('point_of_sale.Registries');
    var core = require('web.core');
    const _t = core._t;
    const { Gui } = require('point_of_sale.Gui');
    models.load_fields('pos.config', 'discount_limit');
    models.load_fields('pos.category', 'config');
    models.load_fields("hr.employee","cashier");
    models.load_fields('pos.config','manual_discount');
    const PosComponent = require('point_of_sale.PosComponent');
    const NumpadWidget = require('point_of_sale.NumpadWidget');

    var _super_order_line = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        set_discount: function(discount){
            var order = this.pos.get_order();
            var pos_prod_id = order.selected_orderline.product.pos_categ_id[0]
            if(this.pos.config.discount_config == false){

                var parsed_discount = isNaN(parseFloat(discount)) ? 0 : field_utils.parse.float('' + discount);
                var disc = Math.min(Math.max(parsed_discount || 0, 0),100);
                this.discount = disc;
                this.discountStr = '' + disc;
                this.trigger('change',this);
            }
            else
            {
                var rounded = Math.round(discount);

                console.log('discunt',discount)
                console.log('rounded',rounded)
                if(Number.isInteger(pos_prod_id))
                {
                    if(this.pos.db.category_by_id[pos_prod_id].config == true)
                    {
                        if(this.pos.get_cashier().role === 'manager')
                        {
                            if(rounded > this.pos.config.discount_limit){
                                discount = 0;
                                rounded = 0;
                                Gui.showPopup("ErrorPopup", {
                                    'title': _t("Discount Not Possible"),
                                    'body':  _t("You cannot apply discount above %s" %(this.pos.config.discount_limit)),
                                });
                            }
                            else {
                                var parsed_discount = isNaN(parseFloat(rounded)) ? 0 : field_utils.parse.float('' + rounded);
                                var disc = Math.min(Math.max(parsed_discount || 0, 0),100);
                                this.discount = disc;
                                this.discountStr = '' + disc;
                                this.trigger('change',this);
                            }
                        }
                        else
                        {
                            rounded = 0.0;
                                this.pos.get_order().get_selected_orderline().set_discount(discount)
                               Gui.showPopup("ErrorPopup", {
                                'title': _t("Discount Not Possible"),
                                'body':  _t("You cannot apply discount to this category."),
                            });
                        }
//                        {
//                            this.pos.config.manual_discount = false
//                        }
//                        else
//                        {
//                             this.pos.config.manual_discount = true
//                        }

                        }
                    else
                    {
                        var parsed_discount = isNaN(parseFloat(rounded)) ? 0 : field_utils.parse.float('' + rounded);
                        var disc = Math.min(Math.max(parsed_discount || 0, 0),100);
                        this.discount = disc;
                        this.discountStr = '' + disc;
                        this.trigger('change',this);
                    }
                }
            }
        }
    })
    });