from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Books(models.Model):
    _name = "inventory.books"
    _description = "Inventory Books"
    name_of_book = fields.Char(string='Name', required=True)
    author_name_id = fields.Many2many('res.partner', string='Author',
                                      required=True)
    image = fields.Binary(string='Book Image')
    book_category = fields.Selection([
        ('story', 'Story'),
        ('novel', 'Novel'),
        ('poem', 'Poem')
    ])
    isbn_no = fields.Char(string='ISBN Number')
    publisher_name = fields.Many2one('res.partner', string='Publisher')
    serial_no = fields.Char(string='Serial Number', required=True)
    published_date = fields.Date(string='Published Date')
    related_partner_id = fields.Many2one('res.partner',
                                         string='Related Partner')
    responsible = fields.Many2one('res.users', string='Responsible',
                                  default=lambda self: self.env.user)
    book_price = fields.Float(string='Price')
    availability = fields.Boolean(string='Availability')

    _sql_constraints = [
        ('serial_no', 'unique(serial_no)', 'Serial Number Must Be Unique')]

    @api.constrains('serial_no')
    def check_slno(self):
        print(self)
        count = len(self.serial_no)
        if count > 5 or count < 3:
            raise ValidationError(
                "Serial number must have length from 3 to 5")

    _rec_name = 'name_of_book'
