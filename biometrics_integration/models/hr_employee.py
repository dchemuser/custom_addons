from openerp import models, fields, api, tools, _
import datetime
from datetime import timedelta

class hr_employee_extension(models.Model):
	_inherit = 'hr.employee'
	
	emp_code = fields.Char(string="Employee Code")
	
	@api.multi
	def emp_attendance_fetcher(self, attendance_list, att_date, in_machine, out_machine):
		hr_attendance =  self.env["hr.attendance"]
		
		todays_attendance = [item for item in attendance_list if (item[2].date() == att_date)]
		
		employees = []
		employee_att = {}
		
		for record in todays_attendance:
			if record[0] not in employees:
				employees.append(record[0])
				employee_att[record[0]] = []
			employee_att[record[0]].append((record[1],record[2]))
		
		for key, value in employee_att.iteritems():
			employee = self.search([('emp_code','=',key)])
			if len(employee):
				login_list = [item for item in value if (item[0] == in_machine)]
				logout_list = [item for item in value if (item[0] == out_machine)]
				if logout_list and login_list:
					login_time = (login_list[0][1] - timedelta(hours=5,minutes=30)).strftime("%Y-%m-%d %H:%M:%S")
					hr_attendance.create({'name':login_time,'action':'sign_in','employee_id':employee[0].id})
					logout_time = (logout_list[-1][1] - timedelta(hours=5,minutes=30)).strftime("%Y-%m-%d %H:%M:%S")
					hr_attendance.create({'name':logout_time,'action':'sign_out','employee_id':employee[0].id})
					# print employee.name,": Login = ",login_time," --- Logout = ",logout_time