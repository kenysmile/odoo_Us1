# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions

class Uyquyen(models.Model):
    _name = 'th.uyquyen'

    giaovien = fields.Many2many('th.giaovien', string='Giáo viên')
    date_start = fields.Date('Date_start')
    date_expire = fields.Date('Date_expire')
    giaoan = fields.Many2many('th.giaoan', string='Giáo án')
    thoigian_ids = fields.One2many('th.thoigiansudung', 'uyquyen_id', string='Code')

    @api.model
    def create(self, vals):
        list_giaovien = []
        for giaovien_ids in vals['giaovien'][0][2]:
            for giaoan_ids in vals['giaoan'][0][2]:
                list_giaovien.append([0,0,{'giaovien': giaovien_ids, 'date_start': vals['date_start'], 'date_expire': vals['date_expire'], 'giaoan': giaoan_ids}])
        vals['thoigian_ids'] = list_giaovien
        return super(Uyquyen, self).create(vals)

    @api.multi
    def write(self, vals):
        list_giaoan = []
        # if date start exited in vals.keys()
        if 'date_start' in vals.keys():
            for thoigian_id in self.thoigian_ids:
                thoigian_id.date_start = vals['date_start']
        # check date expire exited in vals.keys()
        if 'date_expire' in vals.keys():
            for thoigian_id in self.thoigian_ids:
                thoigian_id.date_expire = vals['date_expire']
        # check giaoan exited in vals.keys()
        if 'giaoan' in vals.keys():
            for giaoan_id in self.giaoan:
                list_giaoan.append(giaoan_id.id)
                for edit_giaoan in vals['giaoan'][0][2]:
                    if edit_giaoan not in list_giaoan:
                        if 'giaovien' in vals.keys():
                            for giaovien_id in vals['giaovien'][0][2]:
                                self.env['th.thoigiansudung'].create({'giaovien': giaovien_id, 'date_start': vals['date_start'], 'date_expire': vals['date_expire'], 'giaoan': edit_giaoan,
                                                                      'uyquyen_id': self.id})
                # for edit_giaoan in vals['giaoan'][0][2]:
                #     # check value in list_new with list_before
                #     if edit_giaoan not in list_giaoan:
                #         if 'giaovien' in vals.keys():
                #             for giaovien_id in vals['giaovien'][0][2]:
                #                 self.env['th.thoigiansudung'].create(
                #                     {'giaovien': giaovien_id, 'date_start': vals['date_start'],
                #                      'date_expire': vals['date_expire'], 'giaoan': edit_giaoan,
                #                      'uyquyen_id': self.id})


        return super(Uyquyen, self).write(vals)