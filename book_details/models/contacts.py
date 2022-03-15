from odoo import api, fields, models


class PartnerForm(models.Model):
    _inherit = "res.partner"
    _description = "Inventory Books"

    book_owner = fields.Boolean('Is Book Owner')
    need_invoice = fields.Boolean('Need Invoice')
    need_dn = fields.Boolean("Need DN")
    reservation_count = fields.Integer(string='Reservation Count',
                                       compute='_compute_reservation_count')

    def _compute_reservation_count(self):
        for rec in self:
            reservation_count = self.env['product.reservation']. \
                search_count([('customer_id', '=', rec.id)])
            rec.reservation_count = reservation_count

    def action_reservations(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Reservation',
            'res_model': 'product.reservation',
            'domain': [('customer_id', '=', self.id)],
            'view_mode': 'tree,form,kanban',
            'target': 'current',
        }
    def action_invoice(self):
        reservations = self.env['product.reservation'].search([('customer_id','=',self.id)])
        print(reservations)

    def action_dn(self):
        print("delivert")
