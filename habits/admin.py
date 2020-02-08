from django.contrib import admin

from .models import Habit, Tracker

@admin.register(Tracker)
class HabitsAdmin(admin.ModelAdmin):
	fields = ('title', 'habit', 'description', 'user', 'done')

	list_display = ('title', 'habit', 'description', 'user', 'created_at', 'updated_at')

	def get_user(self):
		pass

@admin.register(Habit)
class HabitsAdmin(admin.ModelAdmin):
	fields = ('title', 'description', 'user')

	def get_user(self):
		pass
