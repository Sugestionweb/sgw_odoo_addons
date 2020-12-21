# Created on 2019-07-14
# author: Javier https://www.sugestionweb.com
# email: javier@sugestionweb.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo12


{
    "name": "Decorate Sale Orders Tree",
    "version": "12.0.0.1.0",
    "author": "Sugestionweb.com",
    "category": "Productivity",
    "website": "https://www.sugestionweb.com",
    "license": "AGPL-3",
    "sequence": 2,
    "summary": """
    Customize the Sale orders tree to decorate the lines with diferent colors \
    depending of the order status and invoiced status.
    """,
    "images": ["static/description/banner.gif"],
    "depends": [
        "base",
        "sale"
        # 'digest',
        # when enterprise
        # 'web_mobile'
    ],
    "data": ["views/inherited_so.xml"],
    "qweb": ["static/src/xml/*.xml"],
    "demo": [],
    "test": [],
    "css": [],
    "js": [],
    "installable": True,
    "application": False,
    "auto_install": True,
}
