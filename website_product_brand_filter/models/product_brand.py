# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductBrand(models.Model):
    _name = 'product.brand'
    _description = "Product Brand"
    _rec_name = 'brand_name'

    brand_name = fields.Char(required=True)
    sequence_no = fields.Integer(string="Sequence no")
    parent_id = fields.Many2one('product.brand', string='Parent Category', index=True)


class DiscountPrizeTag(models.Model):
    _inherit = 'product.template'
    # defines new field
    brand_id = fields.Many2one('product.brand', string="Product Brand")


class Website(models.Model):
    _inherit = "website"

    def get_brands(self):
        brand = self.env['product.brand'].search([])
        return brand
