# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):

    _name = 'moon.spaceship'
    _description = 'Spaceship'

    name = fields.Char(string='Name of ship', required=True)
    ship_type = fields.Char(string='Ship type')
    fuel_type = fields.Selection(string='Fuel type',
                                 selection=[('nuclear', 'Nuclear'),
                                            ('electric', 'Electric')],
                                 default='electric',
                                 copy=False)

    passengers = fields.Integer(string='Number of passengers')

    active = fields.Boolean(string='Active', default=True)
