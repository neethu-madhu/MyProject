# -*- coding: utf-8 -*-

from odoo import models, fields, api


# defines new model PackageBundles
class PackageBundles(models.Model):
    _name = 'package.bundles'
    _description = 'package bundles'
    _rec_name = 'sequence_no'
    # defines fields
    sequence_no = fields.Char(string="Sequence Number",
                              readonly=True,
                              required=True,
                              copy=False,
                              default='New')
    sale_order_reference = fields.Char(string='Sale Order Reference')
    sale_order_date = fields.Datetime(string='Date')
    sale_order_expected_date = fields.Datetime(string='Expected Date')
    # takes instance of res.partner and sale order line
    sale_partner_id = fields.Many2one('res.partner', string='Partner')
    sale_order_ids = fields.Many2many('sale.order.line')

    @api.model
    # Override the original create function
    def create(self, values):
        if values.get('sequence_no', 'New') == 'New':
            values['sequence_no'] = self.env['ir.sequence'].next_by_code(
                'package.bundles.sequence') or 'New'
        result = super(PackageBundles, self).create(values)
        return result
