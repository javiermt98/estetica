# -*- coding: utf-8 -*-
{
    'name': "Estetica",

    'summary': """
       Gestion de un centro de estética, parte financiera y personal
       """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Javier Manez",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/estetica_security_view.xml',
        'security/ir.model.access.csv',
        'views/empleados_view.xml',
        'views/clientes_view.xml',
        'views/facturas_view.xml',
        'views/productos_view.xml',
        'views/tratam_view.xml',
        'views/proveedor_view.xml',
        'views/menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application':True,
    'installable':True,
}
