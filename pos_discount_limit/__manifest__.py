# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'POS Discount Limit',
    'version': '1.0',
    'summary': 'POS Discount Limit',
    'sequence': 1,
    'description': """POS Discount Limit""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'depends': ['base', 'point_of_sale', 'hr'],

    'data': [
        'views/pos_product_category_view.xml',

    ],
    'assets': {
            'point_of_sale.assets': [
                'pos_discount_limit/static/src/js/discount.js',
                'pos_discount_limit/static/src/js/restrict_cashier.js',
            ],
        },
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
