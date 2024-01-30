# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class ProjectProject(models.Model):
    _inherit = 'project.project'

    @api.depends('sale_line_id')
    def _compute_order_id(self):
        return False

    localization = fields.Char(
        string='Localización',
        help='Ingrese la localización del proyecto',
    )

    order_id = fields.Many2one(
        'sale.order',
        string='Orden de Venta ',
        help='Numero de la orden de venta relacionado al proyecto',
        compute='_compute_order_id'
    )