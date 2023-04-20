# -*- coding: utf-8 -*-
# Part of IT IS AG. See LICENSE file for full copyright and licensing details.

from . import models

from odoo.api import Environment, SUPERUSER_ID

def post_init_hook(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})
    #Reset sequence on sales order line
    # sale = env['sale.order'].search([])
    # sale.reset_sequence()

    #Update Context
    context_pool = env['res.context']
    context = """{'default_delivery_date': est_delivery_date}"""
    record_id = context_pool.search([('model_name', '=', 'sale.order'), ('field_name', '=', 'order_line')], limit=1)
    context_line_pool = env['res.context.line']
    if record_id:
        line_id = context_line_pool.search([
            ('module_name', '=', 'itis_lines_delivery_date'), ('context_record_id', '=', record_id.id)
        ])
        if line_id:
            line_id.write({'context': context})
        else:
            context_line_pool.create({
                'module_name': 'itis_lines_delivery_date',
                'context': context,
                'context_record_id': record_id.id or False,
        })
    else:
        model_id = env['ir.model'].search([('model', '=', 'sale.order')], limit=1)
        field_id = env['ir.model.fields'].search([('name', '=', 'order_line'), ('model_id', '=', model_id.id)], limit=1)
        context_record_id = context_pool.create({'name': 'Order Line Context',
                             'model_id': model_id.id,
                             'field_id': field_id.id,})
        context_line_pool.create({
            'module_name': 'itis_lines_delivery_date',
            'context': context,
            'context_record_id': context_record_id.id or False,
        })


def uninstall_hook(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})
    context_line_ids = env['res.context.line'].search([('module_name', '=', 'itis_lines_delivery_date')])
    if context_line_ids:
        context_record_ids = [record_id.context_record_id for record_id in context_line_ids]
        context_line_ids.unlink()
        for context_rec in context_record_ids:
            context_rec.update_context()
