{
    'name': 'design creative custom',
    'description': 'design creative customization',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'category': 'custom',
    'author': 'kashif',
    'website': '',
    'depends': [
        'base',
        'hr',
        'account'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_emplouee_custom.xml',
        'views/quotation_report.xml',
        'views/product_custom_view.xml',
        'views/payslip_report_inherit.xml',
        'report/logs_report.xml',
        'report/sick_leave.xml',
        'wizard/emp_sick_wiz.xml',
        # 'report/attendance_summery.xml',
        # 'wizard/attend_summery_wiz.xml',
        'report/daily_attendence.xml',
        'wizard/payslip_report.xml',
        'wizard/daily_attend_wiz.xml',
        'views/hr_contract_custom.xml',
        'wizard/emp_log_wixz.xml',
        'wizard/emp_info_wixz.xml',
        'report/emp_info.xml',
        'report/emp_wage_listing.xml',
        'wizard/emp_wage_wixz.xml'


    ],
    'installable': True,
}
