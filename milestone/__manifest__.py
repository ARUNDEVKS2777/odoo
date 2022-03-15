# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Milestone',
    'version': '1.0',
    'summary': 'Milestone',
    'sequence': 10,
    'description': """Milestone""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'depends': ['base', 'sale'],

    'data': [
        'views/sale_view.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
