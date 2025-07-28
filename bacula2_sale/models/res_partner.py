from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    is_technical_contact = fields.Boolean("Technical contact")
