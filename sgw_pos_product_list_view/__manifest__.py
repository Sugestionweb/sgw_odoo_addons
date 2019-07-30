# -*- coding: utf-8 -*-

# Created on 2019-07-30
# author: Javier https://www.sugestionweb.com
# email: javier@sugestionweb.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo12
{
    'name': 'SGW Pos Product List View',
    'version': '1.1.1.01',
    'author': 'Sugestionweb.com',
    'category': 'POS',
    'website': 'https://www.sugestionweb.com',
    'license': 'AGPL-3',
    'sequence': 2,
    'summary': """    
    This module modifies the screen of the products at the point of sale to see them in list mode. 
    """,
    'description': """
    This module modifies the screen of the products at the point of sale to see them in list mode, saving space and without displaying the image of the product.
    """,
    'images': ['static/description/icon.png'],
    'depends': [
        'point_of_sale',
        # 'digest',
        # when enterprise
        # 'web_mobile'
    ],
    'data': [
        'views/point_of_sale_assets.xml',
    ],
    'qweb': ['static/xml/pos.xml'],
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': True,
}
