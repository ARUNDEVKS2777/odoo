from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ProductReservation(models.Model):
    _name = 'product.reservation'
    _description = 'Product Reservation'

    _rec_name = 'reference'

    name = fields.Char(string='Name')
    customer_id = fields.Many2one('res.partner', string='Customer', copy=False)
    creation_date = fields.Date(string='Date', default=lambda self: fields.Date.today())
    expiry_date = fields.Date(string='Expiry Date', required=True)
    product_line_id = fields.One2many('product.line', 'description_id',
                                      string='Product Line')
    internal_note = fields.Text(string='Internal Note')
    reference = fields.Char(string='Order Reference', default='New')
    state = fields.Selection([('draft', 'Draft'), ('reserved', 'Reserved')], string='Status', default= 'draft')
    active = fields.Boolean(default=True)
    compare = fields.Boolean(store=True)
    reservation_count = fields.Integer(string='Reservation Count',
                                       compute='_compute_reservation_count')
    related_user = fields.Many2one('res.users', string='Related User',
                                   default=lambda self: self.env.user)
    inv = fields.Boolean(related='customer_id.need_invoice')
    delivery_check = fields.Boolean(default=False)
    invoice_check = fields.Boolean(default=False)


    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code(
                'product.reservation.sequence') or _('New')
        return super(ProductReservation, self).create(vals)

    @api.model
    def check_expiry(self):
        customer_ids = self.env['product.reservation'].search(
            [('expiry_date', '<', fields.Date.today())])
        for rec in customer_ids:
            rec.active = False

    def action_reserve(self):
        if self.product_line_id and self.customer_id:
            self.state = 'reserved'
            self.name = self.reference
        else:
            raise ValidationError("can't validate without order line or customer")

    def action_invoice(self):
        print("invoice")
        if self.product_line_id:
            self.invoice_check = True
            listed = []
            for rec in self.product_line_id:
                record = {
                    'product_id': rec.product_id.id,
                    'quantity': rec.quantity,
                    'price_unit': rec.price
                }
                listed.append(record)
                print(listed)
            create_inv = self.env['account.move'].create({
                'partner_id': self.customer_id,
                'move_type': 'out_invoice',
                'invoice_origin': self.id,
                'l10n_in_gst_treatment': 'consumer',
                'invoice_line_ids': listed
            })
            print(create_inv.id)
            # create_inv.action_post()
            # self.state = 'confirm'
            return {
                'name': 'Customer Invoice',
                'view_mode': 'form',
                'view_type': 'form',
                'view_id': self.env.ref('account.view_move_form').id,
                'res_id': create_inv.id,
                'res_model': 'account.move',
                'context': "{'move_type':'out_invoice'}",
                'type': 'ir.actions.act_window',
            }
        else:
            raise ValidationError("Some Fields are Empty...")


    def reservation_invoiced(self):
        print("smart button")
        inv = self.env['account.move'].search(
            [('invoice_origin', '=', self.id)])
        print(inv)
        return {
            'name': 'test_invoice',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': self.env.ref('account.view_move_form').id,
            'res_id': inv.id,
            'res_model': 'account.move',
            'context': "{'type':'out_invoice'}",
            'type': 'ir.actions.act_window',
            'target': 'target',
        }

    def action_delivery(self):
        print("delivery order")
        self.delivery_check = True
        # self.state = 'delivery'
        if self.product_line_id or self.customer_id:
            delivery_ord = self.env['stock.picking'].create({
                'partner_id': self.customer_id.id,
                'picking_type_id': self.env.ref('stock.picking_type_out').id,
                'location_id': self.env.ref('stock.stock_location_stock').id,
                'location_dest_id': self.customer_id.id,
                'origin': self.id,
                'move_line_ids_without_package': [(0, 0, {
                    'product_id': self.product_line_id.product_id.id,
                    'qty_done': self.product_line_id.quantity,
                    'product_uom_qty': self.product_line_id.price,
                    'location_id': self.env.ref('stock.stock_location_stock').id,
                    'location_dest_id': self.customer_id.id,
                    'product_uom_id': self.product_line_id.product_id.uom_id.id})]
            })
            delivery_ord.state = 'assigned'
            print(delivery_ord)
            return {
                'name': 'Delivery Order',
                'view_mode': 'form',
                'view_type': 'form',
                'view_id': self.env.ref('stock.view_picking_form').id,
                'res_id': delivery_ord.id,
                'res_model': 'stock.picking',
                'type': 'ir.actions.act_window',
            }
        else:
            raise ValidationError("Some Fields are Empty...")

    def reservation_delivery(self):
        print("delivery smart button" )
        delivery = self.env['stock.picking'].search([('origin', '=', self.id)])
        return {
            'name': 'Delivery Order',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref('stock.view_picking_form').id,
            'res_id': delivery.id,
            'res_model': 'stock.picking',
            'type': 'ir.actions.act_window',
        }

    def _compute_reservation_count(self):
        for rec in self:
            rec.reservation_count = self.env['res.partner']. \
                search_count([('id', '=', rec.customer_id.id)])



class ProductLine(models.Model):
    _name = 'product.line'
    _description = 'Product Line'

    product_id = fields.Many2one('product.product', string='Select Products')
    quantity = fields.Integer(string='Quantity', default=1)
    price = fields.Float(string='Price')
    description_id = fields.Many2one('product.reservation', string='desc')
