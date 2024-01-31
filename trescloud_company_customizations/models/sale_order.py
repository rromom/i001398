# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('analytic_account_id')
    def change_analytic_distribution_in_sale_order_lines(self):
        '''
        Método que cambia la distribución analítica por una distribución del 100% para la cuenta analítica seleccionada 
        en otra información
        '''
        self.ensure_one()
        for line in self.order_line:
            line.analytic_distribution = {self.analytic_account_id.id: 100}
        return False
    