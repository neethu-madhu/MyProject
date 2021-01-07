# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LoanInstallments(models.Model):
    _name = 'loan.installments'
    _description = 'For paying loan installments'

    date = fields.Datetime(string="Payment Date", required=True, help="Date of the payment")
    amount = fields.Float(string="Amount", required=True, help="Amount")
    loan_id = fields.Many2one('loan.request', string="Loan Ref.", help="Loan")
    # partner_id = fields.Char(string="Name", related='loan_id.partner_id')
    # email = fields.Char(string="Email", related='loan_id.email')
    sequence_no = fields.Char(string="Seq", required=True, related='loan_id.sequence_no')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('paid', 'Paid')
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    def action_payment_register(self):
        for rec in self:
            rec.state = 'paid'
