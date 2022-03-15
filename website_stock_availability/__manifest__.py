# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Stock Availability',
    'version': '1.0',
    'summary': 'Stock availability in website',
    'sequence': 10,
    'description': """Stock availability in website""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'depends': ['base', 'website'],

    'data': [
        'views/stock_availability_template.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
