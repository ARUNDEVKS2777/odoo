# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'HR Shift',
    'version': '1.0',
    'summary': 'HR Shift',
    'sequence': 1,
    'description': """HR Shift""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'depends': ['base', 'hr'],

    'data': [
        'security/ir.model.access.csv',
        'views/hr_shift_view.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
