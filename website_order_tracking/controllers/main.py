from odoo import http, _
from odoo.http import request


class OrderTracking(http.Controller):
    @http.route('/track', auth='public', type='http', website=True)
    def order_track(self, **post):
        return request.render('website_order_tracking.order_tracking_template')


class OrderTrackingView(http.Controller):
    @http.route('/track_view', type='http', auth='public', method=['POST'], website=True, csrf=False)
    def order_track_view(self, **kw):
        done = False
        ready = False
        # from_loc = False
        # to_loc = False
        print('post', kw.get('search'))
        if kw.get('search'):
            wh_out = request.env['stock.picking'].search([('origin', '=', kw.get('search'))])
            print('from------------', wh_out.from_place.id)
            if wh_out:
                print('source doc', wh_out.from_place)
                if wh_out.state == 'done':
                    done = ready = True
                    # from_loc = wh_out.from_place
                    # to_loc = wh_out.to_place
                if wh_out.state == 'assigned':
                    ready = True
                    # from_loc = wh_out.from_place
                values = {'data': wh_out}
                return request.render(template='website_order_tracking.order_tracking_view', qcontext=values)
            else:
                return request.render(template='website_order_tracking.warning')

        else:
            print("empty")
            return request.render(template='website_order_tracking.warning')
