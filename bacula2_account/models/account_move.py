from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def action_send_and_print(self):
        res = super().action_send_and_print()
        res["context"][
            "default_email_layout_xmlid"
        ] = "bacula2_mail.mail_notification_layout"
        return
