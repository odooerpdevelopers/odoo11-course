from odoo import api, models


class InvoiceDemo(models.AbstractModel):
    _name = 'report.report_demo.invoice_demo'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['account.invoice']
        docs = report_obj.browse(docids)
        docargs = {
            'doc_ids': docids,
            'doc_model': 'account.invoice',
            'docs': docs,
            'mydata': [1, 5, 8],
        }

        return docargs

