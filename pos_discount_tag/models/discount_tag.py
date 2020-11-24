# -*- coding: utf-8 -*-


from odoo import models, fields


class DiscountTag(models.Model):
    _inherit = 'product.template'
    _description = 'specify discount'

    # defines field to add in product.template model
    discount_tag = fields.Integer()
