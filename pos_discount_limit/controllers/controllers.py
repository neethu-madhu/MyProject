# -*- coding: utf-8 -*-
# from odoo import http


# class PosDiscountLimit(http.Controller):
#     @http.route('/pos_discount_limit/pos_discount_limit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_discount_limit/pos_discount_limit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_discount_limit.listing', {
#             'root': '/pos_discount_limit/pos_discount_limit',
#             'objects': http.request.env['pos_discount_limit.pos_discount_limit'].search([]),
#         })

#     @http.route('/pos_discount_limit/pos_discount_limit/objects/<model("pos_discount_limit.pos_discount_limit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_discount_limit.object', {
#             'object': obj
#         })
