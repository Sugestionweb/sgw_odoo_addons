# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp

_logger = logging.getLogger(__name__)

class SgwProduct(models.Model):
    _inherit = "product.template"
    historyprices_ids = fields.One2many('sgw.purchase.prices', 'product_id', label='History', help="Prices History.")


class HistoryPurchasePrices(models.Model):
     
    _name = 'sgw.purchase.prices'
    _description = "History for Purchase Prices"
    _order = 'date_change desc'
    
    origin = fields.Char('Source Document', copy=False,
        help="Reference of the document that generated this entry "
             "(e.g. a purchase order)")
    
    product_id = fields.Many2one('product.template', string='Product', 
                                 domain=[('purchase_ok', '=', True)], 
                                 change_default=True, required=True,
                                 ondelete='cascade')
    
    date_change = fields.Datetime('Change Date', required=True, 
                                 index=True, 
                                 copy=False, default=fields.Datetime.now,\
                                help="Date")
    
    partner_id = fields.Many2one('res.partner', 
                                 string='Vendor', 
                                 required=True, 
                                 change_default=True, 
                                 track_visibility='always', 
        help="You can find a vendor by its Name, TIN, Email or Internal "
            "Reference.")
    
    price_old = fields.Float(string='Price Old', required=True, 
                              digits=dp.get_precision('Product Price'))
    
    price_updated = fields.Float(string='Price Updated', required=True, 
                              digits=dp.get_precision('Product Price'))
    
    
    