from odoo import api, fields, models


class SaleRepair(models.Model):
    _name = "inventory.repair"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Inventory Repair"

    sale_order_id = fields.Many2one('sale.order', string='Sale Order')
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirm'),
                              ('done', 'Done')], default='draft')
    product_id = fields.Many2one('product.product', string='Product')
    customer_id = fields.Many2one('res.partner', string='Customer',
                                  related='sale_order_id.partner_id')

    @api.onchange('sale_order_id')
    def select_customer(self):
        if self.sale_order_id:
            self.sale_order_id.repair = True
            orderslist = []
            orders = self.sale_order_id.order_line.product_id
            for rec in orders:
                orderslist.append(rec.id)
            return {'domain': {'product_id': [('id', 'in', orderslist)]}}
