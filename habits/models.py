from django.db import models
from django.contrib.auth.models import User

"""
Database representing the Habit Tracker
"""
class Habit(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField()
	started_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{}".format(self.title)

	def save_model(self, request, obj, form, change):
	    obj.user = request.user
	    super().save_model(request, obj, form, change)

	class Meta:
		verbose_name = "habit"
		verbose_name_plural = "Habit Management"

class Tracker(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
	description = models.TextField()
	started_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	done = models.BooleanField(default=False)

	def __str__(self):
		return "{}".format(self.habit)

	def save_model(self, request, obj, form, change):
	    obj.user = request.user
	    super().save_model(request, obj, form, change)

	class Meta:
		verbose_name = "tracker"
		verbose_name_plural = "Track Habits"