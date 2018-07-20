# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions

class Truonghoc(models.Model):
    _name = 'th.truonghoc'

    name = fields.Char('Tên trường')
    diachi = fields.Char('Địa chỉ')
    tinhtrang = fields.Selection([('1', 'Đang hoạt động'), ('2', 'Chưa hoạt động')], 'Tình trạng')
    giaovien_ids = fields.One2many('th.giaovien', 'truong', string='Giáo viên')

    # @api.multi
    # def write(self, vals):
    #     a = self.env['th.thoigiansudung'].browse([8, 11, 13])
    #     self.env['th.uyquyen'].browse([11]).thoigian_ids=a
    #     return super(Truonghoc, self).write(vals)