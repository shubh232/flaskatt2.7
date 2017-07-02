import math
class CalcAtten(object):
	"""docstring for CalcAtten"""
	def __init__(self, p,t,pw):
		super(CalcAtten, self).__init__()
		self.present = float(p)
		self.total = float(t)
		self.per_week_class = float(pw)
		self.cur_atten = (self.present/self.total)*100
	def req_lec(self):
		res = math.ceil((self.cur_atten*(self.total+self.per_week_class))/100)
		res = res - self.present
		return int(res)
