# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Order Tracking',
    'version': '1.0',
    'summary': 'website order tracking',
    'sequence': 1,
    'description': """Website order tracking""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'depends': ['base', 'website', 'stock'],

    'data': [
        'views/order_track_views.xml',
        'views/stock_picking_views.xml',

    ],
    # 'assets': {
    #         'web.assets_frontend': [
    #             "website_order_tracking/static/src/js/search_get.js",
    #
    #
    #         ],
    #     },
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
