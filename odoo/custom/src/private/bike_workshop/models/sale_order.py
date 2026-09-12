from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_open_barcode_scan(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": self.env._("Escanear Código de Barras"),
            "res_model": "bike.workshop.barcode.scan",
            "view_mode": "form",
            "target": "new",
            "context": {"default_order_id": self.id},
        }
