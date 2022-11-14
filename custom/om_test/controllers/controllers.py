# -*- coding: utf-8 -*-
# from odoo import http


# class OmTest(http.Controller):
#     @http.route('/om_test/om_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_test/om_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_test.listing', {
#             'root': '/om_test/om_test',
#             'objects': http.request.env['om_test.om_test'].search([]),
#         })

#     @http.route('/om_test/om_test/objects/<model("om_test.om_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_test.object', {
#             'object': obj
#         })
