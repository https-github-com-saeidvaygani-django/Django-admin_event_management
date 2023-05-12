from django.contrib import admin
from .models import EventTable, AttendeeTable, PaymentTable, SpeakersTable, SessionTable
from django.forms import TextInput, Textarea
from django import forms
from django.utils.html import format_html
from django.db import models



class EventTableAdmin(admin.ModelAdmin):
    def photo_display(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)

    list_display = ('id', 'name', 'date', 'location', 'photo_display')
    list_display_links = ('id', 'name', 'date', 'location')
    list_filter = ('date',)
    search_fields = ('name',)
    sortable_by = ('date',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})}
    }

    photo_display.short_description = 'Photo'


class AttendeeTableAdmin(admin.ModelAdmin):
    list_display = ('id','fname','lname','company','country','phone','phone','email','website','degree','industries_type')
    list_display_links = ('id','fname','lname','company','country','phone','phone','email','website','degree','industries_type')
    list_filter = ('country','degree','industries_type')
    search_fields = ('lname','country','industries_type')
    sortable_by = ('id','country','degree')
    ordering =('id',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})},
        models.CharField: {'widget': TextInput(attrs={'size': '50'})}
    }
    
# for putting the placeholder in TextInput we define Meta class. also you can write it in the models.py or admin.py
class AttendeeTableForm(forms.ModelForm):
    class Meta:
        model = AttendeeTable
        fields = '__all__'
        widgets = {
            'website': forms.TextInput(attrs={'placeholder': 'www.yoursite.com'})
        }

class PaymentTableAdmin(admin.ModelAdmin):
    list_display = ('id','payment_type','amount')
    list_display_links = ('id','payment_type','amount')
    list_filter = ('payment_type',)
    


class SpeakersTableAdmin(admin.ModelAdmin):
    list_display = ('id','fname','lname','degree')
    list_display_links = ('id','fname','lname','degree')
    list_filter = ('degree',)
    search_fields = ('fname','lname','country')
    sortable_by = ('id','country')
    ordering =('id',)

class SessionTableAdmin(admin.ModelAdmin):
    list_display = ('id','title','start_time','end_time')
    list_display_links = ('id','title','start_time','end_time')
    list_filter = ('title',)
    search_fields = ('title',)
    sortable_by = ('id','title')
    ordering =('id',)


admin.site.register(EventTable, EventTableAdmin)
admin.site.register(AttendeeTable, AttendeeTableAdmin)
admin.site.register(PaymentTable, PaymentTableAdmin)
admin.site.register(SpeakersTable, SpeakersTableAdmin)
admin.site.register(SessionTable, SessionTableAdmin)
