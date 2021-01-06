# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime


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
    # partner information
    partner_id = fields.Many2one('res.partner', required=True, string='Applicant Name',
                                 help='Company or individual that lends the money at an interest rate.')
    email = fields.Char(string="Email", related='partner_id.email')
    function = fields.Char(string="Job Position", related='partner_id.function')

    applied_date = fields.Date(string='Applied Date', help='Start of the moves', default=datetime.today())
    approved_date = fields.Date(string='Approved Date', help='Date of approval', default=datetime.today())
    currency_id = fields.Many2one('res.currency',
                                  string="Currency")
    principal_amount = fields.Monetary(string='Principal Amount')
    total_loan_amount = fields.Float(string="Total Amount",
                                     computte='_compute_total_amount')
    loan_schemes_id = fields.Many2one('loan.schemes',
                                      string='Scheme',
                                      editable=False,
                                      help='Scheme of loan')
    interest_rate = fields.Float(string='Rate', related='loan_schemes_id.interest_rate')
    duration = fields.Integer(string='Duration',
                                     related='loan_schemes_id.duration')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Request Sent '),
        ('approve', 'Approved'),
        ('refuse', 'Refused'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

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
