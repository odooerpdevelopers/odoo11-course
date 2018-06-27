# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryAuthor(models.Model):
    _name = "library.author"

    name = fields.Char(string="Name")
    active = fields.Boolean(string="Is Active?", default=True)
    country_id = fields.Many2one("res.country")

    book_ids = fields.One2many("library.book", "author_id", string="Books")

    total_books = fields.Integer(
        compute="_get_total_books",
        string="Total Books",
        readonly=True,
    )

    def _get_total_books(self):
        for record in self:
            if record.book_ids:
                record.total_books = len(record.book_ids)
