from odoo import api, fields, models, _


class PaymentPos(models.TransientModel):
    _name = 'payment.pos.wizard'

    pay_line_ids = fields.One2many('pay.line', 'refer')
    so = fields.Many2one('sale.order')

    def action_payment(self):
        self.so.state = 'pay_at_the_counter'
        # print(self.name)
        pos_config = self.env['pos.config'].search([('id', '=', 34)])
        pos_session = self.env['pos.session'].search([('config_id', '=', pos_config.id)])
        print(pos_session)
        # pos_session.action_pos_session_close()
        listed = []
        payment = []
        for rec in self.pay_line_ids:
            pay = {
                'payment_method_id': rec.pay_method_id.id,
                'amount': rec.paid_amt
            }
            payment.append((0, 0, pay))
        for line in self.so.order_line:
            record = {
                'product_id': line.product_id.id,
                'full_product_name': line.product_id.name,
                'qty': line.product_uom_qty,
                'product_uom_id': line.product_uom_qty,
                'price_unit': line.price_unit,
                'price_subtotal': line.price_subtotal,
                'price_subtotal_incl': line.price_subtotal
            }
            listed.append((0, 0, record))
        pos_order = self.env['pos.order'].create({'name': self.so.name,
                                                  'session_id': pos_session.id,
                                                  'amount_tax': 0.0,
                                                  'amount_total': self.so.amount_total,
                                                  'amount_paid': 0.0,
                                                  'amount_return': 0.0,
                                                  # 'user_id': self.env.user,
                                                  'partner_id': self.so.partner_id.id,
                                                  'payment_ids': payment,
                                                  'lines': listed,
                                                  'so_id': self.so
                                                  })
        # self.so.state = 'pay_at_the_counter'
        # print(self.so.state)


class PayLine(models.TransientModel):
    _name = 'pay.line'

    pay_method_id = fields.Many2one('pos.payment.method', string='Method')
    total_amt_paid = fields.Float(string='Total Amount Paid')
    paid_amt = fields.Float(string='Paid Amount')
    remaining_amt = fields.Float(string='Remaining Amount')
    refer = fields.Many2one('payment.pos.wizard')



