# -*- coding: utf-8 -*-
# by Juan Carlos Montoya <odooerpcloud@gmail.com>

{
    'name': "Library Book Date",

    'summary': """
        This module adds a new Date field in Book Model
        """,

    'description': """
            This module adds a new Date field in Book Model

    """,

    'author': "Odoo ERP Cloud",
    'website': "http://odooerpcloud.com",

    # for the full list
    'category': 'Library',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['library'],

    # always loaded
    'data': ["views/book_view.xml"],
    # only loaded in demonstration mode
    'application': True,

}