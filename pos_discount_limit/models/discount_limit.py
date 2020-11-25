# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DiscountRestrictCat(models.Model):
    _inherit = 'pos.category'
    # _description = 'Discount Restriction'

    discount_limit_on = fields.Boolean()
    limited_discount = fields.Integer(string="Discount Limit")


class DiscountLimit(models.Model):
    _inherit = 'pos.config'
    _description = 'Discount Restriction'

    discount_limit = fields.Boolean()

    @api.onchange('discount_limit')
    def onchange_discount_limit(self):
        categories = self.env['pos.category'].search([])
        print('print')
        if self.discount_limit:
            for category in categories:
                category.discount_limit_on = True
        else:
            for category in categories:
                category.discount_limit_on = False
