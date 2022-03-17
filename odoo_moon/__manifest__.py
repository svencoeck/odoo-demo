# -*- coding: utf-8 -*-

{
    'name': "Odoo Moon",
    'summary': """App to organize the logistics of going to the moon""",
    'description': """
        Organize the logistics of going to the moon, this includes:
            - Spaceships
            - Space crew
    """,

    'author': 'Evato BV',
    'website': 'https://evato.be',
    'category': 'Space Travel',
    'depends': ['sale'],
    'data': [
        'security/odoo_moon.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/sale_order_inherit.xml',
        'wizard/sale_order_wizard.xml',
    ],
    'demo': [
        'demo/spaceship_demo.xml'
    ],

    'application': True
}