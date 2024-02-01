# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Trescloud Company Customizations',
    'version': '1.0',
    'category': '/',
    'summary': 'Customizations',
    'description': '''
        Módulo de Personalizaciones especificadas por el cliente.

            Autores: Ricardo Romo
    ''',
    'author': 'TRESCLOUD CIA. LTDA.',
    'maintainer': 'TRESCLOUD CIA. LTDA.',
    'website': 'https://www.trescloud.com',
    'license': 'OEEL-1',
    'depends': [
        'project',
        'sale_timesheet',
        'sale',

        # Se agregan estos módulos para evitar errores en la reestructuración de la vista lista de los proyectos
        'sale_project',
        'hr_timesheet',

    ],
    'data': [
        'views/project_views.xml',
        'data/project_data.xml',
        
    ],
}