from django.db import models

# Create your models here.
class Log(models.Model):

	host = models.CharField(max_length=255)
	user = models.CharField(max_length=255)
	time = models.DateTimeField()
	utc_offset = models.IntegerField()
	request = models.CharField(max_length=1024)
	status = models.PositiveSmallIntegerField()
	size = models.PositiveIntegerField()
	referer = models.CharField(max_length=1024)
	agent = models.CharField(max_length=1024)

