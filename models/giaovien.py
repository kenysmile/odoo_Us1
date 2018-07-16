# -*- coding: utf-8 -*-

from odoo import fields, models

class Giaovien(models.Model):
    _name = 'th.giaovien'

    name = fields.Char('Tên giáo viên')
    truonghoc_id = fields.Many2one('th.truonghoc', string='Tên trường')
    lop = fields.Char('Lớp')
    email = fields.Char('Email')
    pas = fields.Char('Pass')
    sdt = fields.Integer('Số điện thoại')
    thoigiansudung_ids = fields.One2many('th.thoigiansudung', 'giaovien', string='Thời gian sử dụng')