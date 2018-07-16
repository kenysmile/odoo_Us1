# -*- coding: utf-8 -*-

from odoo import fields, models

class Truonghoc(models.Model):
    _name = 'th.truonghoc'

    name = fields.Char('Tên trường')
    diachi = fields.Char('Địa chỉ')
    tinhtrang = fields.Selection([('1', 'Đang hoạt động'), ('2', 'Chưa hoạt động')], 'Tình trạng')
    giaovien_ids = fields.One2many('th.giaovien', 'name', string='Giáo viên')