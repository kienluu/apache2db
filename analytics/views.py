# Create your views here.
from datetime import timedelta
from itertools import izip
from django.db.models.aggregates import Max, Min
from django.db.models.expressions import F
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from analytics.utils import date_range, pair_inter, Object
from apachelog.models import Log


# all the times are stored in local -4 utc time so this should work
local_utcoffset = timedelta(hours=0)

def hits_per_interval(request, days=1):
	"""
	hits per day to facebook.html or
	"""
	context = {}
	rows = []
	logs = Log.objects.order_by('time').all()
	# should include the timezone info in this
	dates= Log.objects.aggregate(Max('time'), Min('time'))
	min_date = dates['time__min'].date()
	max_date = dates['time__max'].date()
	dates = date_range(min_date,max_date, days)

	for from_date,to_date in pair_inter(dates):
		count = Log.objects.filter(
			Q(time__gte=from_date) & Q(time__lt=to_date)
			&
			(
				Q(request__startswith='GET /facebook.htm') | Q(request__startswith='GET /fb.htm')
			)
		).count()
		row= Object()
		row.date = from_date
		row.hits = count
		rows.append(row)

	context['rows']=rows
	context['use_tabs']=request.GET.get('use_tabs') in ['1','true','True']
	return render_to_response('analytics/hits.html', context,mimetype='text')
