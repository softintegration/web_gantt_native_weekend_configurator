# -*- coding: utf-8 -*-

from odoo import models, fields


class res_company(models.Model):
    _inherit = "res.company"

    weekend_list_days = fields.Many2many('gantt.weekday', string='Weekend days',
                                         help='Days selected here will be considered as weekend in gantt view')