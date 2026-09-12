{
    "name": "Bike Base",
    "summary": "Foundation module for Bike ERP: menu, category and security groups",
    "version": "18.0.1.0.0",
    "category": "Bike ERP",
    "author": "Nathan Gobbi",
    "license": "AGPL-3",
    "depends": ["base", "mail", "product", "sale", "stock", "account"],
    "data": [
        "security/bike_security.xml",
        "security/ir.model.access.csv",
        "views/bike_menus.xml",
        "data/product_category_data.xml",
    ],
    "demo": [
        "demo/product_demo.xml",
    ],
    "installable": True,
    "application": True,
}
