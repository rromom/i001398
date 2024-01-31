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
    
    def _compute_amount_sale_order(self):
        '''
        Calcula la sumatoria de las bases imponibles de todas las ordenes de ventas confirmadas asociadas
        y la primera orden de venta que se confirmo y que se creo el proyecto
        '''
        for record in self:
            record.sale_order_task_id = False 
            record.amount_sale_orders = 0.0
            if record.task_ids:
                sales_orders = record.task_ids.mapped('sale_order_id').filtered(lambda order: order.state in ['sale', 'done'] )
                if sales_orders:
                    record.amount_sale_orders = sum(sales_orders.mapped('amount_untaxed'))
                    record.sale_order_task_id = self.env['sale.order'].browse(min(sales_orders.mapped('id')))

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

    sale_order_task_id = fields.Many2one(
        'sale.order',
        string='Numero de orden asociada',
        help='Se selecciona la primera orden confirmada',
        compute='_compute_amount_sale_order',
    )

    amount_sale_orders = fields.Float(
        string='Monto',
        help='Monto total de las ordenes de venta confirmadas',
        compute='_compute_amount_sale_order',
    )

    