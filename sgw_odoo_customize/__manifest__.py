# ------------------------------------------------------------------------------
# (c) 2020 Sugestionweb.com -  javier@sugestionweb.com
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# Created on 2019-04-20
# Author: Javier https://www.sugestionweb.com
# Email: javier@sugestionweb.com
# -------------------------------------------------------------------------------

{
    "name": "Odoo Customized Sugestionweb",
    "version": "12.0.0.1.0",
    "author": "Sugestionweb.com",
    "category": "Productivity",
    "website": "https://www.sugestionweb.com",
    "license": "AGPL-3",
    "sequence": 2,
    "summary": """
    Customize odoo.
    """,
    "images": ["static/description/banner.gif"],
    "depends": [
        "base",
        "web",
        "mail",
        "web_settings_dashboard",
        "iap",
        # 'digest',
        # when enterprise
        # 'web_mobile'
    ],
    "data": [
        "views/sgw_odoo_customize_view.xml",
        "views/sgw_theme_config_settings_view.xml",
        "views/ir_model_view.xml",
        "views/website_templates.xml",
        # data
        "data/ir_config_parameter.xml",
        "data/ir_module_module.xml",
        "data/res_groups.xml",
        "security/ir.model.access.csv",
    ],
    "qweb": ["static/src/xml/*.xml"],
    "demo": [],
    "test": [],
    "css": [],
    "js": [],
    "installable": True,
    "application": True,
    "auto_install": True,
}
