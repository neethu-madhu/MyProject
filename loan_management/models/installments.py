# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LoanInstallments(models.Model):
    _name = 'loan.installments'
    _description = 'For paying loan installments'

    date = fields.Date(string="Payment Date", required=True, help="Date of the payment")
    amount = fields.Float(string="Amount", required=True, help="Amount")
    paid = fields.Boolean(string="Paid", help="Paid")
    loan_id = fields.Many2one('loan.request', string="Loan Ref.", help="Loan")
    sequence_id = fields.Char(string="Seq", related='loan_id.sequence_no')
    name = fields.Many2one('res.partner', string='Applicant Name', related='loan_id.applicant_name')
    age = fields.Integer(string='Applicant Age', related='loan_id.applicant_Age')
    # loan_amount = fields.Float(string='Loan Amount', related='loan_id.principal_amount')
    # payslip_id = fields.Many2one('hr.payslip', string="Payslip Ref.", help="Payslip")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('paid', 'Paid')
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    def action_payment_register(self):
        for rec in self:
            rec.state = 'paid'
        values = {
            'applicant_name': self.name.id,
            'paid_amount': self.amount,
            'payment_date': self.date,
            'sequence_no': self.sequence_id

        }
        print('values', values)
        if self.env['loan.request'].search([('sequence_no', '=', self.sequence_id)]):
            print('sdfghj')
            self.env['loan.request'].sudo().create(values)

    # def action_compute(self):
    #     values = {
    #         'paid_amount': self.amount,
    #         'payment_date': self.date,
    #
    #     }
    #     print('values', values)
    #     print('values', self.loan_id)
    # if self.env['loan.request'].search([('sequence_no', '=', self.loan_id)]):
    #     if self.env['loan.request'].search([('sequence_no', '=', self.loan_id)]):
    #         print('sdfghj')
        #     self.env['loan.request'].sudo.create(values)
