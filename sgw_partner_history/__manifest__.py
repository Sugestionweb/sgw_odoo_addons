# Created on 2019-12-18
# author: Javier https://www.sugestionweb.com
# email: javier@sugestionweb.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo12


{
    "name": "SGW Partner History",
    "version": "12.0.0.1.0",
    "author": "Sugestionweb.com",
    "category": "Productivity",
    "website": "https://www.sugestionweb.com",
    "license": "AGPL-3",
    "sequence": 2,
    "summary": """
    Save a note automatically whenever you change the value of any field
    in the partner table
    """,
    "images": ["static/description/banner.gif"],
    "depends": ["base"],
    "data": [
        # data
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
