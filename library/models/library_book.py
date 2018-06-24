# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char(string="Name")
    active = fields.Boolean("Is active", default=True)
    image = fields.Binary()
    pages = fields.Integer(string="# Pages")
    isbn = fields.Char(string="ISBN", size=13)
    description = fields.Html(string="Description")
    category_id = fields.Many2one("library.category", string="Category")

    @api.constrains('name')
    def check_name(self):
        if not self.name:
            raise exceptions.ValidationError(
                "Name must be filled!!!"
            )

    @api.constrains('pages')
    def check_pages(self):
        if self.pages <= 0:
            raise exceptions.ValidationError(
                "Pages must be > 0!!!"
            )
