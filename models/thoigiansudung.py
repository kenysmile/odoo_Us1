# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions

class Thoigiansudung(models.Model):
    _name = 'th.thoigiansudung'

    giaovien = fields.Char('Giáo viên')
