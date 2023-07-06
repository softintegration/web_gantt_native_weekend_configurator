# -*- coding: utf-8 -*- 

import datetime

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from odoo.tools import float_compare, float_round, float_is_zero
from odoo.tools import format_datetime


class GanttWeekDay(models.Model):
    _name = 'gantt.weekday'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code',required=True)
