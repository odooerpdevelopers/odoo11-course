# -*- coding: utf-8 -*-
{
    'name': "Report Invoice demo",

    'summary': """
       report demo""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'data/paperformat.xml',
        'report/reports.xml',
        'report/invoice_report.xml',
    ],
}
