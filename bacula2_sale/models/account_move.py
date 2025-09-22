from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _message_auto_subscribe_followers(self, *args, **kw):
        res = super()._message_auto_subscribe_followers(*args, **kw)
        salesperson = self.invoice_line_ids.sale_line_ids.order_id.user_id.partner_id
        if salesperson == self.env.user.partner_id:
            return res

        new_res = []
        for x in res:
            if salesperson.id != x[0]:
                new_res.append(x)

        return new_res
