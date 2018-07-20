# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions

class Giaovien(models.Model):
    _name = 'th.giaovien'

    name = fields.Char('Tên giáo viên')
    user_id = fields.Many2one('res.users', string='User_id')
    truong = fields.Many2one('th.truonghoc', string='Tên trường')
    lop = fields.Char('Lớp')
    email = fields.Char('Email')
    pas = fields.Char('Pass')
    sdt = fields.Integer('Số điện thoại')
    thoigiansudung = fields.One2many('th.thoigiansudung', inverse_name='giaovien', string='Thời gian sử dụng')