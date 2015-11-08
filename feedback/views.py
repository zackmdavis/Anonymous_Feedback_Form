from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from feedback.models import FeedbackItem
from feedback.forms import FeedbackForm

SIGNATURE = ("Signed, anonymous-feedback web application "
             "on behalf of {}").format(
                 settings.FEEDBACK_SUBJECT_INITIALS)


@require_http_methods(["GET", "POST"])
def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks for your feedback! {}".format(SIGNATURE))
            return redirect('feedback')
        else:
            messages.error(
                request,
                "Thanks, but your feedback couldn't be accepted "
                "due to errors. {}".format(SIGNATURE))
            pass  # fallthrough to render
    else:  # GET
        form = FeedbackForm()
    return render(request, 'feedback.html',
                  {'subject': settings.FEEDBACK_SUBJECT, 'form': form})
