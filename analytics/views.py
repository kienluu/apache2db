# Create your views here.
from datetime import timedelta
from itertools import izip
from django.db.models.aggregates import Max, Min
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response
from analytics.utils import date_range, pair_inter, Object
from apachelog.models import Log



def hits_per_interval(request, days=1):
	context = {}
	rows = []
	logs = Log.objects.order_by('time').all()
	dates= Log.objects.aggregate(Max('time'), Min('time'))
	min_date = dates['time__min'].date()
	max_date = dates['time__max'].date()
	dates = date_range(min_date,max_date, days)

	for from_date,to_date in pair_inter(dates):
		count = Log.objects.filter(
			Q(time__gte=from_date) & Q(time__lt=to_date)
		).count()
		row= Object()
		row.date = from_date
		row.hits = count
		rows.append(row)

	context['rows']=rows
	return render_to_response('analytics/hits.html', context,mimetype='text')
