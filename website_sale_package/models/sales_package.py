# -*- coding: utf-8 -*-

from odoo import models, fields


# defining model sale.package
class SalesPackage(models.Model):
    _name = 'sales.package'
    _description = 'packages'
    _rec_name = 'package_name'
    # defining fields
    # Name, width, height, length, Maximum weight
    package_name = fields.Char(string="Name", required=True)
    width = fields.Integer(string="width")
    height = fields.Integer(string="height")
    length = fields.Integer(string="length")
    maximum_weight = fields.Integer(string="maximum_weight")
