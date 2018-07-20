# -*- coding: utf-8 -*-

from odoo import fields, models

class ResUsers(models.Model):
    _inherit = 'res.users'

    giaovien = fields.Many2one('th.giaovien', string='Giáo viên')