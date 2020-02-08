from django.contrib import admin

from .models import Habit, Tracker

@admin.register(Tracker)
class TrackerAdmin(admin.ModelAdmin):
	fields = ('habit', 'description',  'done')

	list_display = ('habit', 'description', 'started_at', 'user' , 'updated_at' ,  'is_complete')

	def is_complete(self, instance):
		if instance.done == True:
			return "Completed"
		else:
			return "On Going"

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super(TrackerAdmin, self).save_model(request, obj, form, change)

@admin.register(Habit)
class HabitsAdmin(admin.ModelAdmin):
	fields = ('title', 'description')

	list_display = ('title', 'description', 'started_at', 'updated_at')
	exclude = ['user']

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super(HabitsAdmin, self).save_model(request, obj, form, change)
