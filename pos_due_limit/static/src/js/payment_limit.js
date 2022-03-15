odoo.define('pos_due_limit.payment_limit', function (require) {
    "use strict";
var models = require('point_of_sale.models');
var core = require('web.core');
var _t = core._t;
const { Gui } = require('point_of_sale.Gui');
const Registries = require('point_of_sale.Registries');
const PosComponent = require('point_of_sale.PosComponent');
const PaymentScreen = require('point_of_sale.PaymentScreen');
models.load_fields('res.partner','limit');

const LimitPaymentScreen = (PaymentScreen) =>

    class extends PaymentScreen {


    async validateOrder(isForceValidate) {
                console.log(this.env.pos.get_order().get_total_with_tax())
                console.log(this.env.pos.get_client().limit)
                if(this.env.pos.get_client()){
                if(this.env.pos.get_order().get_total_with_tax() > parseFloat(this.env.pos.get_client().limit))
                {
                    Gui.showPopup("ErrorPopup", {
                                            'title': _t("Can't Validate"),
                                            'body':  _t("Due limit exceeds."),
                                        });
                }
                else
                {
                    await super.validateOrder(...arguments)
                }}else{
                await super.validateOrder(...arguments)}
//            {
//                if(this.env.pos.config.cash_rounding) {
//                    if(!this.env.pos.get_order().check_paymentlines_rounding()) {
//                        this.showPopup('ErrorPopup', {
//                            title: this.env._t('Rounding error in payment lines'),
//                            body: this.env._t("The amount of your payment lines must be rounded to validate the transaction."),
//                        });
//                        return;
//                    }
//                }
//                if (await this._isOrderValid(isForceValidate)) {
//                    // remove pending payments before finalizing the validation
//                    for (let line of this.paymentLines) {
//                        if (!line.is_done()) this.currentOrder.remove_paymentline(line);
//                    }
//                    await this._finalizeValidation();
//                }
//            }
        }
    }
Registries.Component.extend(PaymentScreen, LimitPaymentScreen);
return PaymentScreen;
    })