# -*- coding: utf-8 -*-
# Part of IT IS AG. See LICENSE file for full copyright and licensing details.

{
    'name': 'IT IS delivery date in line',
    'version': '1.0',
    'sequence': 1,
    'summary': """Added delivery date in line.""",
    'description': """This modules provides the functionality to add delivery dates per line on sale-orders and purchase orders.
        These dates reflect on the according reports for the order confirmation for example.
        The dates on the lines do not reflect on the according warehouse transfers.
        """,
    'category': 'Sales',
    'author': 'IT IS AG',
    'website': 'http://www.itis.de',
    'depends': ['sale_management', 'purchase'],
    'data': [
        # 'views/assets.xml',
    ],
    'demo': [
    ],
    'assets': {
        'web.assets_backend': [
            'itis_lines_delivery_date/static/src/js/form_view.js',
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
}
