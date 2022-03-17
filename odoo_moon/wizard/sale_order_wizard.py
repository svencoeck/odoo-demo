# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderWizard(models.TransientModel):
    _name = 'moon.sale.order.wizard'
    _description = 'Sale Order wizard for missions'

    mission_id = fields.Many2one('moon.mission',
                                 string='Mission',
                                 required=True)

    passenger_ids = fields.Many2many('res.partner', string='Passengers')

    def create_orders(self):
        for passenger_id in self.passenger_ids:
            sale = self.env['sale.order'].create({
                'partner_id': passenger_id.id,
                'mission_id': self.mission_id.id
            })

