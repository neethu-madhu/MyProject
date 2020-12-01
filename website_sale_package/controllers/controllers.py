# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class WebsiteSalePackage(http.Controller):
    @http.route('/sale_package/form', type="http", auth='public', website=True)
    def sales_package_form(self, **post):
        print('Page loaded')
        return request.render('website_sale_package.create_sales_package', {})

    @http.route(['/sale_package/form/submit'], type='http', auth="public", website=True)
    # next controller with url for submitting data from the form#
    def customer_form_submit(self, **post):
        partner = request.env['sales.package'].create({
            'package_name': post.get('package_name'),
            'width': post.get('width'),
            'height': post.get('height'),
            'length': post.get('length'),
            'maximum_weight': post.get('maximum_weight'),
        })
        vals = {
            'partner': partner,
        }
        # inherited the model to pass the values to the model from the form#
        return request.render("website_sale_package.package_thanks", vals)
