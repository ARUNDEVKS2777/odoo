
from odoo import http
from odoo.http import content_disposition, request


class RecentViewedProducts(http.Controller):
    @http.route('/get_product', auth='public', type='json', website=True)
    def products_recently_viewed_update(self, **kwargs):
        visitor_sudo = request.env['website.visitor']._get_visitor_from_request \
            (force_create=True)
        prod = request.env['website.track'].search([('visitor_id.id', '=', visitor_sudo.id)]).mapped('product_id')
        values = {'product_id': prod}
        response = http.Response(template='website_recent_products.snippet_recent_view',
                                 qcontext=values)
        return response.render()
