# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    _rec_name = "package_name_ids"
    # selects multiple packages in the package field lies below customer field
    package_name_ids = fields.Many2many('sales.package',
                                        string="Packages")
    # defines package info page
    package_info_ids = fields.Many2many('sales.package',
                                        'package_info',
                                        string="Package Info")

    # defines function to add details of package selected in package field
    @api.onchange('package_names')
    def set_package_info(self):
        for rec in self:
            rec.package_info_ids = rec.package_names_ids

    # defines function to add corresponding package name in package field
    @api.onchange('package_info')
    def set_package_name(self):
        for rec in self:
            rec.package_name_ids = rec.package_info_ids

    # defines function to create a new bundle
    def create_bundles(self):
        order_line = []
        for order in self:
            for details in order.order_line:
                if details.order_line_package_id.id:
                    order_line.append(details.id)

        if len(order_line) != 0:
            vals = {
                'sale_order_reference': self.name,
                'sale_order_date': self.date_order,
                'sale_order_expected_date': self.expected_date,
                'sale_partner_id': self.partner_id.id,
                'sale_order_ids': order_line
            }
            if self.env['package.bundles'].search([('sale_order_reference', '=', self.name)]):
                # used when edit the sale order
                self.env['package.bundles'].search([('sale_order_reference', '=', self.name)]).write(vals)
            else:
                # used when creates a new sale order
                self.env['package.bundles'].sudo().create(vals)

    # function to show details of selected  in the smart button
    def get_package_info(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Package Bundles',
            'view_mode': 'tree,form',
            'res_model': 'package.bundles',
            'domain': [('sale_order_reference', '=', self.name)],
            'context': "{'create': False}"
        }

    # Override the write function for the model
    def write(self, vals):
        result = super(SaleOrderInherit, self).write(vals)
        self.create_bundles()
        return result


# define to add field in the sale order line
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    # defines field for adding Package field inside the sale.order.line
    order_line_package_id = fields.Many2one('sales.package', string='Packages')
    # defines fields to take required details from sales.package model
    width_package = fields.Integer('Width', related='order_line_package_id.width')
    height_package = fields.Integer('Height', related='order_line_package_id.height')
    length_package = fields.Integer('Length', related='order_line_package_id.length')
    weight_package = fields.Integer('Max Weight', related='order_line_package_id.maximum_weight')
