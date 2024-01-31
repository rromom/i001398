# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class ProjectProject(models.Model):
    _inherit = 'project.project'

    # @api.depends('customer_approval')
    def _compute_project_progress(self):
        '''
        Calcula el progreso de la ultima actualización del proyecto
        '''
        for record in self:
            record.project_progress = record.last_update_id.progress
    
    def _compute_sale_order_number(self):
        for record in self:
            record.amount_sale_orders = 0
            if record.task_ids:
                record.amount_sale_orders = sum(record.task_ids.mapped('sale_order_id').mapped('amount_untaxed'))

    localization = fields.Char(
        string='Localización',
        help='Localización de donde se elaborara el proyecto(Campo Informativo).',
    )

    customer_approval = fields.Selection(
        [('yes','Si'), ('no', 'No')],
        string='Aprobación',
        help='Aprobación de la cotización por parte del cliente(Campo Informativo).',
        default='no'
    )

    project_progress = fields.Integer(
        compute='_compute_project_progress',
        string='Progreso',
        help='Ultimo progreso del proyecto'
    )

    sale_order_number = fields.Many2one(
        'sale.order',
        string='Numero de orden asociada',
        compute='_compute_sale_order_number'
    )

    amount_sale_orders = fields.Float(
        string='Monto',
        help='Monto total de las ordenes de venta',
        compute='_compute_sale_order_number'
    )

    