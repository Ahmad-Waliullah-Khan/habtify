from django.contrib import admin

from .models import Habit, Tracker

@admin.register(Tracker)
class HabitsAdmin(admin.ModelAdmin):
	fields = ('habit', 'description', 'user', 'done')

	list_display = ('habit', 'description', 'user', 'started_at', 'updated_at' , 'is_complete')

	def is_complete(self, instance):
		if instance.done == True:
			return "Completed"
		else:
			return "On Going"

	def get_user(self):
		pass

@admin.register(Habit)
class HabitsAdmin(admin.ModelAdmin):
	fields = ('title', 'description', 'user')

	list_display = ('title', 'description', 'user', 'started_at', 'updated_at')

	def get_user(self):
		pass
