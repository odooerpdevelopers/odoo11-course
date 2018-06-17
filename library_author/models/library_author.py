# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryAuthor(models.Model):
    _name = "library.author"

    name = fields.Char(string="Name")
    active = fields.Boolean(string="Is Active?", default=True)
    country_id = fields.Many2one("res.country")

    book_ids = fields.Many2many("library.book", string="Books")

