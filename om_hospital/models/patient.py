from odoo import fields, models, api, _


class Patient(models.Model):
    _name = 'hospital.patient'
    _inherit = ["mail.thread", 'mail.activity.mixin']

    bino = fields.Binary(string='Binary')
    mone=fields.Monetary(currency_field='currency')
    mono = fields.Monetary(currency_field='currency', digits=(12, 5))
    flo = fields.Float(digits=(5, 7))
    currency = fields.Many2one('res.currency', string='Currency', default=lambda x: x.env.company.currency_id)
    man_1 = fields.Many2one('res.partner', string='Customer', tracking=10)
    user_id = fields.Many2one('res.users')
    # activity_ids = fields.One2many('mail.activity', 'calendar_event_id', string='Activities')
    d= fields.Many2one('country.state')
    into = fields.Integer()
    charo = fields.Char()


    @api.onchange('man_1')
    def s(self):
        print(self.env)





