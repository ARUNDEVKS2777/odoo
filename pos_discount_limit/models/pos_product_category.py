from odoo import api, fields, models, _


class PosProductCategory(models.Model):
    _inherit = 'pos.category'

    # discount_limit = fields.Float(string="Discount %")
    config = fields.Boolean(string='Discount Configuration')


class CashierRestrict(models.Model):
    _inherit = 'hr.employee'

    cashier = fields.Boolean(string='Cashier')


class PosDiscountConfig(models.Model):
    _inherit = 'pos.config'

    discount_limit = fields.Float(string="Discount %")
    discount_config = fields.Boolean(string='Discount Limit')
    product_category_ids = fields.Many2many('pos.category', 'pos_category_rel', 'categ_id', 'select_id', string='Categories')

    @api.onchange('employee_ids')
    def _compute_cashier(self):
        emp = self.env['hr.employee'].search([])
        emp.cashier = False
        for rec in self.employee_ids.ids:
            cashiers = self.env['hr.employee'].search([('id', '=', rec)])
            cashiers.cashier = True







    @api.onchange('discount_config')
    def disc_limit(self):
        limit = self.env['pos.category'].search([])
        print(limit)
        limit.config = self.discount_config

    @api.constrains('product_category_ids')
    def discount_category(self):
        print(self.product_category_ids)
        all_categ = self.env['pos.category'].search([])
        for g in all_categ:
            g.config = False
        print(all_categ)
        for rec in self.product_category_ids:
            for i in all_categ:
                # print(i.config)
                if rec.id == i.id:
                    i.config = True
                    # print(i.config)
        for g in all_categ:
            print(g.config)



