# -*- coding: utf-8 -*- 


{
    'name': 'Gantt native weekend configurator',
    'author': 'Soft-integration',
    'application': True,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1',
    'category': 'Project',
    'demo': [],
    'depends': ['web_gantt_native'],
    'data': [
        'security/ir.model.access.csv',
        'data/web_gantt_native_weekend_configurator_data.xml',
        'views/res_config_settings_views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'web_gantt_native_weekend_configurator/static/src/js/gantt_timeline_head.js',
            'web_gantt_native_weekend_configurator/static/src/js/gantt_timeline_header.js',
        ],

    },
    'license': 'LGPL-3',
}
