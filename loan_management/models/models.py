# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LoanManagement(models.Model):
    _name = 'loan.management'
    _description = 'loan_management.loan_management'


# loan proofs required
class LoanProofs(models.Model):
    _name = 'loan.proofs'
    _description = 'Proofs required to be provided'
    _rec_name = 'proof_name'

    # fields
    proof_name = fields.Char(string='Name', required=True)
    mandatory_proof = fields.Boolean(string='Mandatory')


# types  of loan present
class LoanTypes(models.Model):
    _name = 'loan.types'
    _description = 'Types of loan'
    _rec_name = 'name'

    # fields
    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', help='Code for the name', required=True)
    interest_payable = fields.Boolean(sting='Is interest payable', help='Enable if there is interest')
    repayment_method = fields.Selection([('cash bank/cheque', 'Cash Bank/Check')], string='Repayment Method')
    disburse_method = fields.Selection([('cash bank/cheque', 'Cash Bank/Check')], string='Disburse Method')


# loan schemes
class LoanSchemes(models.Model):
    _name = 'loan.schemes'
    _description = 'Loan schemes present'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)

    duration = fields.Integer(string='Duration(months)')
    interest_rate = fields.Float(string='Rate(%)')
