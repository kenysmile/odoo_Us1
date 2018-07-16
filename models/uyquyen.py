# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions

class Uyquyen(models.Model):
    _name = 'th.uyquyen'

    giaovien_ids = fields.Many2many('th.giaovien', string='Ủy quyền')
    date_start = fields.Date('Date_start')
    date_expire = fields.Date('Date_expire')
    giaoan_ids = fields.Many2many('th.giaoan', string='Giáo án')

    @api.model
    def create(self, vals):
        for giaovien_ids in vals['giaovien_ids'][0][2]:
            for giaoan_ids in vals['giaoan_ids'][0][2]:
                self.env['th.thoigiansudung'].create({'giaovien': giaovien_ids, 'date_start': vals['date_start'], 'date_expire': vals['date_expire'], 'giaoan': giaoan_ids})
        return super(Uyquyen, self).create(vals)