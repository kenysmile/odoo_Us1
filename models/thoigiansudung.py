# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions, api, exceptions

class Thoigiansudung(models.Model):
    _name = 'th.thoigiansudung'

    giaovien = fields.Many2one('th.giaovien',string='Giáo viên')
    date_start = fields.Date('Date_start')
    date_expire = fields.Date('Date_expire')
    giaoan = fields.Many2one('th.giaoan', string='Giáo án')
    uyquyen_id = fields.Many2one('th.uyquyen', string='Code')

    # @api.multi
    # def write(self, vals):
    #     a = self.env['th.giaovien'].browse([1, 2])
    #     self.env['th.truonghoc'].browse([1]).giaovien_ids=a
    #     print(a)
    #     return super(Thoigiansudung, self).write(vals)