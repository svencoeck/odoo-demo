# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

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

    notes = fields.Text(string='Notes')

    fuel_cost = fields.Float(string='Fuel cost / month', default=0.00)

    maintenance_cost = fields.Float(string='Maintenance cost / year', default=0.00)

    total_cost = fields.Float(string='Total cost / year', readonly=True)

    @api.onchange('fuel_cost', 'maintenance_cost')
    def _onchange_total_cost(self):
        total_cost = (self.fuel_cost * 12) + self.maintenance_cost
        if (total_cost > 2000.00):
            raise UserError('The upkeep cost is to high')

        self.total_cost = total_cost

    @api.constrains('maintenance_cost')
    def _constraint_maintenance_cost(self):
        for record in self:
            if (record.maintenance_cost < 20.00):
                raise ValidationError('The maintenance cost needs to be higher than 20.00: %s' % record.maintenance_cost)


