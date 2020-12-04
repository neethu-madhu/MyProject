#  -*- coding: utf-8 -*-
#  from addons.web.controllers.main import env
# from odoo import http
# from odoo.http import request
#  from werkzeug.exceptions import NotFound
#  from odoo.addons.http_routing.models.ir_http import slug
# from odoo.addons.website_sale.controllers.main import QueryURL, WebsiteSale
#  from addons.website_sale.controllers.main import TableCompute


# class WebsiteSale(WebsiteSale):
#     @http.route([
#         '''/shop''',
#         '''/shop/page/<int:page>''',
#         '''/shop/brand/<model("product.brand"):brand>''',
#         '''/shop/brand/<model("product.brand"):brand>/page/<int:page>'''
#     ], type='http', auth="public", website=True)
#     def shop(self, page=0, brand=None, search='', ppg=False, **post):
#         add_qty = int(post.get('add_qty', 1))

#         Brand = request.env['product.brand']
#         print('Category', Brand)
#         if brand:
#             brand = Brand.search([('id', '=', int(brand))], limit=1)
#             print('category', brand)
#         product_obj = request.env['product.template']
#         print('product_obj', product_obj)
#         products = product_obj.sudo().search([])
#         print('products', products)
#
#         print('add_qty', add_qty)
#         Brand = request.env['product.brand']
#         print('Category', Brand)
#         if brand:
#             brand = Brand.search([('id', '=', int(brand))], limit=1)
#             print('category', brand)
#             if not brand or not brand.can_access_from_current_website():
#                 raise NotFound()
#         else:
#             brand = Brand
#
#         if ppg:
#             try:
#                 ppg = int(ppg)
#                 print('ppg', ppg)
#                 post['ppg'] = ppg
#             except ValueError:
#                 ppg = False
#         if not ppg:
#             ppg = request.env['website'].get_current_website().shop_ppg or 20
#
#         ppr = request.env['website'].get_current_website().shop_ppr or 4
#
#         attrib_list = request.httprequest.args.getlist('attrib')
#         print('attrib_list', attrib_list)
#         attrib_values = [[int(x) for x in v.split("-")] for v in attrib_list if v]
#         print('attrib_values', attrib_values)
#         attributes_ids = {v[0] for v in attrib_values}
#         print('attributes_ids', attributes_ids)
#         attrib_set = {v[1] for v in attrib_values}
#         print('attrib_set', attrib_set)
#
#         domain = self._get_search_domain(search, brand, attrib_values)
#         print('domain', domain)
#
#         keep = QueryURL('/shop', brand=brand and int(brand), search=search, attrib=attrib_list,
#                         order=post.get('order'))
#         print('keep', keep)
#
#         pricelist_context, pricelist = self._get_pricelist_context()
#
#         request.context = dict(request.context, pricelist=pricelist.id, partner=request.env.user.partner_id)
#
#         url = "/shop"
#         if search:
#             post["search"] = search
#         if attrib_list:
#             post['attrib'] = attrib_list
#
#         Product = request.env['product.template'].with_context(bin_size=True)
#         print('Product', Product)
#
#         search_product = Product.search(domain, order=self._get_search_order(post))
#         print('search_product', search_product)
#         website_domain = request.website.website_domain()
#         print('website_domain', website_domain)
#         brand_domain = [('parent_id', '=', False)] + website_domain
#         print('brand_domain', brand_domain)
#         if search:
#             search_categories = Brand.search(
#                 [('product_tmpl_ids', 'in', search_product.ids)] + website_domain).parents_and_self
#             brand_domain.append(('id', 'in', search_categories.ids))
#         else:
#             search_categories = Brand
#         brands = Brand.search(brand_domain)
#         print('brands', brands)
#
#         if brand:
#             url = "/shop/brand/%s" % slug(brand)
#             print('url', url)
#
#         product_count = len(search_product)
#         pager = request.website.pager(url=url, total=product_count, page=page, step=ppg, scope=7, url_args=post)
#         offset = pager['offset']
#         products = search_product[offset: offset + ppg]
#
#         ProductAttribute = request.env['product.attribute']
#         print('ProductAttribute', ProductAttribute)
#         if products:
#             # get all products without limit
#             attributes = ProductAttribute.search([('product_tmpl_ids', 'in', search_product.ids)])
#             print('attributes', attributes)
#         else:
#             attributes = ProductAttribute.browse(attributes_ids)
#
#         layout_mode = request.session.get('website_sale_shop_layout_mode')
#         print('layout_mode', layout_mode)
#         if not layout_mode:
#             if request.website.viewref('website_sale.products_list_view').active:
#                 layout_mode = 'list'
#             else:
#                 layout_mode = 'grid'
#
#         values = {
#             'search': search,
#             'category': brand,
#             'attrib_values': attrib_values,
#             'attrib_set': attrib_set,
#             'pager': pager,
#             'pricelist': pricelist,
#             'add_qty': add_qty,
#             'products': products,
#             'search_count': product_count,  # common for all searchbox
#             'bins': TableCompute().process(products, ppg, ppr),
#             'ppg': ppg,
#             'ppr': ppr,
#             'categories': brands,
#             'attributes': attributes,
#             'keep': keep,
#             'search_categories_ids': search_categories.ids,
#             'layout_mode': layout_mode,
#         }
#         if brand:
#             values['main_object'] = brand
#         return request.render("website_sale.products", values)
