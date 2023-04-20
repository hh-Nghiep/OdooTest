# -*- coding: utf-8 -*-
# Part of IT IS AG. See LICENSE file for full copyright and licensing details.

from odoo.tests.common import TransactionCase, tagged
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo.addons.sale.tests.test_sale_order import TestSaleOrder


@tagged('-standard', 'itis_lines_delivery_date')
class TestDeliveryDate(TestSaleOrder):

    @classmethod
    def setUpClass(self):
        super(TestDeliveryDate, self).setUpClass()

        SaleOrder = self.env['sale.order'].with_context(tracking_disable=True)

        self.test_order = SaleOrder.sudo(self.user_employee).create({
            'partner_id': self.partner_customer_usd.id,
            'partner_invoice_id': self.partner_customer_usd.id,
            'partner_shipping_id': self.partner_customer_usd.id,
            'est_delivery_date': datetime.today().date(),
            'pricelist_id': self.pricelist_usd.id,
        })

        SaleOrderLine = self.env['sale.order.line']
        self.test_order_line = SaleOrderLine.sudo(self.user_employee).create({
            'name': self.product_order.name,
            'product_id': self.product_order.id,
            'product_uom_qty': 2,
            'product_uom': self.product_order.uom_id.id,
            'price_unit': self.product_order.list_price,
            'order_id': self.test_order.id,
            'tax_id': False,
        })
        self.test_order_line_2 = self.env['sale.order.line'].create({
            'name': self.product_order.name,
            'product_id': self.product_order.id,
            'product_uom_qty': 3,
            'product_uom': self.product_order.uom_id.id,
            'price_unit': self.product_order.list_price,
            'order_id': self.test_order.id,
            'tax_id': False,
        })

        self.assertTrue(self.test_order, 'Sale Order not created')

    def test_delivery_date_on_line(self):
        """Test for check delivery date on line"""

        self.assertEqual(self.test_order.est_delivery_date, self.test_order_line.delivery_date, "Delivery date on line: Delivery date should be same")

        today = datetime.today().date()
        new_delivery_date = today + timedelta(days=5)
        self.test_order.sudo().write({'delivery_date': new_delivery_date})
        self.test_order.sudo().set_delivery_date_line(new_delivery_date)
        self.assertEqual(new_delivery_date, self.test_order_line_2.delivery_date, "Delivery date on line: Delivery date should be same")
