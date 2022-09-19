from django import forms
from django.forms import inlineformset_factory

from pegasus_app.models import PhoneNumberCheckConfig, ScheduleDay


class PhoneNumberCheckConfigForm(forms.ModelForm):
    class Meta:
        model = PhoneNumberCheckConfig
        fields = ['ima_name', 'phone', 'failure_threshold', 'test_frequency']


class ScheduleDayForm(forms.ModelForm):
    class Meta:
        model = ScheduleDay
        fields = ['day', 'is_active', 'open_time', 'close_time']


ScheduleDayFormset = inlineformset_factory(PhoneNumberCheckConfig, ScheduleDay, fields='__all__', extra=0)
