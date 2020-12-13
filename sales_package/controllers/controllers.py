# -*- coding: utf-8 -*-
# from odoo import http


# class SalesPackage(http.Controller):
#     @http.route('/sales_package/sales_package/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_package/sales_package/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_package.listing', {
#             'root': '/sales_package/sales_package',
#             'objects': http.request.env['sales_package.sales_package'].search([]),
#         })

#     @http.route('/sales_package/sales_package/objects/<model("sales_package.sales_package"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_package.object', {
#             'object': obj
#         })
