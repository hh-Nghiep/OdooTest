# -*- coding: utf-8 -*-
# Part of IT IS AG. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    planned_date = fields.Date(compute="_compute_date_planned", string='Scheduled Date', store=True)

    @api.depends('date_planned')
    def _compute_date_planned(self):
        for line in self:
            line.planned_date = False
            if line.date_planned:
                line.planned_date = line.date_planned.date()
