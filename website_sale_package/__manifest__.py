# -*- coding: utf-8 -*-
{
    'name': "Website Sale Package",

    'summary': """Sale package builder""",

    'description': """Sale package builder""",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    'category': 'Website/Website',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'stock', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sales_package.xml',
        'views/website_sales_package_form.xml',
        # 'views/templates.xml',
        'data/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
