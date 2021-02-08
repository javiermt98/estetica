# -*- coding: utf-8 -*-
# from odoo import http


# class Estetica(http.Controller):
#     @http.route('/estetica/estetica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estetica/estetica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('estetica.listing', {
#             'root': '/estetica/estetica',
#             'objects': http.request.env['estetica.estetica'].search([]),
#         })

#     @http.route('/estetica/estetica/objects/<model("estetica.estetica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estetica.object', {
#             'object': obj
#         })
