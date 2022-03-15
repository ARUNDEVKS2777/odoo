odoo.define('pos_due_limit.due_limit', function (require) {
    "use strict";
var models = require('point_of_sale.models');
var core = require('web.core');
var _t = core._t;
const { Gui } = require('point_of_sale.Gui');
const Registries = require('point_of_sale.Registries');
const PosComponent = require('point_of_sale.PosComponent');
const OrderWidget = require('point_of_sale.OrderWidget');
const ClientListScreen = require('point_of_sale.ClientListScreen');
models.load_fields('res.partner','limit');


const LimitOrderWidget = (OrderWidget) =>

    class extends OrderWidget {
        async _updateSummary() {
//            const total = this.order ? this.order.get_total_with_tax() : 0;
            if(this.env.pos.get_client())
            {

                if(parseFloat(this.env.pos.get_client().limit) < this.order.get_total_with_tax())
                {
                    await super._updateSummary()
                    Gui.showPopup("ErrorPopup", {
                                        'title': _t("Warning"),
                                        'body':  _t("Due limit exceeds."),
                                    });

                }
//                await super._updateSummary()
            }
            await super._updateSummary()

        }
    }
Registries.Component.extend(OrderWidget, LimitOrderWidget);
return OrderWidget;
    })