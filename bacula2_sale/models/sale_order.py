from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _compute_partner_shipping_id(self):
        Partners = self.env["res.partner"]
        others = self

        for order in self:
            tc = Partners.search(
                [
                    ("is_technical_contact", "=", True),
                    ("parent_id", "=", order.partner_id.commercial_partner_id.id),
                ]
            )
            if len(tc) > 1:
                tc = tc.sorted(key=lambda r: 0 if r.type == "delivery" else 1)[0]

            if tc:
                order.partner_shipping_id = tc
                others -= order
                continue

        return super(SaleOrder, others)._compute_partner_shipping_id()
