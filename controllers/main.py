# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request


class GanttNativeConfiguratorController(http.Controller):
    @http.route(['/web_gantt_native_weekend_configurator/configure'], type='json', auth="user", methods=['POST'])
    def configure(self,varname, **kw):
        if varname == 'weekend':
            selected_weekend_days  = request.env.company.weekend_list_days
            return [int(weekendday.code) for weekendday in selected_weekend_days] or [6,7]