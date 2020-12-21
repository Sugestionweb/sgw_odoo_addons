# Created on 2019-08-08
# author: Javier https://www.sugestionweb.com
# email: javier@sugestionweb.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo12


{
    "name": "History Purchase Prices",
    "version": "12.0.0.1.0",
    "author": "Sugestionweb.com",
    "category": "Productivity",
    "website": "https://www.sugestionweb.com",
    "license": "AGPL-3",
    "sequence": 2,
    "summary": """

    """,
    "images": ["static/description/banner.gif"],
    "depends": [
        "base",
        "purchase"
        # 'digest',
        # when enterprise
        # 'web_mobile'
    ],
    "data": ["security/ir.model.access.csv", "views/inherited_view.xml"],
    "qweb": ["static/src/xml/*.xml"],
    "demo": [],
    "test": [],
    "css": [],
    "js": [],
    "installable": True,
    "application": True,
    "auto_install": True,
}
