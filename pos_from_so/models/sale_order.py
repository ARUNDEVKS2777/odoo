from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _default_session(self):
        return self.env['pos.session'].search([('state', '=', 'opened')])

    session = fields.Many2one('pos.session', string="Session",
                              default=_default_session)
    bool = fields.Boolean(default=False)
    state = fields.Selection(
        selection_add=[('pay_at_the_counter', 'Pay at the Counter')])


class PaymentWizard(models.TransientModel):
    _inherit = 'pos.make.payment'

    def check(self):
        checked = super(PaymentWizard, self).check()
        print('hh')

        return checked


class PosState(models.Model):
    _inherit = 'pos.order'

    so_id = fields.Integer()

    @api.constrains('state')
    def stated(self):
        print(self.state)
        if self.state == 'paid':
            so_bool = self.env['sale.order'].search([('id', '=', self.so_id)])
            so_bool.bool = True

