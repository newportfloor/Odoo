{
    'name': 'CRM Lead Messaging Extension',
    'version': '1.0',
    'summary': 'Extend CRM for SMS, WhatsApp, Album Sharing and Link Tracking',
    'depends': ['crm'],
    'data': [
        'views/crm_lead_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}
