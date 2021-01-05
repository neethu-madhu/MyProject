# -*- coding: utf-8 -*-
{
    'name': "Loan Management",

    'summary': """Deals with loan management snd related processes""",

    'description': """Deals with loan management snd related processes""",

    'author': "Neethu Madhu",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
        'views/loan_request.xml',
        'views/sequence_no.xml',
        'views/installments.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
