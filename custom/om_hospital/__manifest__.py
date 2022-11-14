
{
    'name' : 'Hospital Management',
    'version' : '1.0',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Hospital',
    'author': 'Devloper',

    'website': 'https://www.odoodev.tech',
    'license':'LGPL-3',
    'depends' : ['mail','product'],
    'data': [
        'security/ir.model.access.csv', 
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'data/sequence_data.xml',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/female_patient_view.xml',
        'views/patient_tag_view.xml',
        'views/odoo_playground_view.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    
}
