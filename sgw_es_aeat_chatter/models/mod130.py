
import logging
from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError, UserError
import datetime

class sgwL10nEsAeatMod130Report(models.Model):
    _description = "AEAT 130 report modified"
    _name = "l10n.es.aeat.mod130.report"
    _inherit = ["l10n.es.aeat.mod130.report",'mail.thread']

