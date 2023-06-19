from django.contrib import admin
from . models import *
# Register your models here.
@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display=['id','user','notes_type']
    list_display_links=['id','user']

@admin.register(Share_Notes)
class Share_Notes_Admin(admin.ModelAdmin):
    list_display=['id','sender','shared_timing']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['email','username']
    list_display_links=['email','username']
