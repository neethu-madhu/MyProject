# -*- coding: utf-8 -*-
{
    'name': 'Sales Package',
    'summary': """This module will add a record to store package details""",
    'version': '13.1',
    'description': """This module will add a record to store package details""",
    'author': 'neethu',
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'category': 'Sales',
    'depends': ['base', 'sale', 'stock'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/sales_package.xml',
        'views/sales_package_sale_order.xml',
        'views/package_bundles.xml',
        'views/package_bundles_sequence.xml',
        'wizards/package_bundles_wizard.xml',
        'reports/report.xml',
        'reports/pdf_report_template.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
