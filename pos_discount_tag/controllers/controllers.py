# -*- coding: utf-8 -*-
# from odoo import http


# class PosDiscount(http.Controller):
#     @http.route('/pos_discount/pos_discount/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_discount/pos_discount/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_discount.listing', {
#             'root': '/pos_discount/pos_discount',
#             'objects': http.request.env['pos_discount.pos_discount'].search([]),
#         })

#     @http.route('/pos_discount/pos_discount/objects/<model("pos_discount.pos_discount"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_discount.object', {
#             'object': obj
#         })
