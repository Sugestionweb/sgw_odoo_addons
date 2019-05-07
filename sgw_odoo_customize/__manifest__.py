# -*- coding: utf-8 -*-

# Created on 2019-04-20
# author: Javier https://www.sugestionweb.com
# email: javier@sugestionweb.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo12


{
    'name': 'Odoo Customized Sugestionweb',
    'version': '1.1.1.01',
    'author': 'Sugestionweb.com',
    'category': 'Productivity',
    'website': 'https://www.sugestionweb.com',
    'license': 'AGPL-3',
    'sequence': 2,
    'summary': """    
    Customize odoo. 
    """,
    'description': """

    """,
    'images': ['static/description/banner.gif'],
    'depends': [
        'base',
        'web',
        'mail',
        'web_settings_dashboard',
        'iap',
        # 'digest',
        # when enterprise
        # 'web_mobile'
    ],
    'data': [
        'views/sgw_odoo_customize_view.xml',
        'views/sgw_theme_config_settings_view.xml',
        'views/ir_model_view.xml',
        'views/website_templates.xml',
        # data
        'data/ir_config_parameter.xml',
        'data/ir_module_module.xml',
        'data/res_groups.xml',
        'security/ir.model.access.csv',
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
