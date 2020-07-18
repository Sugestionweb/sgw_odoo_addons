# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError, UserError
import datetime

_logger = logging.getLogger(__name__)


class SgwPartner(models.Model):
    _inherit = "res.partner"

    name = fields.Char(track_visibility = 'onchange')
#     display_name = fields.Char(compute='_compute_display_name', store=True, index=True)
    date = fields.Date(track_visibility = 'onchange')
    title = fields.Many2one(track_visibility = 'onchange')
#     parent_id = fields.Many2one('res.partner', string='Related Company', index=True)
#     parent_name = fields.Char(related='parent_id.name', readonly=True, string='Parent name')
#     child_ids = fields.One2many('res.partner', 'parent_id', string='Contacts', domain=[('active', '=', True)])  # force "active_test" domain to bypass _search() override
    ref = fields.Char(track_visibility = 'onchange')
    lang = fields.Selection(track_visibility = 'onchange')
#     tz = fields.Selection(_tz_get, string='Timezone', default=lambda self: self._context.get('tz'),
#                           help="The partner's timezone, used to output proper date and time values "
#                                "inside printed reports. It is important to set a value for this field. "
#                                "You should use the same timezone that is otherwise used to pick and "
#                                "render date and time values: your computer's timezone.")
#     tz_offset = fields.Char(compute='_compute_tz_offset', string='Timezone offset', invisible=True)
    user_id = fields.Many2one(track_visibility = 'onchange')
    vat = fields.Char(track_visibility = 'onchange')
    bank_ids = fields.One2many(track_visibility = 'onchange')
    website = fields.Char(track_visibility = 'onchange')
#     comment = fields.Text(string='Notes')
# 
    category_id = fields.Many2many(track_visibility = 'onchange')
    credit_limit = fields.Float(track_visibility = 'onchange')
    barcode = fields.Char(track_visibility = 'onchange')
    active = fields.Boolean(track_visibility = 'onchange')
    customer = fields.Boolean(track_visibility = 'onchange')
    supplier = fields.Boolean(track_visibility = 'onchange')
    employee = fields.Boolean(track_visibility = 'onchange')
    function = fields.Char(track_visibility = 'onchange')
    type = fields.Selection(track_visibility = 'onchange')
    
    # Address Fields
    street = fields.Char(track_visibility = 'onchange')
    street2 = fields.Char(track_visibility = 'onchange')
    zip = fields.Char(track_visibility = 'onchange')
    city = fields.Char(track_visibility = 'onchange')
    state_id = fields.Many2one(track_visibility = 'onchange')
    country_id = fields.Many2one(track_visibility = 'onchange')
    email = fields.Char(track_visibility = 'onchange')

#     email_formatted = fields.Char(
#         'Formatted Email', compute='_compute_email_formatted',
#         help='Format email address "Name <email@domain>"')
    phone = fields.Char(track_visibility = 'onchange')
    mobile = fields.Char(track_visibility = 'onchange')
    is_company = fields.Boolean(track_visibility = 'onchange')
    industry_id = fields.Many2one(track_visibility = 'onchange')
#     # company_type is only an interface field, do not use it in business logic
#     company_type = fields.Selection(string='Company Type',
#         selection=[('person', 'Individual'), ('company', 'Company')],
#         compute='_compute_company_type', inverse='_write_company_type')
    company_id = fields.Many2one(track_visibility = 'onchange')
    color = fields.Integer(track_visibility = 'onchange')
    user_ids = fields.One2many(track_visibility = 'onchange')
#     partner_share = fields.Boolean(
#         'Share Partner', compute='_compute_partner_share', store=True,
#         help="Either customer (not a user), either shared user. Indicated the current partner is a customer without "
#              "access or with a limited access created for sharing data.")
#     contact_address = fields.Char(compute='_compute_contact_address', string='Complete Address')
# 
#     # technical field used for managing commercial fields
    commercial_partner_id = fields.Many2one(track_visibility = 'onchange')
    commercial_company_name = fields.Char(track_visibility = 'onchange')
    company_name = fields.Char(track_visibility = 'onchange')
# 
#     # image: all image fields are base64 encoded and PIL-supported
#     image = fields.Binary("Image", attachment=True,
#         help="This field holds the image used as avatar for this contact, limited to 1024x1024px",)
#     image_medium = fields.Binary("Medium-sized image", attachment=True,
#         help="Medium-sized image of this contact. It is automatically "\
#              "resized as a 128x128px image, with aspect ratio preserved. "\
#              "Use this field in form views or some kanban views.")
#     image_small = fields.Binary("Small-sized image", attachment=True,
#         help="Small-sized image of this contact. It is automatically "\
#              "resized as a 64x64px image, with aspect ratio preserved. "\
#              "Use this field anywhere a small image is required.")
#     # hack to allow using plain browse record in qweb views, and used in ir.qweb.field.contact
#     self = fields.Many2one(comodel_name=_name, compute='_compute_get_ids')

    property_payment_term_id = fields.Many2one(track_visibility = 'onchange')
    customer_payment_mode_id = fields.Many2one(track_visibility = 'onchange')
    