# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime


class LoanRequest(models.Model):
    _name = 'loan.request'
    _description = 'Loan Requests'
    _rec_name = 'sequence_no'

    # def _compute_loan_amount(self):
    #     total_paid = 0.0
    #     for loan in self:
    #         for line in loan.loan_lines:
    #             if line.paid:
    #                 total_paid += line.amount
    #         balance_amount = loan.loan_amount - total_paid
    #         loan.total_amount = loan.loan_amount
    #         loan.balance_amount = balance_amount
    #         loan.total_paid_amount = total_paid

    # fields
    sequence_no = fields.Char(string="Sequence Number",
                              readonly=True,
                              required=True,
                              copy=False,
                              default='New')
    # partner information
    partner_id = fields.Many2one('res.partner', required=True, string='Applicant Name',
                                 help='Company or individual that lends the money at an interest rate.')
    email = fields.Char(string="Email", related='partner_id.email')
    function = fields.Char(string="Job Position", related='partner_id.function')

    applied_date = fields.Date(string='Applied Date', help='Start of the moves', default=datetime.today())
    approved_date = fields.Date(string='Approved Date', help='Date of approval', default=datetime.today())
    currency_id = fields.Many2one('res.currency',
                                  string="Currency")
    principal_amount = fields.Monetary(string='Principal Amount', required=True)
    # total_loan_amount = fields.Float(string="Total Amount", compute='_compute_total_amount')
    loan_schemes_id = fields.Many2one('loan.schemes',
                                      string='Scheme',
                                      required=True,
                                      editable=False,
                                      help='Scheme of loan')
    interest_amount = fields.Float(string="Interest amount",
                                   required=True,
                                   help="interest amount")
    loan_amount = fields.Float(string="Loan Amount",
                               required=True,
                               help="Loan amount")
    total_amount = fields.Float(string="Total Amount",
                                store=True, readonly=True,
                                help="Total loan amount")
    monthly_payment = fields.Float(string="Monthly Payment")
    # balance_amount = fields.Float(string="Balance Amount",
    #                               store=True,
    #                               compute='_compute_loan_amount',
    #                               help="Balance amount")
    # total_paid_amount = fields.Float(string="Total Paid Amount",
    #                                  store=True,
    #                                  compute='_compute_loan_amount',
    #                                  help="Total paid amount")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Request Sent '),
        ('approve', 'Approved'),
        ('refuse', 'Refused'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    # installment line
    loan_lines = fields.One2many('loan.request.line', 'loan_id', string="Loan Line", index=True)

    # calculating interest amount toal amount to be paid and monthly payment
    @api.onchange('loan_schemes_id')
    def compute_interest_amount(self):
        for rec in self:
            interest_rate = rec.loan_schemes_id.interest_rate/100
            principal_amount = rec.principal_amount
            duration = rec.loan_schemes_id.duration
            rec.interest_amount = principal_amount * interest_rate
            rec.total_amount = principal_amount + rec.interest_amount
            rec.monthly_payment = rec.total_amount / duration

    # action for Apply button
    def action_send_request(self):
        for rec in self:
            rec.state = 'sent'

    # action function to refuse the request
    def action_refuse(self):
        for rec in self:
            rec.state = 'refuse'

    # action function for approving the request
    def action_approve(self):
        for rec in self:
            rec.state = 'approve'

    # action for cancel button
    def action_cancel(self):
        for rec in self:
            rec.state = 'draft'

    # sequence number
    @api.model
    # Override the original create function
    def create(self, values):
        if values.get('sequence_no', 'New') == 'New':
            values['sequence_no'] = self.env['ir.sequence'].next_by_code(
                'loan.request.sequence') or 'New'
        result = super(LoanRequest, self).create(values)
        return result


class InstallmentLine(models.Model):
    _name = 'loan.request.line'
    _description = "Installment details"

    date = fields.Date(string="Payment Date", required=True, help="Date of the payment")
    loan_id = fields.Many2one('loan.request', string="Loan Ref.")
    amount = fields.Float(string="Amount", required=True)
    paid = fields.Boolean(string="Paid")
