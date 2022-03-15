from odoo import api, fields, models


class ProductForm(models.Model):
    _inherit = 'product.template'
    _description = 'product_related_book'

    related_book = fields.Many2one('inventory.books', string='Related Book')

    @api.onchange('related_book')
    def update_field(self):
        if self.related_book:
            if self.list_price:
                self.related_book.book_price = self.list_price
                self.related_book.isbn_no = self.default_code

