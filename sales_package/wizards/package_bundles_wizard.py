# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import UserError


class PackageBundleWizard(models.TransientModel):
    _name = 'package.bundle.wizard'
    _description = "Wizard: "

    salesman_id = fields.Many2one('res.partner', string='Salesman')
    from_date = fields.Date(string='Date From')
    to_date = fields.Date(string='Date To')

    # function to print pdf from the wizard
    def pdf_report(self):
        if self.salesman_id.id:
            if self.from_date:
                if self.to_date:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_partner_id = %s "
                                        "AND sale_order_date >= %s AND sale_order_date <= %s",
                                        (self.salesman_id.id, self.from_date, self.to_date))
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA', bundle_records)
                    return self.print_data(bundle_records)
                else:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_partner_id = %s AND sale_order_date >= %s ",
                                        (self.salesman_id.id, self.from_date))
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA-->', bundle_records)
                    return self.print_data(bundle_records)
            else:
                if self.to_date:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_partner_id = %s "
                                        "AND sale_order_date <= %s",
                                        (self.salesman_id.id, self.to_date))
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA', bundle_records)
                    return self.print_data(bundle_records)
                else:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_partner_id = %s ",
                                        (self.salesman_id.id,))
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA-->', bundle_records)
                    return self.print_data(bundle_records)
        else:
            if self.from_date:
                if self.to_date:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_order_date >= %s AND sale_order_date <= %s",
                                        (self.from_date, self.to_date))
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA', bundle_records)
                    return self.print_data(bundle_records)
                else:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_order_date >= %s ",
                                        (self.from_date,))
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA-->', bundle_records)
                    return self.print_data(bundle_records)
            else:
                if self.to_date:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_order_date <= %s",
                                        (self.to_date,))
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA', bundle_records)
                    return self.print_data(bundle_records)
                else:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles ")
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA-->', bundle_records)
                    return self.print_data(bundle_records)

    def print_data(self, bundle_records):
        if bundle_records:
            record_list = []
            # fetching required data based on each sequence number in bundle_records
            for details in bundle_records:
                values = [details['sequence_no']]
                self.env.cr.execute("SELECT a.sequence_no,b.name AS product_name,"
                                    "b.product_uom_qty,c.package_name,"
                                    "c.width,c.height,c.maximum_weight "
                                    "FROM sale_order_line b LEFT "
                                    "JOIN package_bundles_sale_order_line_rel d "
                                    "ON d.sale_order_line_id = b.id LEFT JOIN package_bundles a "
                                    "ON d.package_bundles_id = a.id LEFT JOIN sales_package c "
                                    "ON c.id = b.order_line_package_id "
                                    "WHERE sequence_no IS NOT NULL "
                                    "AND sequence_no = %s", values)
                get_data = self.env.cr.dictfetchall()
                print('PDF DATA-->', get_data)
                data_records = []
                # storing thq required data from get_data to the list data_records
                for records in get_data:
                    data_records.append({
                        'serial_number': records['sequence_no'],
                        'product': records['product_name'],
                        'product_uom_qty': records['product_uom_qty'],
                        'package_name': records['package_name'],
                        'package_width': records['width'],
                        'package_height': records['height'],
                        'package_maximum_weight': records['maximum_weight'],
                    })
                # appending sequence number and the list data_records to record_list
                record_list.append({
                    'serial_number': details['sequence_no'],
                    'recordset': data_records
                })
            data = {
                'ids': self.ids,
                'model': self._name,
                'values': record_list,
                'from_date': self.from_date,
                'to_date': self.to_date,
                'salesman': self.salesman_id.name
            }
            return self.env.ref('sales_package.report_package_bundle').report_action(self, data=data)
        else:
            raise UserError("NO valid data")

    # define function to print excel report from wizard
    def excel_report(self):
        print("excel report")
        if self.salesman_id.id:
            if self.from_date:
                if self.to_date:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_partner_id = %s "
                                        "AND sale_order_date >= %s AND sale_order_date <= %s",
                                        (self.salesman_id.id, self.from_date, self.to_date))
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA', bundle_records)
                    return self.wizard_data(bundle_records)
                else:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_partner_id = %s AND sale_order_date >= %s ",
                                        (self.salesman_id.id, self.from_date))
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA-->', bundle_records)
                    return self.wizard_data(bundle_records)
            else:
                if self.to_date:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_partner_id = %s "
                                        "AND sale_order_date <= %s",
                                        (self.salesman_id.id, self.to_date))
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA', bundle_records)
                    return self.wizard_data(bundle_records)
                else:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_partner_id = %s ",
                                        (self.salesman_id.id,))
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA-->', bundle_records)
                    return self.wizard_data(bundle_records)
        else:
            if self.from_date:
                if self.to_date:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_order_date >= %s AND sale_order_date <= %s",
                                        (self.from_date, self.to_date))
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA', bundle_records)
                    return self.wizard_data(bundle_records)
                else:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_order_date >= %s ",
                                        (self.from_date,))
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA-->', bundle_records)
                    return self.wizard_data(bundle_records)
            else:
                if self.to_date:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_order_date <= %s",
                                        (self.to_date,))
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA', bundle_records)
                    return self.wizard_data(bundle_records)
                else:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles ")
                    bundle_records = self.env.cr.dictfetchall()
                    print('DATA-->', bundle_records)
                    return self.wizard_data(bundle_records)

    def wizard_data(self, bundle_records):
        if bundle_records:
            data = {
                'ids': self.ids,
                'model': self._name,
                'from_date': self.from_date,
                'to_date': self.to_date,
                'salesman': self.salesman_id.name,
                'salesman_id': self.salesman_id.id,
            }
            print('wizard data', data)
            return self.env.ref('sales_package.report_package_bundle_xlsx').report_action(self, data)
        else:
            raise UserError("No Data")
