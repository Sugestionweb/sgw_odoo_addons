# ------------------------------------------------------------------------------
# # (c) 2020 Sugestionweb.com -  javier@sugestionweb.com
# # License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# ------------------------------------------------------------------------------

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class View(models.Model):
    _inherit = "ir.ui.view"

    @api.model
    def render_template(self, template, values=None, engine="ir.qweb"):
        if template in ["web.login", "web.webclient_bootstrap"]:
            if not values:
                values = {}
            values["title"] = (
                self.env["ir.config_parameter"]
                .sudo()
                .get_param("sgw_system_name", "Sugestionweb")
            )
        return super(View, self).render_template(template, values=values, engine=engine)
