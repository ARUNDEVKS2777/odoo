from odoo import api, fields, models, _


class CustomerDueLimit(models.Model):
    _inherit = 'res.partner'

    limit = fields.Char(string='Due Limit')
