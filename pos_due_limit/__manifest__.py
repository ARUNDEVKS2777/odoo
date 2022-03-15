# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'POS Due Limit',
    'version': '1.0',
    'summary': 'POS due limit',
    'sequence': 1,
    'description': """PoS due limit""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'depends': ['base', 'sale', 'point_of_sale'],

    'data': [
        'views/customer_due_limit_view.xml',

    ],
    'assets': {
            'point_of_sale.assets': [
                'pos_due_limit/static/src/js/due_limit.js',
                'pos_due_limit/static/src/js/payment_limit.js',
            ],
        },
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
