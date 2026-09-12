from odoo import fields, models
from odoo.exceptions import UserError


class BikeWorkshopBarcodeScan(models.TransientModel):
    _name = "bike.workshop.barcode.scan"
    _description = "Scan a barcode to add a product to an Ordem de Serviço"

    order_id = fields.Many2one("sale.order", required=True)
    barcode = fields.Char(string="Código de barras")

    def action_scan(self):
        self.ensure_one()
        code = (self.barcode or "").strip()
        if not code:
            raise UserError(self.env._("Informe um código de barras."))

        products = self.env["product.product"].search([("barcode", "=", code)])
        if not products:
            raise UserError(
                self.env._(
                    "Nenhum produto encontrado para o código de barras %s.", code
                )
            )
        if len(products) > 1:
            raise UserError(
                self.env._(
                    "Mais de um produto usa o código de barras %s."
                    " Corrija o cadastro antes de continuar.",
                    code,
                )
            )
        product = products

        line = self.order_id.order_line.filtered(lambda sol: sol.product_id == product)
        if line:
            line[0].product_uom_qty += 1
        else:
            self.env["sale.order.line"].create(
                {
                    "order_id": self.order_id.id,
                    "product_id": product.id,
                    "product_uom_qty": 1,
                }
            )

        self.barcode = False
        return {
            "type": "ir.actions.act_window",
            "name": self.env._("Escanear Código de Barras"),
            "res_model": self._name,
            "res_id": self.id,
            "view_mode": "form",
            "target": "new",
        }
