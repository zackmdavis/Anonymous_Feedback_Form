from django.db import models
from django.utils import timezone

class FeedbackItem(models.Model):
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    def __repr__(self):
        return "<FeedbackItem: {}{}>".format(
            self.content[:30],
            '...' if len(self.content) > 30 else ''
        )
