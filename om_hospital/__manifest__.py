# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Hospital Management Software',
    'sequence': 10,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.cybrosys.com',
    'depends': ['sale', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/patient_view.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
