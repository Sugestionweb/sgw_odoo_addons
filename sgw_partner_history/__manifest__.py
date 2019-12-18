# -*- coding: utf-8 -*-

# Created on 2019-12-18
# author: Javier https://www.sugestionweb.com
# email: javier@sugestionweb.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo12


{
    'name': 'SGW Partner History',
    'version': '1.1.1.01',
    'author': 'Sugestionweb.com',
    'category': 'Productivity',
    'website': 'https://www.sugestionweb.com',
    'license': 'AGPL-3',
    'sequence': 2,
    'summary': """    
    Save a note automatically whenever you change the value of any field 
    in the partner table
    """,
    'description': """
    Save a note automatically whenever you change the value of any field 
    in the partner table
    """,
    'images': ['static/description/banner.gif'],
    'depends': [
        'base',
    ],
    'data': [
        # data

    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
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
