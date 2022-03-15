from odoo import api, fields, models, _


class SaleRepair(models.Model):
    _inherit = 'sale.order'

    repair = fields.Boolean(string='Repair')

    @api.onchange('partner_id')
    def repair_warning(self):
        if self.partner_id:
            cust = self.env['inventory.repair'].search(
                [('customer_id', '=', self.partner_id.id)])
            if self.partner_id == cust.customer_id:
                res = {'warning': {
                    'title': _('Warning'),
                    'message': _('This user has some pending repair requests.')}}
                if res:
                    return res
