from django.db import models

# Create your models here.

class Rota(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	tier = models.IntegerField(default=0)
	is_published = models.BooleanField(default=True) 
	rota = models.URLField()

	def __str__(self):
		return self.title

