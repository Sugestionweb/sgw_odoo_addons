import logging

from odoo import api, fields, models
from odoo.exceptions import AccessError

_logger = logging.getLogger(__name__)


class SgwPurchase(models.Model):
    _inherit = "purchase.order"

    @api.multi
    def _add_supplier_to_product(self):
        # Add the partner in the supplier list of the product if the supplier
        # is not registered for this product. We limit to 10 the number of
        # suppliers for a product to avoid the mess that could be caused for
        # some generic products ("Miscellaneous").

        for line in self.order_line:
            # Do not add a contact as a supplier
            partner = (
                self.partner_id
                if not self.partner_id.parent_id
                else self.partner_id.parent_id
            )
            currency = (
                partner.property_purchase_currency_id
                or self.env.user.company_id.currency_id
            )
            price = self.currency_id._convert(
                line.price_unit,
                currency,
                line.company_id,
                line.date_order or fields.Date.today(),
                round=False,
            )

            if (
                partner not in line.product_id.seller_ids.mapped("name")
                and len(line.product_id.seller_ids) <= 10
            ):
                search_last_price_stored = 0  # We don't have partner / history

                supplierinfo = {
                    "name": partner.id,
                    "sequence": max(line.product_id.seller_ids.mapped("sequence")) + 1
                    if line.product_id.seller_ids
                    else 1,
                    "product_uom": line.product_uom.id,
                    "min_qty": 0.0,
                    "price": price,
                    "currency_id": currency.id,
                    "delay": 0,
                }
                vals = {
                    "seller_ids": [(0, 0, supplierinfo)],
                }

                try:
                    line.product_id.write(vals)
                except AccessError:  # no write access rights -> just ignore
                    break

                # Save First History Record
                history_info = {
                    "origin": line.order_id.name,
                    "product_id": line.product_id.id,
                    "partner_id": partner.id,
                    "price_old": search_last_price_stored,
                    "price_updated": price,
                }

                vals = {
                    "historyprices_ids": [(0, 0, history_info)],
                }

                try:
                    line.product_id.write(vals)
                except AccessError:  # no write access rights -> just ignore
                    break

            else:

                id_supplier_info = line.product_id.seller_ids[0].id

                supplierinfo = {
                    "price": price,
                    "currency_id": currency.id,
                }

                vals = {
                    "seller_ids": [(1, id_supplier_info, supplierinfo)],
                }

                try:
                    line.product_id.write(vals)
                except AccessError:  # no write access rights -> just ignore
                    break

                obj_history = self.env["sgw.purchase.prices"]
                search_last_price_stored = obj_history.search(
                    [
                        ("product_id", "=", line.product_id.id),
                        ("partner_id", "=", partner.id),
                    ],
                    limit=1,
                )["price_updated"]

                # Save History Record
                history_info = {
                    "origin": line.order_id.name,
                    "product_id": line.product_id.id,
                    "partner_id": partner.id,
                    "price_old": search_last_price_stored,
                    "price_updated": price,
                }

                vals = {
                    "historyprices_ids": [(0, 0, history_info)],
                }

                try:
                    line.product_id.write(vals)
                except AccessError:  # no write access rights -> just ignore
                    break
