from odoo import api, fields, models


class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    country_id = fields.Many2one('res.country', default=lambda self: self.env.company.country_id)
    from_place = fields.Many2one('res.country.state', domain="[('country_id', '=', country_id)]", required=True)
    to_place = fields.Many2one('res.country.state', domain="[('country_id', '=', country_id)]", required=True)