# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class ProjectProject(models.Model):
    _inherit = 'project.project'
    
    def _compute_first_order_and_sum_amount_orders(self):
        '''
        Método que calcula la primera orden de venta confirmada y la suma de todas las ordenes de venta asociadas a las tareas  del proyecto 
        amount_sale_orders: Almacena la suma total de todo el 
        '''
        for record in self:
            record.sale_order_task_id = False 
            record.amount_sale_orders = 0.0
            if record.task_ids:
                sales_orders = record.task_ids.mapped('sale_order_id').filtered(lambda order: order.state in ['sale', 'done'] )
                if sales_orders:
                    record.amount_sale_orders = sum(sales_orders.mapped('amount_untaxed'))
                    first_sale_order_id = min(sales_orders.mapped('id'))
                    record.sale_order_task_id = sales_orders.browse(first_sale_order_id)

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
        related='last_update_id.progress',
        string='Progreso del Proyecto',
        help='Almacena el ultimo avance del proyecto registrado en las actualizaciones del proyecto'
    )

    sale_order_task_id = fields.Many2one(
        'sale.order',
        string='Numero de orden asociada',
        help='Almacena la primera orden de venta confirmada asociada al proyecto',
        compute='_compute_first_order_and_sum_amount_orders',
    )

    amount_sale_orders = fields.Float(
        string='Monto',
        help='Monto total de las ordenes de venta confirmadas',
        compute='_compute_first_order_and_sum_amount_orders',
    )

    