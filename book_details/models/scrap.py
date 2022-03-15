from odoo import api, fields, models


class ScrapPutaway(models.Model):
    _inherit = 'stock.scrap'

    @api.onchange('product_id')
    def change_location(self):
        putaways = self.env['stock.putaway.rule'].search(
            [('product_id', '=', self.product_id.id)])
        self.location_id = putaways.location_out_id
