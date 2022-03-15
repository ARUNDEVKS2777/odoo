from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order"
    _description = "Sale Order Line"

    @api.onchange('partner_id')
    def update_reservations(self):
        record = self.env['product.reservation']. \
                search([('customer_id', '=', self.partner_id.id)])
        lines = [(5, 0, 0)]
        for val in record:
            for line in val.product_line_id:
                val = {
                    'product_id': line.product_id.id,
                    'product_uom_qty': line.quantity,
                    'price_unit': line.price,
                    'product_uom': line.product_id.uom_id.id,
                    'name': line.product_id.name
                }
                lines.append((0, 0, val))
        self.order_line = lines





class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_template_id = fields.Char()
    product_uom_qty = fields.Integer()



