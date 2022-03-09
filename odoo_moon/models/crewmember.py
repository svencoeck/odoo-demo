# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrewMember(models.Model):
    _name = 'moon.crew_member'
    _description = 'Moon Crew Member'

    name = fields.Char(string='Name', required=True)
    day_of_birth = fields.Date(string='Day of birth', required=True)
    function = fields.Selection(string='Function', selection=[
        ('pilot', 'Pilot'),
        ('medical', 'Medical'),
        ('technical', 'Technical')
    ], required=True)

    photo = fields.Image(string='Photo')

    spaceship_id = fields.Many2one('moon.spaceship', string='Space Ship')

