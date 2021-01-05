# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LoanRequest(models.Model):
    _name = 'loan.request'
    _description = 'Loan Requests'
    _rec_name = 'sequence_no'

    # fields
    sequence_no = fields.Char(string="Sequence Number",
                              readonly=True,
                              required=True,
                              copy=False,
                              default='New')
    # applicant_name = fields.Many2one('res.partner', string='Applicant Name')
    applicant_name = fields.Many2one('res.partner', string='Applicant Name',
                                     help='Company or individual that lends the money at an interest rate.',
                                     required=True, change_default=True, index=True, tracking=1)
    applicant_Age = fields.Integer(string='Age', help='Age of the applicant')
    applied_date = fields.Datetime(string='Applied Date', help='Start of the moves')
    approved_date = fields.Datetime(string='Approved Date')
    currency_id = fields.Many2one('res.currency', string="Currency")
    principal_amount = fields.Monetary(string='Principal Amount')
    total_loan_amount = fields.Float(string="Total Amount", computte='_compute_total_amount')
    # loan_types_id = fields.Many2one('loan.types', string='Category', help='Type of loan required')
    loan_schemes_id = fields.Many2one('loan.schemes', string='Scheme', editable=False, help='Scheme of loan')
    # print('loan_schemes_id', loan_schemes_id)
    rate_of_interest = fields.Float(string='Rate', related='loan_schemes_id.interest_rate')
    # print('rate_of_interest', rate_of_interest)
    scheme_duration = fields.Integer(string='Duration', related='loan_schemes_id.duration')
    # print('scheme_duration', scheme_duration)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Request Sent '),
        ('approve', 'Approved'),
        ('refuse', 'Refused'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    # general info
    # loan_amount = fields.Float(string="Loan Amount", related='principal_amount')
    date_applied = fields.Datetime(string='Applied date', related='applied_date')
    date_approved = fields.Datetime(string='Approved date', related='approved_date')
    loan_installment_id = fields.Many2many('loan.installments')
    print('paid_amount', loan_installment_id)
    # paid_amount = fields.Float(string="Paid Amount", related='loan_installment_id.amount')
    # payment_date = fields.Date(string="Date", related='loan_installment_id.date')

    paid_amount = fields.Float(string="Paid Amount")
    # installment_id = fields.Char('inst')
    payment_date = fields.Date(string="Date")

    # action for Apply button
    def action_send_request(self):
        for rec in self:
            rec.state = 'sent'

    def action_refuse(self):
        for rec in self:
            rec.state = 'refuse'
        # return self.write({'state': 'refuse'})

    def action_approve(self):
        for rec in self:
            rec.state = 'approve'
        # self.write({'state': 'approve'})

    #  action for done button
    # def action_done_request(self):
    #     for rec in self:
    #         rec.state = 'loan_request'
    def action_cancel(self):
        self.write({'state': 'cancel'})

    # sequence number
    @api.model
    # Override the original create function
    def create(self, values):
        if values.get('sequence_no', 'New') == 'New':
            values['sequence_no'] = self.env['ir.sequence'].next_by_code(
                'loan.request.sequence') or 'New'
        result = super(LoanRequest, self).create(values)
        return result
