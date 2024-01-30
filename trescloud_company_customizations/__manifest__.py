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
    'author': 'Trescloud',
    'maintainer': 'TRESCLOUD CIA. LTDA.',
    'website': 'http://www.trescloud.com',
    'license': 'OEEL-1',
    'depends': [
        'project',
        'sale_timesheet',
    ],
    'data': [
        'data/project_data.xml',
        'views/project_views.xml',
        
    ],
    'assets': {
        'web.assets_backend': [

        ],
    },
}