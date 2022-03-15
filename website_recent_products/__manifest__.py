# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Recent Viewed Products',
    'version': '1.0',
    'summary': 'website recently viewed products',
    'sequence': 1,
    'description': """Website recently viewed products""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'depends': ['base', 'website', 'point_of_sale'],

    'data': [
        'views/snippet.xml',

    ],
    'assets': {
            'web.assets_frontend': [
                "website_recent_products/static/src/js/recent_view.js",


            ],
        },
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
