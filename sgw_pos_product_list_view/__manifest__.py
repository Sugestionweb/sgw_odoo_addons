# Created on 2019-07-30
# author: Javier https://www.sugestionweb.com
# email: javier@sugestionweb.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "SGW Pos Product List View",
    "version": "12.0.0.1.0",
    "author": "Sugestionweb.com",
    "category": "Point Of Sale",
    "website": "https://www.sugestionweb.com",
    "license": "AGPL-3",
    "sequence": 2,
    "summary": """
    This module modifies the screen of the products at the point of sale to see
    them in list mode.
    """,
    "images": ["static/description/icon.png"],
    "depends": [
        "point_of_sale",
        # 'digest',
        # when enterprise
        # 'web_mobile'
    ],
    "data": ["views/point_of_sale_assets.xml"],
    "qweb": ["static/xml/pos.xml"],
    "demo": [],
    "test": [],
    "css": [],
    "js": [],
    "installable": True,
    "application": False,
    "auto_install": False,
}
