# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AssignAuthor(models.TransientModel):
    _name = "library.assign.author"

    active_book_ids = fields.Many2many(
        comodel_name='library.book',
        relation="library_book_wizard_rel",
        col1="wiz_id",
        col2="book_id",
        string="Active Book Ids"
    )

    author_id = fields.Many2one("library.author", string="Author")

    @api.model
    def default_get(self, fields_list):
        res = super(AssignAuthor, self).default_get(fields_list)
        active_ids = self.env.context.get("active_ids")
        if active_ids:
            res['active_book_ids'] = [(6, 0, active_ids)]

        return res

    def assign_author(self):
        if self.author_id:
            self.active_book_ids.write({'author_id': self.author_id.id})
