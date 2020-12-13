from odoo import models
# from odoo.exceptions import UserError


class PackageBundlesXlsx(models.AbstractModel):
    _name = 'report.sales_package.report_package_bundles_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet('Package Bundles')
        format1 = workbook.add_format({'bold': 2, 'border': 1, 'align': 'center',
                                       "font_size": 16, 'bg_color': '#808080', 'valign': 'vcenter'})
        format4 = workbook.add_format({'bold': 2, 'align': 'center', "font_size": 14,
                                       'bg_color': '#808080', 'valign': 'vcenter'})
        format2 = workbook.add_format({'bold': 1, "font_size": 14, 'align': 'left'})
        format3 = workbook.add_format({"font_size": 14, "align": "left"})
        format5 = workbook.add_format({'bold': 1, "font_size": 10, "align": "left"})
        print('Data from', lines)
        print('Data ', data)
        sheet.merge_range('B6:J7', 'Package Bundles Excel Report', format1)
        sheet.merge_range('B1:C4', 'My Company (San Francisco)'
                                   '\n 250 Executive Park Blvd,'
                                   '\n Suite 3400San Francisco '
                                   '\n 94134Gujarat GJ '
                                   '\n India', format5)
        # increase size of columns
        sheet.set_column(1, 1, 10)
        sheet.set_column(2, 2, 15)
        sheet.set_column(3, 3, 15)
        sheet.set_column(4, 4, 35)
        sheet.set_column(5, 5, 15)
        sheet.set_column(6, 6, 15)
        sheet.set_column(7, 7, 15)
        sheet.set_column(8, 8, 15)
        sheet.set_column(9, 9, 15)
        sheet.set_column(10, 10, 15)
        # table headings
        sheet.write(11, 2, 'SI No', format4)
        sheet.write(11, 3, 'Package', format4)
        sheet.write(11, 4, 'Product', format4)
        sheet.write(11, 5, 'Quantity', format4)
        sheet.write(11, 6, 'Width', format4)
        sheet.write(11, 7, 'Height', format4)
        sheet.write(11, 8, 'Weight', format4)
        if data['salesman_id']:
            sheet.write(7, 4, 'Salesman', format2)
            sheet.write(7, 5, data['salesman'], format3)
        if data['from_date']:
            sheet.write(8, 4, 'From Date', format2)
            sheet.write(8, 5, data['from_date'], format3)
        if data['to_date']:
            sheet.write(9, 4, 'To Date', format2)
            sheet.write(9, 5, data['to_date'], format3)

        def filter_data():
            serial_no = 1
            count = 13
            for details in bundle_records:
                values = [details['sequence_no']]
                sheet.write(count, 2, serial_no, format2)
                sheet.merge_range(count, 3, count, 8, details['sequence_no'], format2)
                count = count+1
                serial_no = serial_no+1
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
                sequence = serial_no-1
                sequence_in = sequence+0.1
                for records in get_data:
                    sheet.write(count, 2, sequence_in, format3)
                    sheet.write(count, 3, records['package_name'], format3)
                    sheet.write(count, 4, records['product_name'], format3)
                    sheet.write(count, 5, records['product_uom_qty'], format3)
                    sheet.write(count, 6, records['width'], format3)
                    sheet.write(count, 7, records['height'], format3)
                    sheet.write(count, 8, records['maximum_weight'], format3)
                    count = count+1
                    sequence_in = sequence_in+0.1
        # checking conditions
        if data['salesman_id']:
            if data['from_date']:
                if data['to_date']:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_partner_id = %s "
                                        "AND sale_order_date >= %s AND sale_order_date <= %s",
                                        (data['salesman_id'], data['from_date'], data['to_date']))
                    bundle_records = self.env.cr.dictfetchall()
                    return filter_data()
                else:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_partner_id = %s AND sale_order_date >= %s ",
                                        (data['salesman_id'], data['from_date']))
                    bundle_records = self.env.cr.dictfetchall()
                    return filter_data()
            else:
                if data['to_date']:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_partner_id = %s "
                                        "AND sale_order_date <= %s",
                                        (data['salesman_id'], data['to_date']))
                    bundle_records = self.env.cr.dictfetchall()
                    return filter_data()
                else:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_partner_id = %s ",
                                        (data['salesman_id'],))
                    bundle_records = self.env.cr.dictfetchall()
                    return filter_data()
        else:
            if data['from_date']:
                if data['to_date']:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_order_date >= %s AND sale_order_date <= %s",
                                        (data['from_date'], data['to_date']))
                    bundle_records = self.env.cr.dictfetchall()
                    return filter_data()
                else:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_order_date >= %s ",
                                        (data['from_date'],))
                    bundle_records = self.env.cr.dictfetchall()
                    return filter_data()
            else:
                if data['to_date']:
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles "
                                        "WHERE sale_order_date <= %s",
                                        (data['to_date'],))
                    bundle_records = self.env.cr.dictfetchall()
                    return filter_data()
                else:
                    print("No filters applied")
                    self.env.cr.execute("SELECT sequence_no FROM package_bundles ")
                    bundle_records = self.env.cr.dictfetchall()
                    return filter_data()
