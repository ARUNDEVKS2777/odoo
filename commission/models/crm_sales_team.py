from odoo import api, fields, models


class CrmSalesTeam(models.Model):
    _inherit = 'crm.team'

    plan_id = fields.Many2one('crm.commission', string='Commission Plan')


class SalesPerson(models.Model):
    _inherit = 'res.users'

    plan_id = fields.Many2one('crm.commission', string='Commission Plan')