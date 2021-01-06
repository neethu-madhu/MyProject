# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LoanManagement(models.Model):
    _name = 'loan.management'
    _description = 'loan_management.loan_management'


# loan schemes
class LoanSchemes(models.Model):
    _name = 'loan.schemes'
    _description = 'Loan schemes present'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    duration = fields.Integer(string='Duration(months)')
    interest_rate = fields.Float(string='Rate(%)')
