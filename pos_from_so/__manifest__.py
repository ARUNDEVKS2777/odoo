# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Pos From SO',
    'version': '1.0',
    'summary': 'PoS From SaleOrder',
    'sequence': 1,
    'description': """PoS From SaleOrder""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'depends': ['base', 'sale', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'wizard/payment_pos_view.xml',
        'views/sale_order_view.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
