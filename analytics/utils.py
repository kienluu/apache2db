from datetime import timedelta
from itertools import izip

class Object(object):
	pass

def date_range(start_date, end_date, step=1):
	"""
	returns list of dates from start_date to end_date, possibly a bit more depending on step size.  step in days
	"""
	result=[start_date]
	index = 0
	delta = timedelta(days=1)
	while result[index]<=end_date:
		result.append(result[index]+delta)
		index+=1
	return result

def pair_inter(iterable):
	return izip(iterable[:-1:1], iterable[1::1])