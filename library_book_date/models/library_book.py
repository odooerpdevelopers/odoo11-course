# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class LibraryBook(models.Model):
    _inherit = "library.book"

    date = fields.Date(string="Release Date")

    @api.onchange('date')
    def onchange_date(self):
        today = fields.Date.today()
        if self.date and self.date > today:
            raise exceptions.UserError(
                "Date should be less than today!!!"
            )
