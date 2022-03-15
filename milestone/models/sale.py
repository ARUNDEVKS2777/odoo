from odoo import fields, models, _


class SaleMilestone(models.Model):
    _inherit = 'sale.order.line'

    milestone = fields.Integer(string="Milestone", required=True)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project = fields.Boolean(default=False)

    def create_project(self):
        self.project = True
        print(self.order_line.mapped('milestone'))
        main_task = set(self.order_line.mapped('milestone'))
        print(main_task)
        project = self.env['project.project'].create({'name': self.name,
                                                      'partner_id': self.partner_id.id})
        for rec in main_task:
            task = self.env['project.task'].create({'name': 'Milestone ' + str(rec),
                                                    'project_id': project.id,
                                                    })
            for i in self.order_line:
                if rec == i.milestone:
                    self.env['project.task'].create({'name': 'Milestone ' + str(
                        rec) + '-' + i.product_id.name,
                                                     'parent_id': task.id})

        return {
            'name': _('Project'),
            'view_mode': 'kanban,tree,form',
            'res_id': project.id,
            'res_model': 'project.project',
            'search_view_id': self.env.ref(
                'project.view_project_kanban').id,
            'type': 'ir.actions.act_window',
        }


        # self.env['project.task'].create({'name': 'task_1',
        #                                  'project_id': pro.id,
        #                                  'child_ids': {'name': self.name}
        #                                  })

        # j = 0
        # listed=[]
        # if self.order_line:
        #     for rec in self.order_line:
        #         listed[j] = 'Milestone_'+str(rec.milestone)
        #         j += 1
        #         for i in self.order_line:
        #             if i.milestone == rec.milestone:
        #                 print(i)

        # for rec in self.order_line:
        #     if rec.order_line.milestone:
        #         print(rec.order_line.milestone)
        #     else:
        #         print("gdgd")
        # for rec in self.order_line:
        #     self.task_name = 'Milestone_'+str(rec.milestone)
        #     print(self.task_name)

        # print(pro)