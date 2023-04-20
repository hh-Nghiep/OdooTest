# -*- coding: utf-8 -*-
# Part of IT IS AG. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    est_delivery_date = fields.Date(string='Delivery Date')

    def set_delivery_date_line(self, delivery_date):
        if delivery_date:
            for line in self.order_line:
                line.delivery_date = delivery_date
        return True


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    delivery_date = fields.Date(string='Delivery Date')

    @api.model
    def create(self, values):
        sale_line = super(SaleOrderLine, self).create(values)
        if sale_line.order_id and sale_line.order_id.est_delivery_date and not sale_line.delivery_date:
            sale_line.delivery_date = sale_line.order_id.est_delivery_date
        return sale_line
