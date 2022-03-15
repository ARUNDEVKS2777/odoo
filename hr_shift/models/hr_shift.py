from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HRShifts(models.Model):
    _name = 'hr.shift'

    name = fields.Char(string='Name', required=True)
    from_time = fields.Float(string='From', required=True)
    to_time = fields.Float(string='To')

    @api.constrains('from_time', 'to_time')
    def check_time(self):
        if self.from_time > 24 or self.from_time < 0 or self.to_time > 24 or self.to_time < 0:
            raise ValidationError("wrong time")


class Employee(models.Model):
    _inherit = 'hr.employee'

    shift_id = fields.Many2one('hr.shift', string='Shift')


class Attendance(models.Model):
    _inherit = 'hr.attendance'

    late = fields.Boolean(string='Late', readonly=True)
    early_out = fields.Boolean(string='Early Out', readonly=True)

    @api.constrains('check_in', 'check_out')
    def checking(self):
        shift = self.env['hr.shift'].search([('id', '=', self.employee_id.id)])
        print(self.check_in)

        checked_in = self.check_in.hour + (self.check_in.minute / 100)
        print(checked_in)
        if shift.from_time < checked_in:
            self.late = True
        if self.check_out:
            checked_out = self.check_out.hour + (self.check_out.minute / 100)
            if shift.to_time > checked_out:
                self.early_out = True
        # print(datetime(self.check_in, "%H"))
        # checking_out = int(datetime.strftime(self.check_out, "%H"))
        # print(checking_out)

        # checked_out = datetime.strftime(self.check_out, "%H:%M:%S")
        # print(int(datetime.strftime(self.check_in, "%H")))
        # print(int(datetime.strftime(self.check_out, "%H")))
        # if shift.from_time < checked_in:
        #     print("late")
            # self.late = True
        # if shift.to_time > checking_out:
        #     print("early")
            # self.early_out; = True
