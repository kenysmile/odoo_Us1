# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions

class Giaoan(models.Model):
    _name = 'th.giaoan'

    name = fields.Char('Giáo án')