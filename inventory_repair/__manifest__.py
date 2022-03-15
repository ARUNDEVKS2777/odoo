# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Inventory Repair',
    'version': '1.0',
    'summary': 'Inventory Repair Software',
    'sequence': 10,
    'description': """Inventory Repair Software""",
    'category': 'Productivity',
    'website': 'https://www.cybrosys.com',
    'depends': ['stock', 'sale', 'mail', 'contacts'],

    'data': [
        'security/ir.model.access.csv',
        'views/repair.xml',
        'views/sale_repair.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
