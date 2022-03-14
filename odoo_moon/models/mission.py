# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Mission(models.Model):
    _name = 'moon.mission'
    _description = 'Mission to the moon'

    name = fields.Char(string='Name', related='spaceship_id.name')
    spaceship_id = fields.Many2one('moon.spaceship', string='Space Ship')
    crew = fields.Many2many('moon.crew_member', ondelete='cascade')
