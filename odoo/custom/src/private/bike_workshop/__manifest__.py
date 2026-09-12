{
    "name": "Bike Workshop",
    "summary": "Ordem de Servico for Bike ERP, built on top of sale.order",
    "version": "18.0.1.0.0",
    "category": "Bike ERP",
    "author": "Nathan Gobbi",
    "license": "AGPL-3",
    "depends": ["bike_base", "sale", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_order_workshop_views.xml",
        "wizard/bike_workshop_barcode_scan_views.xml",
    ],
    "installable": True,
    "application": False,
}
