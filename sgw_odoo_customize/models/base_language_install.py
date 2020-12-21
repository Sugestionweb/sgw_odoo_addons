# ------------------------------------------------------------------------------
# # (c) 2020 Sugestionweb.com -  javier@sugestionweb.com
# # License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# ------------------------------------------------------------------------------
from odoo import api, models


class BaseLanguageInstall(models.TransientModel):
    _inherit = "base.language.install"

    @api.multi
    def lang_install(self):
        self.ensure_one()
        if self.overwrite:
            self.env.cr.execute("""
                delete from ir_translation
                where lang=%s
                """, (self.lang,))
        return super(BaseLanguageInstall, self).lang_install()
