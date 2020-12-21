import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class SgwPartner(models.Model):
    _inherit = "res.partner"

    name = fields.Char(track_visibility="onchange")
    date = fields.Date(track_visibility="onchange")
    title = fields.Many2one(track_visibility="onchange")
    ref = fields.Char(track_visibility="onchange")
    lang = fields.Selection(track_visibility="onchange")
    user_id = fields.Many2one(track_visibility="onchange")
    vat = fields.Char(track_visibility="onchange")
    bank_ids = fields.One2many(track_visibility="onchange")
    website = fields.Char(track_visibility="onchange")
    category_id = fields.Many2many(track_visibility="onchange")
    credit_limit = fields.Float(track_visibility="onchange")
    barcode = fields.Char(track_visibility="onchange")
    active = fields.Boolean(track_visibility="onchange")
    customer = fields.Boolean(track_visibility="onchange")
    supplier = fields.Boolean(track_visibility="onchange")
    employee = fields.Boolean(track_visibility="onchange")
    function = fields.Char(track_visibility="onchange")
    type = fields.Selection(track_visibility="onchange")

    # Address Fields
    street = fields.Char(track_visibility="onchange")
    street2 = fields.Char(track_visibility="onchange")
    zip = fields.Char(track_visibility="onchange")
    city = fields.Char(track_visibility="onchange")
    state_id = fields.Many2one(track_visibility="onchange")
    country_id = fields.Many2one(track_visibility="onchange")
    email = fields.Char(track_visibility="onchange")
    phone = fields.Char(track_visibility="onchange")
    mobile = fields.Char(track_visibility="onchange")
    is_company = fields.Boolean(track_visibility="onchange")
    industry_id = fields.Many2one(track_visibility="onchange")
    company_id = fields.Many2one(track_visibility="onchange")
    color = fields.Integer(track_visibility="onchange")
    user_ids = fields.One2many(track_visibility="onchange")
    commercial_partner_id = fields.Many2one(track_visibility="onchange")
    commercial_company_name = fields.Char(track_visibility="onchange")
    company_name = fields.Char(track_visibility="onchange")
    property_payment_term_id = fields.Many2one(track_visibility="onchange")
    customer_payment_mode_id = fields.Many2one(track_visibility="onchange")
