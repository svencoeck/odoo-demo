# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    mission_id = fields.Many2one('moon.mission', string="Mission")