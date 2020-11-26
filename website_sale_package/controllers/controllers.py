# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class WebsiteSalePackage(http.Controller):
    @http.route('/sale_package/form', type="http", auth='public', website=True)
    def sales_package_form(self, **kw):
        print('Page loaded')
        # return 'hello'
        return http.request.render('website_sale_package.create_sales_package', {})

    @http.route('/sale_package/form/submit', type="http", auth='public', website=True)
    def create_package(self, **kw):
        request.env['sales.package'].sudo().create(kw)
        print('Second one loaded')
        return 'hello'
        # return request.render('website_sale_package.package_thanks', {})
