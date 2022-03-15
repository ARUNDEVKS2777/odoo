# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'CRM Commission',
    'version': '1.0',
    'summary': 'CRM Commission',
    'sequence': 10,
    'description': """CRM Commission""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'depends': ['base', 'crm', 'sale'],

    'data': [
        'wizard/generate_commission_views.xml',
        'security/ir.model.access.csv',
        'views/commission.xml',
        'views/crm_sales_team_views.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
