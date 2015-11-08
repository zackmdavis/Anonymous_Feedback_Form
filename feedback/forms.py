from django.forms import ModelForm

from feedback.models import FeedbackItem

class FeedbackForm(ModelForm):
    class Meta:
        model = FeedbackItem
        fields = ('content',)
