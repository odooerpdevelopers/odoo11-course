# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryBook(models.Model):
    _inherit = "library.book"

    author_id = fields.Many2one("library.author")

