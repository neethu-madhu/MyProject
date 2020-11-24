# -*- coding: utf-8 -*-
{
    'name': "POS Discount",
    'summary': """Point of Sale Discount Management""",
    'description': """Point of Sale Discount Management""",
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'point_of_sale',
    'version': '13.0.1.0.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'point_of_sale'],
    # always loaded
    'data': [
        'views/discount_tag.xml',
        'views/templates.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
        'static/src/xml/discount_price_tag.xml',
    ],
}
