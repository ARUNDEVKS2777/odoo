from odoo import fields, models, _


class CommissionPlan(models.Model):
    _name = 'crm.commission'
    _description = 'Commission Plan'

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    from_date = fields.Date(string='From', required=True)
    to_date = fields.Date(string="To", required=True)
    type = fields.Selection([('product_wise', 'Product Wise'),
                             ('revenue_wise', 'Revenue Wise')],
                            default='product_wise', string='Type')
    revenue_type = fields.Selection(
        [('straight', 'Straight'),
         ('graduate', 'Graduate')], default='straight')
    commission_line_ids = fields.One2many('commission.line', 'line_id',
                                          string='Commission Line')
    graduate_line_ids = fields.One2many('revenue.line', 'desc',
                                        string='Graduate Line')
    straight_line_ids = fields.One2many('revenue.line', 'desc',
                                        string='Straight Line')
    # total=fields.Float()


class CommissionLine(models.Model):
    _name = 'commission.line'
    _description = 'Product Wise'

    line_id = fields.Many2one('crm.commission')
    prod_categ_id = fields.Many2one('product.category',
                                    string="Product Category")
    product_id = fields.Many2one('product.product', string='Product')
    rate_in_percentage = fields.Float(string='Rate in Percentage')
    max_commission_amt = fields.Float(string='Max Commission Amount')


class RevenueLine(models.Model):
    _name = 'revenue.line'
    _description = 'Revenue Wise'

    refer = fields.Integer(string='Sequence')
    from_amt = fields.Float(string='From')
    to_amt = fields.Float(string='To')
    rate = fields.Float(string='Rate(%)')
    desc = fields.Many2one('crm.commission')
