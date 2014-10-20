# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time

from osv import orm, fields, osv


class hr_attendance_bymonth(orm.Model):

    _inherit = 'anddes.budget'

    def print_report(self, cr, uid, ids, context=None):
        data = {'form': {'values': ids[0]}}
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'consolidate_budget',
            'datas': data,
        }

hr_attendance_bymonth()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
