from odoo import api, fields, models, _


class GenerateCommission(models.TransientModel):
    _name = 'generate.commission.wizard'
    _description = 'Generate Commission'

    from_date = fields.Datetime(string='From', required=True)
    to_date = fields.Datetime(string='To', required=True)
    sales_team_ids = fields.Many2many('crm.team', string='Sales Team')
    sales_person_ids = fields.Many2many('res.users', string='Sales Person')
    plan = fields.Many2many('crm.commission')
    total = fields.Float(string='Total')
    commission = fields.Float(string='Commission Amount')
    so_count = fields.Integer(string='Sale Order Count')
    type = fields.Selection([('person', 'Sales Person'),
                             ('team', 'Sales Team')], required=True, string="Type")

    def action_generate_commission(self):
        self.refresh()
        listed = []
        temp = 0.0
        self.total = 0.0
        self.commission = 0.0
        so = self.env['sale.order'].search(
            ['&', '&', '&', ('date_order', '>', self.from_date),
             ('date_order', '<', self.to_date), ('state', '=', 'sale'), '|',
             ('team_id', 'in', self.sales_team_ids.ids),
             ('user_id', 'in', self.sales_person_ids.ids)])
        print(so)
        self.so_count = len(so)
        print(self.so_count)
        for rec in so:
            self.total += rec.amount_total
        print(self.total)
        if self.sales_team_ids:
            for line in self.sales_team_ids:
                listed.append(line.plan_id.id)
                print(listed)
                if line.plan_id.revenue_type == 'straight':
                    temp = self.straight(self.total,
                                              line.plan_id.straight_line_ids)
                    print(temp)
                if line.plan_id.revenue_type == 'graduate':
                    temp = self.graduate(self.total,
                                              line.plan_id.graduate_line_ids)
                    print(temp)
                self.commission += temp

        if self.sales_person_ids:
            tempo= 0.0
            for line in self.sales_person_ids:
                listed.append(line.plan_id.id)
                print(listed)
                if line.plan_id.revenue_type == 'straight':
                    tempo = self.straight(self.total,
                                               line.plan_id.straight_line_ids)
                    print(tempo)
                if line.plan_id.revenue_type == 'graduate':
                    tempo = self.graduate(self.total,
                                               line.plan_id.graduate_line_ids)
                    print(tempo)
                self.commission += tempo

        self.plan = listed
        return {
            'name': _('Commission'),
            'view_mode': 'tree',
            # 'res_id': delivery_ord.id,
            'res_model': 'generate.commission.wizard',
            'search_view_id': self.env.ref(
                'commission.generate_commission_wizard_view_tree').id,
            'type': 'ir.actions.act_window',
        }

    def straight(self, total, line_ids):
        temp_total = 0.0
        if total > line_ids.from_amt:
            temp_total += total * line_ids.rate / 100
        return temp_total

    def graduate(self, total, line_ids):
        temp_total = 0.0
        for rec in line_ids:
            if total < rec.to_amt:
                temp_total += total * rec.rate / 100
            else:
                temp_total += rec.to_amt * rec.rate / 100
                total -= rec.to_amt
        return temp_total

    def refresh(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    # return {
    #     'name': _('Sales Orders'),
    #     'view_mode': 'tree,form',
    #     'res_model': 'sale.order',
    #     'search_view_id': [self.env.ref(
    #         'sale.view_quotation_tree').id],
    #     'type': 'ir.actions.act_window',
    #     'domain': ['&', '&', '&', ('date_order', '>', self.from_date),
    #                ('date_order', '<', self.to_date), ('state', '=', 'sale'), '|',
    #                ('team_id', 'in', self.sales_team_id.ids),
    #                ('user_id', 'in', self.sales_person_id.ids)]
    # }

    # delivery_ord = self.env['generate.commission.wizard'].create({
    #     'sales_team_ids': self.sales_team_ids,
    #     'sales_person_ids': self.sales_person_ids,
    #     # 'plan': listed,
    #     'so_count': self.so_count,
    #     'total': self.total,
    #     'commission': self.commission
    # })

