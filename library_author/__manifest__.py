# -*- coding: utf-8 -*-
# by Juan Carlos Montoya <odooerpcloud@gmail.com>

{
    'name': "Library Author",

    'summary': """
        This module adds Author model
        """,

    'description': """
        This module adds Author model
    """,

    'author': "Odoo ERP Cloud",
    'website': "http://odooerpcloud.com",

    # for the full list
    'category': 'Library',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['library'],

    # always loaded
    'data': [
        "views/author_view.xml",
        "wizard/assign_author_view.xml",
    ],
    # only loaded in demonstration mode
    'application': True,

}