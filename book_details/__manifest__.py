# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Book Details',
    'version': '1.0',
    'summary': 'Book Details Menu',
    'sequence': 10,
    'description': """Book Details Menu""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'depends': ['contacts', 'sale', 'stock'],

    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/prod_reserve_seq.xml',
        'data/cron.xml',
        'wizard/reservation_wizard_view.xml',
        'report/report_reservation.xml',
        'report/reservation_details.xml',
        'report/reservation_template.xml',
        # 'views/action_manager.xml',
        'views/books.xml',
        'views/contacts.xml',
        'views/products.xml',
        'views/product_reservation.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': [
            'book_details/static/src/js/action_manager.js',
        ],
    },

}
