from django.db import models

# Create your models here.


#class Staff(models.Model):
	#firstname = models.CharField(max_length=100)
	# lastname = models.CharField(max_length=100)
	# email = models.CharField(max_length=100)
	# phone = models.CharField(max_length=100)
	# grade = models.CharField(max_length=100)
	# workingpattern = models.CharField(max_length=100)

	#def __str__(self):
		#return self.firstname

class Masterrota(models.Model):
	date = models.DateField(auto_now=False, auto_now_add=False)
	day = models.CharField(max_length=50)
	person1shifts = models.CharField(max_length=50)
	person2shifts = models.CharField(max_length=50)
	person3shifts = models.CharField(max_length=50)
	person4shifts = models.CharField(max_length=50)
	person5shifts = models.CharField(max_length=50)
	person6shifts = models.CharField(max_length=50)
	person7shifts = models.CharField(max_length=50)
	person8shifts = models.CharField(max_length=50)
	person9shifts = models.CharField(max_length=50)
	person10shifts = models.CharField(max_length=50)
	person11shifts = models.CharField(max_length=50)
	person12shifts = models.CharField(max_length=50)
	person13shifts = models.CharField(max_length=50)
	person14shifts = models.CharField(max_length=50)
	person15shifts = models.CharField(max_length=50)
	person16shifts = models.CharField(max_length=50)
	person17shifts = models.CharField(max_length=50)
	person18shifts = models.CharField(max_length=50)
	person19shifts = models.CharField(max_length=50)
	person20shifts = models.CharField(max_length=50)
	person21shifts = models.CharField(max_length=50)
	person22shifts = models.CharField(max_length=50)
	person23shifts = models.CharField(max_length=50)
	person24shifts = models.CharField(max_length=50)
	person25shifts = models.CharField(max_length=50)
	person26shifts = models.CharField(max_length=50)
	person27shifts = models.CharField(max_length=50)
	person28shifts = models.CharField(max_length=50)
	person29shifts = models.CharField(max_length=50)
	person30shifts = models.CharField(max_length=50)

	def __str__(self):
		return str(self.date)
	
	