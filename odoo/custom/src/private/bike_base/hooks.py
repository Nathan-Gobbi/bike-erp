MODULES_HIDDEN = {
    "mail",  # Discuss
    "spreadsheet_dashboard",  # Dashboards
    "link_tracker",  # Link Tracker
    "contacts",  # native Contacts app, replaced by bike_base's own menu
    "sale",  # native Sales app, replaced by bike_workshop's Ordem de Serviço
}

MODULES_MANAGER_ONLY = {
    "account",  # Invoicing/Accounting
    "stock",  # Inventory
}


def post_init_bike_base(env):
    """Declutter the app switcher for the Bike ERP profiles.

    Native top-level apps that duplicate a bike_base/bike_workshop menu (or
    are simply not needed for this operation) are hidden from everyone by
    restricting them to base.group_no_one (nobody has it in normal use).
    A couple of native apps (Inventory, Invoicing) are kept, but only for
    Administrador Bike ERP, as a power-user fallback.

    Identified by the technical module that created each top menu (via
    ir.model.data), not by name, so this keeps working regardless of the
    user's UI language.
    """
    menu_model = env["ir.ui.menu"]
    imd_model = env["ir.model.data"]
    group_no_one = env.ref("base.group_no_one")
    group_bike_manager = env.ref("bike_base.group_bike_manager")

    top_menus = menu_model.search([("parent_id", "=", False)])
    for menu in top_menus:
        imd = imd_model.search(
            [("model", "=", "ir.ui.menu"), ("res_id", "=", menu.id)], limit=1
        )
        if not imd:
            continue
        if imd.module in MODULES_HIDDEN:
            menu.groups_id = [(6, 0, [group_no_one.id])]
        elif imd.module in MODULES_MANAGER_ONLY:
            menu.groups_id = [(6, 0, [group_bike_manager.id])]
