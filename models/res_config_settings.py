# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    weekend_list_days = fields.Many2many(related='company_id.weekend_list_days', string='Weekend days',
                                         readonly=False,
                                         help='Days selected here will be considered as weekend in gantt view')
