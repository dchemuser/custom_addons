from openerp import models, fields, api, tools, _
import datetime
import time
from datetime import timedelta
from zklib import zklib
from openerp.exceptions import UserError, Warning

class biometric_machine(models.Model):
	_name= 'biometric.machine'
	
	name = fields.Char(string="Machine Name")
	location = fields.Char(string="Location")
	ip_address = fields.Char(string="Machine IP")
	port = fields.Integer(string="Machine Port")
	in_machine = fields.Integer(string="Entry Machine Code")
	out_machine = fields.Integer(string="Exit Machine Code")
	
	@api.model
	def download_schedular(self):
		###--- Uncomment on final build ---###
		# machine = self.search([('ip_address','not in',['',False])])
		# if machine:
		# 	machine.download_attendance()
		return True
	
	@api.multi
	def download_attendance(self):
		date_yesterday = datetime.datetime.today().date() - timedelta(days=+1)
		# date_yesterday = datetime.datetime.strptime('2016-02-02','%Y-%m-%d').date()
		if self.ip_address and self.port:
			in_machine = self.in_machine or 0
			out_machine = self.out_machine or 0
			# Uncomment after completion
			zk = zklib.ZKLib(self.ip_address, int(self.port))
			res = zk.connect()
			
			
			# res = True # To be removed
			if res == True:
				zk.enableDevice()
				zk.disableDevice()
				attendance = zk.getAttendance()
				time.sleep(2)
				# attendance = [
				# 	('10060', 101, datetime.datetime(2016, 2, 1, 16, 6, 13)), ('10060', 0, datetime.datetime(2016, 2, 1, 16, 14, 45)), ('10077', 101, datetime.datetime(2016, 2, 1, 16, 18, 11)), ('10077', 0, datetime.datetime(2016, 2, 1, 16, 20, 39)), ('10067', 101, datetime.datetime(2016, 2, 1, 16, 32, 27)), ('10067', 0, datetime.datetime(2016, 2, 1, 16, 32, 34)), ('10005', 101, datetime.datetime(2016, 2, 1, 16, 33, 10)), ('10015', 101, datetime.datetime(2016, 2, 1, 16, 34, 1)), ('10090', 101, datetime.datetime(2016, 2, 1, 16, 35, 26)), ('10026', 101, datetime.datetime(2016, 2, 1, 16, 36, 21)), ('10026', 0, datetime.datetime(2016, 2, 1, 16, 38, 38)), ('10090', 0, datetime.datetime(2016, 2, 1, 16, 40, 36)), ('10003', 101, datetime.datetime(2016, 2, 1, 16, 47, 52)), ('10005', 0, datetime.datetime(2016, 2, 1, 16, 49, 31)), ('10094', 101, datetime.datetime(2016, 2, 1, 16, 55, 45)), ('10096', 101, datetime.datetime(2016, 2, 1, 16, 56, 5)), ('10096', 0, datetime.datetime(2016, 2, 1, 16, 58, 25)), ('10085', 101, datetime.datetime(2016, 2, 1, 17, 1, 34)), ('10085', 101, datetime.datetime(2016, 2, 1, 17, 1, 35)), ('10003', 0, datetime.datetime(2016, 2, 1, 17, 7, 20)), ('10085', 0, datetime.datetime(2016, 2, 1, 17, 9, 54)), ('10060', 0, datetime.datetime(2016, 2, 1, 17, 10, 56)), ('10090', 101, datetime.datetime(2016, 2, 1, 17, 11, 27)), ('10090', 0, datetime.datetime(2016, 2, 1, 17, 15, 22)), ('10060', 101, datetime.datetime(2016, 2, 1, 17, 34, 35)), ('10071', 101, datetime.datetime(2016, 2, 1, 17, 35, 42)), ('10015', 101, datetime.datetime(2016, 2, 1, 17, 35, 54)), ('10039', 101, datetime.datetime(2016, 2, 1, 17, 38, 25)), ('10077', 101, datetime.datetime(2016, 2, 1, 17, 39, 9)), ('10026', 101, datetime.datetime(2016, 2, 1, 17, 41, 24)), ('10077', 0, datetime.datetime(2016, 2, 1, 17, 42, 32)), ('10026', 0, datetime.datetime(2016, 2, 1, 17, 44, 59)), ('10060', 0, datetime.datetime(2016, 2, 1, 17, 47, 23)), ('10060', 0, datetime.datetime(2016, 2, 1, 18, 1, 9)), ('10005', 101, datetime.datetime(2016, 2, 1, 18, 1, 47)), ('10039', 0, datetime.datetime(2016, 2, 1, 18, 3, 11)), ('10026', 101, datetime.datetime(2016, 2, 1, 18, 5, 36)), ('10026', 0, datetime.datetime(2016, 2, 1, 18, 5, 55)), ('10090', 0, datetime.datetime(2016, 2, 1, 18, 6, 14)), ('10094', 101, datetime.datetime(2016, 2, 1, 18, 6, 15)), ('10094', 0, datetime.datetime(2016, 2, 1, 18, 6, 27)), ('10039', 0, datetime.datetime(2016, 2, 1, 18, 6, 45)), ('10091', 0, datetime.datetime(2016, 2, 1, 18, 7, 16)), ('10093', 0, datetime.datetime(2016, 2, 1, 18, 7, 53)), ('10039', 0, datetime.datetime(2016, 2, 1, 18, 8, 49)), ('10096', 101, datetime.datetime(2016, 2, 1, 18, 12, 2)), ('10085', 101, datetime.datetime(2016, 2, 1, 18, 12, 12)), ('10003', 101, datetime.datetime(2016, 2, 1, 18, 12, 41)), ('10096', 0, datetime.datetime(2016, 2, 1, 18, 15, 6)), ('10085', 0, datetime.datetime(2016, 2, 1, 18, 15, 31)), ('10005', 0, datetime.datetime(2016, 2, 1, 18, 16, 53)), ('10003', 0, datetime.datetime(2016, 2, 1, 18, 23, 36)), ('10077', 0, datetime.datetime(2016, 2, 1, 18, 36, 6)), ('10085', 101, datetime.datetime(2016, 2, 1, 18, 43, 3)), ('10085', 101, datetime.datetime(2016, 2, 1, 18, 43, 4)), ('10015', 101, datetime.datetime(2016, 2, 1, 18, 43, 48)), ('10015', 0, datetime.datetime(2016, 2, 1, 18, 56, 30)), ('10096', 101, datetime.datetime(2016, 2, 1, 20, 0, 46)), ('10096', 0, datetime.datetime(2016, 2, 1, 20, 6, 7)), ('10096', 101, datetime.datetime(2016, 2, 1, 20, 6, 51)), ('10096', 0, datetime.datetime(2016, 2, 1, 20, 7)), ('10015', 101, datetime.datetime(2016, 2, 1, 20, 14, 44)), ('10015', 0, datetime.datetime(2016, 2, 1, 20, 23, 31)), ('10039', 101, datetime.datetime(2016, 2, 1, 20, 29, 16)), ('10039', 0, datetime.datetime(2016, 2, 1, 20, 32, 9)), ('10015', 101, datetime.datetime(2016, 2, 1, 20, 47, 7)), ('10015', 0, datetime.datetime(2016, 2, 1, 20, 47, 37)), ('10003', 101, datetime.datetime(2016, 2, 1, 20, 59, 18)), ('10039', 101, datetime.datetime(2016, 2, 1, 21, 13, 18)), ('10039', 0, datetime.datetime(2016, 2, 1, 21, 35, 22)), ('10015', 101, datetime.datetime(2016, 2, 1, 21, 41, 48)), ('10039', 101, datetime.datetime(2016, 2, 1, 21, 44, 44)), ('10039', 0, datetime.datetime(2016, 2, 1, 21, 44, 52)), ('10060', 0, datetime.datetime(2016, 2, 2, 8, 45, 42)), ('10091', 0, datetime.datetime(2016, 2, 2, 9, 0)), ('10067', 0, datetime.datetime(2016, 2, 2, 9, 1, 35)), ('10026', 0, datetime.datetime(2016, 2, 2, 9, 12, 59)), ('10096', 0, datetime.datetime(2016, 2, 2, 9, 31, 54)), ('10094', 0, datetime.datetime(2016, 2, 2, 9, 34, 48)), ('10093', 0, datetime.datetime(2016, 2, 2, 9, 51, 56)), ('10071', 0, datetime.datetime(2016, 2, 2, 9, 52, 45)), ('10077', 0, datetime.datetime(2016, 2, 2, 9, 57, 54)), ('10060', 101, datetime.datetime(2016, 2, 2, 10, 33, 37)), ('10060', 0, datetime.datetime(2016, 2, 2, 10, 38, 45)), ('10094', 101, datetime.datetime(2016, 2, 2, 10, 41, 22)), ('10094', 0, datetime.datetime(2016, 2, 2, 10, 43, 56)), ('10090', 101, datetime.datetime(2016, 2, 2, 10, 47, 25)), ('10090', 0, datetime.datetime(2016, 2, 2, 10, 51, 16)), ('10005', 0, datetime.datetime(2016, 2, 2, 10, 52, 41)), ('10091', 101, datetime.datetime(2016, 2, 2, 10, 55, 12)), ('10091', 0, datetime.datetime(2016, 2, 2, 10, 57, 26)), ('10026', 101, datetime.datetime(2016, 2, 2, 11, 23, 57)), ('10026', 0, datetime.datetime(2016, 2, 2, 11, 24, 40)), ('10060', 101, datetime.datetime(2016, 2, 2, 11, 30, 47)), ('10060', 0, datetime.datetime(2016, 2, 2, 11, 35, 49)), ('10060', 101, datetime.datetime(2016, 2, 2, 11, 38, 11)), ('10094', 101, datetime.datetime(2016, 2, 2, 11, 38, 31)), ('10094', 0, datetime.datetime(2016, 2, 2, 11, 42, 38)), ('10093', 101, datetime.datetime(2016, 2, 2, 11, 45, 42)), ('10077', 0, datetime.datetime(2016, 2, 2, 11, 49, 17)), ('10060', 0, datetime.datetime(2016, 2, 2, 11, 55, 35)), ('10026', 101, datetime.datetime(2016, 2, 2, 11, 56, 8)), ('10060', 101, datetime.datetime(2016, 2, 2, 11, 57, 4)), ('10026', 0, datetime.datetime(2016, 2, 2, 12, 0, 39)), ('10090', 0, datetime.datetime(2016, 2, 2, 12, 2, 13)), ('10071', 0, datetime.datetime(2016, 2, 2, 12, 6, 44)), ('10026', 101, datetime.datetime(2016, 2, 2, 12, 6, 58)), ('10093', 101, datetime.datetime(2016, 2, 2, 12, 8, 13)), ('10091', 101, datetime.datetime(2016, 2, 2, 12, 8, 49)), ('10026', 101, datetime.datetime(2016, 2, 2, 12, 9, 12)), ('10091', 0, datetime.datetime(2016, 2, 2, 12, 10, 53)), ('10060', 101, datetime.datetime(2016, 2, 2, 12, 11, 46)), ('10060', 101, datetime.datetime(2016, 2, 2, 12, 12, 23)), ('10060', 101, datetime.datetime(2016, 2, 2, 12, 13)), ('10060', 101, datetime.datetime(2016, 2, 2, 12, 17, 59)), ('10067', 101, datetime.datetime(2016, 2, 2, 12, 24, 6)), ('10096', 101, datetime.datetime(2016, 2, 2, 12, 24, 47)), ('10071', 101, datetime.datetime(2016, 2, 2, 12, 25, 22)), ('10094', 101, datetime.datetime(2016, 2, 2, 12, 29, 51)), ('10096', 0, datetime.datetime(2016, 2, 2, 12, 30, 10)), ('10060', 101, datetime.datetime(2016, 2, 2, 12, 32, 7)), ('10094', 0, datetime.datetime(2016, 2, 2, 12, 32, 30)), ('10060', 101, datetime.datetime(2016, 2, 2, 12, 38, 48)), ('10060', 101, datetime.datetime(2016, 2, 2, 12, 39, 27)), ('10060', 101, datetime.datetime(2016, 2, 2, 12, 46, 14)), ('10060', 101, datetime.datetime(2016, 2, 2, 12, 46, 32)), ('10060', 101, datetime.datetime(2016, 2, 2, 12, 47, 35)), ('10060', 0, datetime.datetime(2016, 2, 2, 12, 48, 20)), ('10005', 0, datetime.datetime(2016, 2, 2, 12, 49, 35)), ('10096', 101, datetime.datetime(2016, 2, 2, 12, 52, 52)), ('10060', 101, datetime.datetime(2016, 2, 2, 12, 54, 5)), ('10067', 0, datetime.datetime(2016, 2, 2, 12, 55, 3)), ('10093', 101, datetime.datetime(2016, 2, 2, 12, 58, 12)), ('10060', 0, datetime.datetime(2016, 2, 2, 12, 58, 36)), ('10060', 101, datetime.datetime(2016, 2, 2, 12, 59, 17)), ('10060', 101, datetime.datetime(2016, 2, 2, 13, 0, 24)), ('10060', 101, datetime.datetime(2016, 2, 2, 13, 1, 13)), ('10060', 101, datetime.datetime(2016, 2, 2, 13, 2, 39)), ('10060', 0, datetime.datetime(2016, 2, 2, 13, 3, 18)), ('10093', 0, datetime.datetime(2016, 2, 2, 13, 3, 44)), ('10071', 0, datetime.datetime(2016, 2, 2, 13, 7, 11)), ('10060', 101, datetime.datetime(2016, 2, 2, 13, 10, 56)), ('10060', 0, datetime.datetime(2016, 2, 2, 13, 14, 35)), ('10060', 0, datetime.datetime(2016, 2, 2, 13, 17, 13)), ('10060', 101, datetime.datetime(2016, 2, 2, 13, 17, 38)), ('10039', 0, datetime.datetime(2016, 2, 2, 13, 18, 32)), ('10060', 0, datetime.datetime(2016, 2, 2, 13, 18, 58)), ('10060', 101, datetime.datetime(2016, 2, 2, 13, 20, 1)), ('10060', 0, datetime.datetime(2016, 2, 2, 13, 20, 29)), ('10090', 0, datetime.datetime(2016, 2, 2, 13, 21, 59)), ('10003', 0, datetime.datetime(2016, 2, 2, 13, 24, 18)), ('10060', 101, datetime.datetime(2016, 2, 2, 13, 26, 39)), ('10060', 101, datetime.datetime(2016, 2, 2, 13, 28, 43)), ('10015', 0, datetime.datetime(2016, 2, 2, 13, 33, 30)), ('10060', 101, datetime.datetime(2016, 2, 2, 13, 34, 46)), ('10071', 101, datetime.datetime(2016, 2, 2, 13, 37, 1)), ('10060', 0, datetime.datetime(2016, 2, 2, 13, 37, 40)), ('10060', 101, datetime.datetime(2016, 2, 2, 13, 38, 8)), ('10060', 101, datetime.datetime(2016, 2, 2, 13, 38, 49)), ('10075', 0, datetime.datetime(2016, 2, 2, 13, 40, 24)), ('10060', 101, datetime.datetime(2016, 2, 2, 13, 42, 55)), ('10067', 0, datetime.datetime(2016, 2, 2, 13, 44, 11)), ('10071', 0, datetime.datetime(2016, 2, 2, 13, 52, 6)), ('10067', 101, datetime.datetime(2016, 2, 2, 13, 54, 11)), ('10085', 101, datetime.datetime(2016, 2, 2, 13, 57, 26)), ('10060', 101, datetime.datetime(2016, 2, 2, 13, 58, 59)), ('10026', 0, datetime.datetime(2016, 2, 2, 13, 59, 9)), ('10085', 0, datetime.datetime(2016, 2, 2, 14, 1, 7)), ('10094', 101, datetime.datetime(2016, 2, 2, 14, 4, 39)), ('10090', 0, datetime.datetime(2016, 2, 2, 14, 6)), ('10091', 101, datetime.datetime(2016, 2, 2, 14, 7, 6)), ('10094', 0, datetime.datetime(2016, 2, 2, 14, 8, 4)), ('10091', 0, datetime.datetime(2016, 2, 2, 14, 9, 35)), ('10060', 0, datetime.datetime(2016, 2, 2, 14, 13, 31)), ('10060', 101, datetime.datetime(2016, 2, 2, 14, 15, 50)), ('10060', 0, datetime.datetime(2016, 2, 2, 14, 17, 30)), ('10096', 101, datetime.datetime(2016, 2, 2, 14, 30, 15)), ('10026', 101, datetime.datetime(2016, 2, 2, 14, 31, 33)), ('10096', 0, datetime.datetime(2016, 2, 2, 14, 32, 59)), ('10026', 0, datetime.datetime(2016, 2, 2, 14, 33, 12)), ('10060', 101, datetime.datetime(2016, 2, 2, 14, 33, 57)), ('10060', 0, datetime.datetime(2016, 2, 2, 14, 34, 35)), ('10090', 101, datetime.datetime(2016, 2, 2, 14, 37, 37)), ('10015', 101, datetime.datetime(2016, 2, 2, 14, 39, 28)), ('10090', 0, datetime.datetime(2016, 2, 2, 14, 43)), ('10060', 101, datetime.datetime(2016, 2, 2, 14, 43, 23)), ('10060', 0, datetime.datetime(2016, 2, 2, 14, 48, 18)), ('10067', 101, datetime.datetime(2016, 2, 2, 14, 52, 28)), ('10093', 101, datetime.datetime(2016, 2, 2, 14, 52, 44)), ('10060', 101, datetime.datetime(2016, 2, 2, 14, 54, 28)), ('10093', 0, datetime.datetime(2016, 2, 2, 14, 55, 22)), ('10060', 0, datetime.datetime(2016, 2, 2, 14, 55, 44)), ('10075', 101, datetime.datetime(2016, 2, 2, 14, 58, 8)), ('10026', 0, datetime.datetime(2016, 2, 2, 15, 7, 6)), ('10005', 0, datetime.datetime(2016, 2, 2, 15, 10, 29)), ('10015', 0, datetime.datetime(2016, 2, 2, 15, 11, 32)), ('10075', 0, datetime.datetime(2016, 2, 2, 15, 18, 13)), ('10003', 101, datetime.datetime(2016, 2, 2, 15, 18, 14)), ('10094', 101, datetime.datetime(2016, 2, 2, 15, 18, 43)), ('10003', 0, datetime.datetime(2016, 2, 2, 15, 20, 15)), ('10094', 0, datetime.datetime(2016, 2, 2, 15, 22)), ('10060', 101, datetime.datetime(2016, 2, 2, 15, 30, 50)), ('10096', 101, datetime.datetime(2016, 2, 2, 15, 31, 58)), ('10085', 101, datetime.datetime(2016, 2, 2, 15, 32, 54)), ('10096', 0, datetime.datetime(2016, 2, 2, 15, 33, 45)), ('10085', 0, datetime.datetime(2016, 2, 2, 15, 35, 38)), ('10015', 101, datetime.datetime(2016, 2, 2, 15, 37, 33)), ('10090', 101, datetime.datetime(2016, 2, 2, 15, 39, 6)), ('10077', 101, datetime.datetime(2016, 2, 2, 15, 40, 5)), ('10067', 101, datetime.datetime(2016, 2, 2, 15, 41, 11)), ('10090', 0, datetime.datetime(2016, 2, 2, 15, 42, 43)), ('10026', 0, datetime.datetime(2016, 2, 2, 15, 44, 23)), ('10039', 101, datetime.datetime(2016, 2, 2, 15, 53, 22)), ('10015', 0, datetime.datetime(2016, 2, 2, 15, 53, 59)), ('10077', 0, datetime.datetime(2016, 2, 2, 15, 55, 24)), ('10039', 0, datetime.datetime(2016, 2, 2, 15, 56, 26)), ('10060', 0, datetime.datetime(2016, 2, 2, 16, 4)), ('10093', 101, datetime.datetime(2016, 2, 2, 16, 6, 40)), ('10060', 101, datetime.datetime(2016, 2, 2, 16, 7, 19)), ('10093', 0, datetime.datetime(2016, 2, 2, 16, 9, 25)), ('10026', 101, datetime.datetime(2016, 2, 2, 16, 9, 33)), ('10026', 0, datetime.datetime(2016, 2, 2, 16, 12, 22)), ('10093', 101, datetime.datetime(2016, 2, 2, 16, 15, 42)), ('10093', 0, datetime.datetime(2016, 2, 2, 16, 15, 48)), ('10015', 101, datetime.datetime(2016, 2, 2, 16, 20, 6)), ('10005', 101, datetime.datetime(2016, 2, 2, 16, 20, 23)), ('10091', 101, datetime.datetime(2016, 2, 2, 16, 24, 49)), ('10091', 0, datetime.datetime(2016, 2, 2, 16, 27, 3)), ('10060', 0, datetime.datetime(2016, 2, 2, 16, 32, 39)), ('10039', 101, datetime.datetime(2016, 2, 2, 16, 36, 37)), ('10015', 0, datetime.datetime(2016, 2, 2, 16, 38, 57)), ('10005', 0, datetime.datetime(2016, 2, 2, 16, 39, 58)), ('10039', 0, datetime.datetime(2016, 2, 2, 16, 43, 54)), ('10090', 101, datetime.datetime(2016, 2, 2, 16, 46, 33)), ('10090', 0, datetime.datetime(2016, 2, 2, 16, 51, 10)), ('10096', 101, datetime.datetime(2016, 2, 2, 16, 54, 45)), ('10096', 0, datetime.datetime(2016, 2, 2, 16, 58, 49)), ('10015', 101, datetime.datetime(2016, 2, 2, 17, 1, 55)), ('10085', 101, datetime.datetime(2016, 2, 2, 17, 2, 7)), ('10071', 101, datetime.datetime(2016, 2, 2, 17, 2, 30)), ('10060', 101, datetime.datetime(2016, 2, 2, 17, 10, 7)), ('10094', 101, datetime.datetime(2016, 2, 2, 17, 12, 12)), ('10005', 101, datetime.datetime(2016, 2, 2, 17, 16, 9)), ('10094', 0, datetime.datetime(2016, 2, 2, 17, 18, 8)), ('10005', 0, datetime.datetime(2016, 2, 2, 17, 18, 21)), ('10015', 0, datetime.datetime(2016, 2, 2, 17, 24, 50)), ('10085', 0, datetime.datetime(2016, 2, 2, 17, 26, 48)), ('10071', 0, datetime.datetime(2016, 2, 2, 17, 27, 48)), ('10060', 0, datetime.datetime(2016, 2, 2, 17, 40, 7)), ('10091', 101, datetime.datetime(2016, 2, 2, 17, 40, 58)), ('10091', 0, datetime.datetime(2016, 2, 2, 17, 43, 24)), ('10060', 101, datetime.datetime(2016, 2, 2, 17, 54, 12)), ('10090', 101, datetime.datetime(2016, 2, 2, 17, 57, 13)), ('10090', 101, datetime.datetime(2016, 2, 2, 17, 57, 14)), ('10060', 101, datetime.datetime(2016, 2, 2, 17, 59, 8)), ('10026', 101, datetime.datetime(2016, 2, 2, 18, 0, 8)), ('10060', 0, datetime.datetime(2016, 2, 2, 18, 1, 30)), ('10005', 101, datetime.datetime(2016, 2, 2, 18, 2)), ('10026', 0, datetime.datetime(2016, 2, 2, 18, 2, 37)), ('10060', 0, datetime.datetime(2016, 2, 2, 18, 2, 52)), ('10026', 101, datetime.datetime(2016, 2, 2, 18, 3, 53)), ('10026', 0, datetime.datetime(2016, 2, 2, 18, 4, 3)), ('10067', 0, datetime.datetime(2016, 2, 2, 18, 4, 5)), ('10094', 0, datetime.datetime(2016, 2, 2, 18, 4, 12)), ('10090', 0, datetime.datetime(2016, 2, 2, 18, 4, 21)), ('10071', 101, datetime.datetime(2016, 2, 2, 18, 5, 44)), ('10091', 101, datetime.datetime(2016, 2, 2, 18, 6, 21)), ('10091', 0, datetime.datetime(2016, 2, 2, 18, 6, 27)), ('10077', 101, datetime.datetime(2016, 2, 2, 18, 12, 5)), ('10077', 0, datetime.datetime(2016, 2, 2, 18, 12, 14)), ('10015', 0, datetime.datetime(2016, 2, 2, 18, 16, 25)), ('10096', 101, datetime.datetime(2016, 2, 2, 18, 41, 44)), ('10096', 0, datetime.datetime(2016, 2, 2, 18, 45, 13)), ('10003', 101, datetime.datetime(2016, 2, 2, 18, 59, 18)), ('10015', 101, datetime.datetime(2016, 2, 2, 19, 2, 6)), ('10005', 101, datetime.datetime(2016, 2, 2, 19, 3, 16)), ('10096', 0, datetime.datetime(2016, 2, 2, 19, 3, 25)), ('10075', 101, datetime.datetime(2016, 2, 2, 19, 37, 29)), ('10075', 0, datetime.datetime(2016, 2, 2, 20, 3, 8)), ('10039', 101, datetime.datetime(2016, 2, 2, 20, 39, 8)), ('10039', 0, datetime.datetime(2016, 2, 2, 20, 42, 3)), ('10075', 101, datetime.datetime(2016, 2, 2, 21, 29, 53)), ('10075', 0, datetime.datetime(2016, 2, 2, 21, 30, 3)), ('10039', 101, datetime.datetime(2016, 2, 2, 21, 35, 25)), ('10039', 0, datetime.datetime(2016, 2, 2, 21, 35, 32)), ('10060', 0, datetime.datetime(2016, 2, 3, 8, 35, 28)), ('10091', 0, datetime.datetime(2016, 2, 3, 8, 54, 53)), ('10067', 0, datetime.datetime(2016, 2, 3, 9, 3, 34)), ('10026', 0, datetime.datetime(2016, 2, 3, 9, 5, 56)), ('10093', 0, datetime.datetime(2016, 2, 3, 9, 14, 45)), ('10096', 0, datetime.datetime(2016, 2, 3, 9, 24, 30)), ('10077', 0, datetime.datetime(2016, 2, 3, 9, 28, 54)), ('10094', 0, datetime.datetime(2016, 2, 3, 9, 57, 8)), ('10071', 0, datetime.datetime(2016, 2, 3, 10, 4, 31)), ('10094', 101, datetime.datetime(2016, 2, 3, 10, 32, 20)), ('10060', 101, datetime.datetime(2016, 2, 3, 10, 33, 44)), ('10094', 0, datetime.datetime(2016, 2, 3, 10, 36, 29)), ('10026', 101, datetime.datetime(2016, 2, 3, 10, 45, 34)), ('10026', 0, datetime.datetime(2016, 2, 3, 10, 46, 34)), ('10026', 101, datetime.datetime(2016, 2, 3, 10, 46, 51)), ('10085', 0, datetime.datetime(2016, 2, 3, 10, 58, 11)), ('10096', 101, datetime.datetime(2016, 2, 3, 10, 59, 33)), ('10096', 0, datetime.datetime(2016, 2, 3, 11, 2, 49)), ('10005', 0, datetime.datetime(2016, 2, 3, 11, 3, 35)), ('10060', 101, datetime.datetime(2016, 2, 3, 11, 11, 33)), ('10060', 101, datetime.datetime(2016, 2, 3, 11, 12, 39)), ('10060', 0, datetime.datetime(2016, 2, 3, 11, 13, 43)), ('10067', 101, datetime.datetime(2016, 2, 3, 11, 20, 52)), ('10090', 101, datetime.datetime(2016, 2, 3, 11, 21, 48)), ('10026', 0, datetime.datetime(2016, 2, 3, 11, 24, 22)), ('10090', 0, datetime.datetime(2016, 2, 3, 11, 25, 55)), ('10067', 0, datetime.datetime(2016, 2, 3, 11, 26, 31)), ('10060', 0, datetime.datetime(2016, 2, 3, 11, 30, 36)), ('10067', 101, datetime.datetime(2016, 2, 3, 11, 31, 39)), ('10060', 101, datetime.datetime(2016, 2, 3, 11, 33, 22)), ('10060', 0, datetime.datetime(2016, 2, 3, 11, 33, 48)), ('10060', 101, datetime.datetime(2016, 2, 3, 11, 37, 15)), ('10094', 101, datetime.datetime(2016, 2, 3, 11, 39, 10)), ('10094', 0, datetime.datetime(2016, 2, 3, 11, 41, 43)), ('10067', 0, datetime.datetime(2016, 2, 3, 11, 43, 38)), ('10060', 101, datetime.datetime(2016, 2, 3, 11, 45)), ('10005', 101, datetime.datetime(2016, 2, 3, 11, 48, 29)), ('10005', 0, datetime.datetime(2016, 2, 3, 11, 50, 42)), ('10060', 101, datetime.datetime(2016, 2, 3, 11, 51, 55)), ('10005', 101, datetime.datetime(2016, 2, 3, 11, 53, 23)), ('10060', 101, datetime.datetime(2016, 2, 3, 12, 0, 29)), ('10060', 101, datetime.datetime(2016, 2, 3, 12, 7, 54)), ('10091', 101, datetime.datetime(2016, 2, 3, 12, 11, 20)), ('10060', 0, datetime.datetime(2016, 2, 3, 12, 11, 38)), ('10085', 101, datetime.datetime(2016, 2, 3, 12, 12, 21)), ('10090', 101, datetime.datetime(2016, 2, 3, 12, 12, 39)), ('10091', 0, datetime.datetime(2016, 2, 3, 12, 14)), ('10071', 101, datetime.datetime(2016, 2, 3, 12, 15, 11)), ('10090', 0, datetime.datetime(2016, 2, 3, 12, 15, 27)), ('10085', 0, datetime.datetime(2016, 2, 3, 12, 15, 51)), ('10060', 101, datetime.datetime(2016, 2, 3, 12, 16, 17)), ('10071', 0, datetime.datetime(2016, 2, 3, 12, 18, 23)), ('10005', 0, datetime.datetime(2016, 2, 3, 12, 18, 41)), ('10077', 101, datetime.datetime(2016, 2, 3, 12, 22, 34)), ('10077', 0, datetime.datetime(2016, 2, 3, 12, 25, 13)), ('10060', 101, datetime.datetime(2016, 2, 3, 12, 30, 17)), ('10060', 101, datetime.datetime(2016, 2, 3, 12, 31, 28)), ('10094', 101, datetime.datetime(2016, 2, 3, 12, 32, 18)), ('10026', 101, datetime.datetime(2016, 2, 3, 12, 32, 41)), ('10094', 0, datetime.datetime(2016, 2, 3, 12, 34, 57)), ('10091', 101, datetime.datetime(2016, 2, 3, 12, 40, 42)), ('10091', 101, datetime.datetime(2016, 2, 3, 12, 41, 6)), ('10003', 0, datetime.datetime(2016, 2, 3, 12, 41, 23)), ('10005', 101, datetime.datetime(2016, 2, 3, 12, 48, 22)), ('10060', 101, datetime.datetime(2016, 2, 3, 12, 48, 49)), ('10067', 101, datetime.datetime(2016, 2, 3, 12, 52, 51)), ('10090', 0, datetime.datetime(2016, 2, 3, 12, 56, 41)), ('10077', 101, datetime.datetime(2016, 2, 3, 13, 6, 5)), ('10060', 0, datetime.datetime(2016, 2, 3, 13, 10, 20)), ('10067', 101, datetime.datetime(2016, 2, 3, 13, 17, 55)), ('10015', 0, datetime.datetime(2016, 2, 3, 13, 23, 25)), ('10096', 101, datetime.datetime(2016, 2, 3, 13, 27, 7)), ('10094', 101, datetime.datetime(2016, 2, 3, 13, 28, 7)), ('10096', 0, datetime.datetime(2016, 2, 3, 13, 30, 8)), ('10005', 0, datetime.datetime(2016, 2, 3, 13, 34, 31)), ('10077', 0, datetime.datetime(2016, 2, 3, 13, 35, 35)), ('10060', 101, datetime.datetime(2016, 2, 3, 13, 35, 48)), ('10026', 0, datetime.datetime(2016, 2, 3, 13, 39, 32)), ('10060', 0, datetime.datetime(2016, 2, 3, 13, 40, 10)), ('10075', 0, datetime.datetime(2016, 2, 3, 13, 41, 32)), ('10005', 101, datetime.datetime(2016, 2, 3, 13, 43, 19)), ('10090', 0, datetime.datetime(2016, 2, 3, 13, 43, 39)), ('10071', 101, datetime.datetime(2016, 2, 3, 13, 46, 10)), ('10090', 101, datetime.datetime(2016, 2, 3, 13, 59, 7)), ('10005', 0, datetime.datetime(2016, 2, 3, 14, 0, 59)), ('10090', 0, datetime.datetime(2016, 2, 3, 14, 2, 9)), ('10003', 101, datetime.datetime(2016, 2, 3, 14, 2, 24)), ('10071', 0, datetime.datetime(2016, 2, 3, 14, 3, 45)), ('10003', 0, datetime.datetime(2016, 2, 3, 14, 4, 7)), ('10060', 101, datetime.datetime(2016, 2, 3, 14, 9, 24)), ('10085', 101, datetime.datetime(2016, 2, 3, 14, 14, 45)), ('10085', 0, datetime.datetime(2016, 2, 3, 14, 17, 43)), ('10026', 101, datetime.datetime(2016, 2, 3, 14, 33, 53)), ('10096', 101, datetime.datetime(2016, 2, 3, 14, 38, 19)), ('10091', 101, datetime.datetime(2016, 2, 3, 14, 41, 59)), ('10026', 0, datetime.datetime(2016, 2, 3, 14, 42, 27)), ('10090', 101, datetime.datetime(2016, 2, 3, 14, 43, 2)), ('10090', 0, datetime.datetime(2016, 2, 3, 14, 43, 29)), ('10091', 0, datetime.datetime(2016, 2, 3, 14, 44, 41)), ('10003', 101, datetime.datetime(2016, 2, 3, 14, 46, 28)), ('10077', 101, datetime.datetime(2016, 2, 3, 14, 53, 35)), ('10094', 101, datetime.datetime(2016, 2, 3, 14, 54, 22)), ('10005', 101, datetime.datetime(2016, 2, 3, 14, 55, 39)), ('10094', 0, datetime.datetime(2016, 2, 3, 14, 57, 37)), ('10077', 0, datetime.datetime(2016, 2, 3, 15, 7, 38)), ('10015', 0, datetime.datetime(2016, 2, 3, 15, 13, 56)), ('10067', 101, datetime.datetime(2016, 2, 3, 15, 15, 8)), ('10090', 101, datetime.datetime(2016, 2, 3, 15, 15, 21)), ('10015', 101, datetime.datetime(2016, 2, 3, 15, 17, 51)), ('10096', 101, datetime.datetime(2016, 2, 3, 15, 18, 16)), ('10090', 0, datetime.datetime(2016, 2, 3, 15, 18, 42)), ('10015', 0, datetime.datetime(2016, 2, 3, 15, 19, 9)), ('10096', 0, datetime.datetime(2016, 2, 3, 15, 21, 1)), ('10005', 0, datetime.datetime(2016, 2, 3, 15, 32, 58)), ('10067', 101, datetime.datetime(2016, 2, 3, 15, 34, 40)), ('10090', 101, datetime.datetime(2016, 2, 3, 15, 35, 11)), ('10090', 0, datetime.datetime(2016, 2, 3, 15, 37, 24)), ('10090', 101, datetime.datetime(2016, 2, 3, 15, 38, 32)), ('10085', 101, datetime.datetime(2016, 2, 3, 15, 39, 34)), ('10085', 101, datetime.datetime(2016, 2, 3, 15, 39, 34)), ('10090', 0, datetime.datetime(2016, 2, 3, 15, 39, 38)), ('10085', 0, datetime.datetime(2016, 2, 3, 15, 43, 37)), ('10060', 101, datetime.datetime(2016, 2, 3, 15, 47, 30)), ('10091', 101, datetime.datetime(2016, 2, 3, 15, 48, 42)), ('10071', 101, datetime.datetime(2016, 2, 3, 15, 52, 28)), ('10091', 0, datetime.datetime(2016, 2, 3, 15, 55, 7)), ('10060', 0, datetime.datetime(2016, 2, 3, 15, 59, 31)), ('10075', 101, datetime.datetime(2016, 2, 3, 16, 0, 32)), ('10077', 101, datetime.datetime(2016, 2, 3, 16, 1, 12)), ('10060', 101, datetime.datetime(2016, 2, 3, 16, 4, 24)), ('10093', 101, datetime.datetime(2016, 2, 3, 16, 5, 5)), ('10093', 0, datetime.datetime(2016, 2, 3, 16, 5, 16)), ('10094', 101, datetime.datetime(2016, 2, 3, 16, 7, 32)), ('10093', 101, datetime.datetime(2016, 2, 3, 16, 8, 12))
				# ]
				zk.enableDevice()
				#zk.disconnect()
				# print "####################",attendance
				if (attendance):
					self.env["hr.employee"].emp_attendance_fetcher(attendance, date_yesterday, in_machine, out_machine)
				# for lattendance in attendance:
					# time_att = str(lattendance[2].date()) + ' ' +str(lattendance[2].time())
					# atten_time1 = datetime.strptime(str(time_att), '%Y-%m-%d %H:%M:%S')
					# atten_time = atten_time1 - timedelta(hours=5,minutes=30)
					# atten_time = datetime.strftime(atten_time,'%Y-%m-%d %H:%M:%S')
					# atten_time1 = datetime.strftime(atten_time1,'%Y-%m-%d %H:%M:%S')
					# in_time = datetime.strptime(atten_time1,'%Y-%m-%d %H:%M:%S').time()
					# employee_id = hr_employee.search(cr,uid,[("emp_code", "=", str(lattendance[0]))])
					# address_id = False
					# category = False
					# if employee_id:
					#     address_id = hr_employee.browse(cr,uid,employee_id[0]).address_id
					#     category = hr_employee.browse(cr,uid,employee_id[0]).category
					# 
					# try:
					#     atten_ids = hr_attendance.search(cr,uid,[('employee_id','=',employee_id[0]),('name','=',atten_time)])
					#     if atten_ids:
					#         continue
					#     else:
					#         # print "Date %s, Name %s: %s" % ( lattendance[2].date(), lattendance[2].time(), lattendance[0] )
					#         atten_id = hr_attendance.create(cr,uid,{'name':atten_time,'address_id':address_id.id,'category':category,'day':str(lattendance[2].date()),'employee_id':employee_id[0],'action':'sign_in'})
					#         # print atten_id
					# except Exception,e:
					#     pass
					#     # print "Exception..Attendance creation======", e.args
				return True
			else:
				raise Warning(_("Unable to connect, please check the Biometrics Machine parameters and network connections."))
			# raise UserError(_('Warning !'),_("Unable to connect, please check the Biometrics Machine parameters and network connections."))
	
	def clear_attendance(self, cr, uid, ids, context=None):
		# machine_ip = self.browse(cr,uid,ids).name
		# port = self.browse(cr,uid,ids).port
		# zk = zklib.ZKLib(machine_ip, int(port))
		# res = zk.connect()
		# if res == True:
		#     zk.enableDevice()
		#     zk.disableDevice()
		#     res = zk.clearAttendance()
		#     print res
		#     zk.enableDevice()
		#     zk.disconnect()
		#     return True
		# else:
		#     raise osv.except_osv(_('Warning !'),_("Unable to connect, please check the parameters and network connections."))
		return True