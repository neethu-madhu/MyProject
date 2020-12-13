# -*- coding: utf-8 -*-
{
    'name': "Product Brand Filter",

    'summary': """Manage filtering based on brand""",

    'description': """Manage filtering based on brand""",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    'category': 'Website/Website',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_brand.xml',
        'views/product_brand_field.xml',
        'views/website_brand_filter.xml',
        # 'views/templates.xml',
        # 'data/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
