# -*- coding: utf-8 -*-

{
    'name': 'Attendance Customization',
    'sequence': 1222,
    'version': '1.0',
    'depends': ['mail','base','hr_payroll','crm','mrp','project','product','sale','product'],
    'category': 'sale','crm'
    'summary': 'Handle lunch orders of your employees',
    'description': """
The base module to manage lunch.
================================
Cost sheet from CRM, Generate Quotation
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/view.xml',
        'views/import_data.xml'
    ],
    'installable': True,
    'application': True,
}
