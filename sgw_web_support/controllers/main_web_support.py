# ------------------------------------------------------------------------------
# # (c) 2020 Sugestionweb.com -  javier@sugestionweb.com
# # License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# ------------------------------------------------------------------------------
import werkzeug

import odoo.http as http

from odoo.addons.website_support.controllers.main import SupportTicketController


class SupportTicketExtended(SupportTicketController):
    @http.route(
        "/support/portal/ticket/view/<portal_access_key>",
        type="http",
        auth="user",
        website=True,
    )
    def support_portal_ticket_view(self, portal_access_key):

        support_ticket = (
            http.request.env["website.support.ticket"]
            .sudo()
            .search([("portal_access_key", "=", portal_access_key)])[0]
        )

        # Only the ticket owner can view the ticket with the portal_access_key specified
        if support_ticket.partner_id.id == http.request.env.user.partner_id.id:
            response = super().support_portal_ticket_view(portal_access_key)
            return response
        else:
            return werkzeug.utils.redirect("/web/login")
