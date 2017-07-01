import math
class CalcAtten(object):
	"""docstring for CalcAtten"""
	def __init__(self, p,t,pw):
		super(CalcAtten, self).__init__()
		self.present = int(p)
		self.total = int(t)
		self.per_week_class = int(pw)
		self.cur_atten = (present/tot)*100
	def req_lec(self):
		res = math.ceil((self.cur_atten*(self.total+self.per_week_class))/100)
		return res
