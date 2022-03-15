from odoo import api, fields, models
import json
import io
from odoo.exceptions import ValidationError
from odoo.tools import date_utils
try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter


class ReservationWizard(models.TransientModel):
    _name = 'reservation.report.wizard'

    from_date = fields.Date(string="From")
    to_date = fields.Date(string='To')
    product_ids = fields.Many2many('product.product', string='Products')
    customer_id = fields.Many2one('res.partner', string='Customer')
    type = fields.Selection([('product', 'Product'),
                             ('customer', 'Customer')], string='Type')
    current_day = fields.Date(default=lambda self: fields.Date.today())

    def action_reservation_report(self):
        print("c")
        products = str(self.product_ids.mapped('id'))
        print('products', products)
        product = '(' + (products)[1:-1] + ')'
        print(product)
        query = """select product_reservation.reference,product_template.name,res_partner.name,
                                product_reservation.creation_date,product_reservation.state from product_reservation
                                inner join product_line on product_line.description_id = product_reservation.id
                                inner join product_product on product_line.product_id= product_product.id
                                inner join product_template on product_product.product_tmpl_id = product_template.id
                                inner join res_partner on res_partner.id = product_reservation.customer_id """
        # if self.from_date:
        #     query += """ AND product_reservation.creation_date >= '%s' """ % self.from_date
        # if self.to_date:
        #     query += """ AND product_reservation.creation_date <= '%s' """ % self.to_date
        if self.from_date and self.to_date:
            if self.from_date > self.to_date:
                raise ValidationError('Start Date must be less than End Date')
            else:
                print(self.from_date)
                query += """ AND product_reservation.creation_date BETWEEN '%s' AND '%s' """ % (self.from_date, self.to_date)
        if self.type == 'customer':
            cust="""select product_reservation.reference,product_template.name,
                                product_reservation.creation_date,product_reservation.state from product_reservation
                                inner join product_line on product_line.description_id = product_reservation.id
                                inner join product_product on product_line.product_id= product_product.id
                                inner join product_template on product_product.product_tmpl_id = product_template.id
                                inner join res_partner on res_partner.id = product_reservation.customer_id """
            if self.from_date:
                cust += """ AND product_reservation.creation_date >= '%s' """ % self.from_date
            if self.to_date:
                cust += """ AND product_reservation.creation_date <= '%s' """ % self.to_date
            if self.customer_id:
                cust += """ AND product_reservation.customer_id = '%d'""" % self.customer_id.id
            self.env.cr.execute(cust)
            rec = self.env.cr.fetchall()
            print(rec)
            data = {
                'form_data': self.read()[0],
                'reservations': rec
            }
            return self.env.ref(
                'book_details.action_report_reservation').report_action(self,
                                                                        data=data)
        if self.type == 'product':
            if self.product_ids:
                query += """AND product_line.product_id IN""" + product
            self.env.cr.execute(query)
            rec = self.env.cr.fetchall()
            data = {
                'form_data': self.read()[0],
                'reservations': rec
            }
            return self.env.ref(
                'book_details.action_reservation_template').report_action(self,
                                                                        data=data)

        if self.type is False:
            print("v")
            self.env.cr.execute(query)
            rec = self.env.cr.fetchall()
            print(rec)
            data = {
                'form_data': self.read()[0],
                'reservations': rec
            }
            return self.env.ref(
                'book_details.action_reservation_template').report_action(self,
                                                                        data=data)

    def action_xlsx_report(self):
        query = """select product_reservation.reference,product_template.name,res_partner.name,
                                        product_reservation.creation_date,product_reservation.state from product_reservation
                                        inner join product_line on product_line.description_id = product_reservation.id
                                        inner join product_product on product_line.product_id= product_product.id
                                        inner join product_template on product_product.product_tmpl_id = product_template.id
                                        inner join res_partner on res_partner.id = product_reservation.customer_id """
        if self.from_date:
            query += """ AND product_reservation.creation_date >= '%s' """ % self.from_date
        if self.to_date:
            query += """ AND product_reservation.creation_date <= '%s' """ % self.to_date
        if self.type == 'customer':
            cust = """select product_reservation.reference,product_template.name,
                                            product_reservation.creation_date,product_reservation.state from product_reservation
                                            inner join product_line on product_line.description_id = product_reservation.id
                                            inner join product_product on product_line.product_id= product_product.id
                                            inner join product_template on product_product.product_tmpl_id = product_template.id
                                            inner join res_partner on res_partner.id = product_reservation.customer_id """
            if self.from_date:
                cust += """ AND product_reservation.creation_date >= '%s' """ % self.from_date
            if self.to_date:
                cust += """ AND product_reservation.creation_date <= '%s' """ % self.to_date
            if self.customer_id:
                cust += """ AND product_reservation.customer_id = '%d'""" % self.customer_id.id
            self.env.cr.execute(cust)
            records = self.env.cr.fetchall()
            print(records)
            data = {
                'form_data': self.read()[0],
                'reservations': records
            }
        if self.type == 'product':
            products = str(self.product_ids.mapped('id'))
            print('products', products)
            product = '(' + (products)[1:-1] + ')'
            print(product)
            if self.product_ids:
                query += """AND product_line.product_id IN""" + product
            self.env.cr.execute(query)
            rec = self.env.cr.fetchall()
            data = {
                'form_data': self.read()[0],
                'reservations': rec
            }

        if self.type is False:
            self.env.cr.execute(query)
            rec = self.env.cr.fetchall()
            print(rec)
            data = {
                'form_data': self.read()[0],
                'reservations': rec
            }

        return {
            'type': 'ir.actions.report',
            'data': {'model': 'reservation.report.wizard',
                     'options': json.dumps(data,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Excel Report',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'align': 'center', 'bold': True, 'font_size': '13px'})
        sheet.set_column(2, 6, 15)
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        txt = workbook.add_format({'align': 'center', 'font_size': '11px'})
        sheet.merge_range('A1:H3', 'Reserved List', head)
        if data['form_data']['from_date']:
            sheet.write('B7', 'From:', cell_format)
            sheet.merge_range('C7:D7', data['form_data']['from_date'], txt)
        if data['form_data']['to_date']:
            sheet.write('F7', 'To:', cell_format)
            sheet.merge_range('G7:H7', data['form_data']['to_date'], txt)
        if not data['form_data']['to_date'] and not data['form_data']['from_date']:
            sheet.write('B7', 'Date:', cell_format)
            sheet.merge_range('C7:D7', str(self.current_day), cell_format)
        if data['form_data']['type'] == 'customer':
                sheet.write('D5', 'Customer :', cell_format)
                sheet.merge_range('E5:F5', data['form_data']['customer_id'][1], cell_format)
        row = 10
        col = 0

        if data['form_data']['type'] == 'customer':
            sheet.write(row, col + 1, 'Sl No', cell_format)
            sheet.write(row, col + 2, 'Reference', cell_format)
            sheet.write(row, col + 3, 'Product', cell_format)
            sheet.write(row, col + 4, 'Date', cell_format)
            sheet.write(row, col + 5, 'Status', cell_format)
            sl_no = 1
            for rec in data['reservations']:
                row += 1
                sheet.write(row, col + 1, sl_no, txt)
                sheet.write(row, col + 2, rec[0], txt)
                sheet.write(row, col + 3, rec[1], txt)
                sheet.write(row, col + 4, rec[2], txt)
                sheet.write(row, col + 5, rec[3], txt)
                sl_no += 1

        if data['form_data']['type'] == 'product' or data['form_data']['type'] is False:
            print("ghgh")
            sheet.write(row, col + 1, 'Sl No', cell_format)
            sheet.write(row, col + 2, 'Reference', cell_format)
            sheet.write(row, col + 3, 'Customer', cell_format)
            sheet.write(row, col + 4, 'Product', cell_format)
            sheet.write(row, col + 5, 'Date', cell_format)
            sheet.write(row, col + 6, 'Status', cell_format)
            sl_no = 1
            for rec in data['reservations']:
                print(rec)
                row += 1
                sheet.write(row, col + 1, sl_no, txt)
                sheet.write(row, col + 2, rec[0], txt)
                sheet.write(row, col + 3, rec[2], txt)
                sheet.write(row, col + 4, rec[1], txt)
                sheet.write(row, col + 5, rec[3], txt)
                sheet.write(row, col + 6, rec[4], txt)
                sl_no += 1
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
