import time
import threading # Question 2 Code

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TestModel, SignalLog  # add SignalLog Question 3 Code


@receiver(post_save, sender=TestModel)
def slow_signal(sender, instance, **kwargs):

    """print("Signal Started")

    # Question 2 Code
    print("Signal Thread ID:", threading.get_ident())

    time.sleep(5)

    print("Signal Finished")"""

   # Question 3 Code
    print("Signal Executed")

    SignalLog.objects.create(
        message="Signal Data Saved"
    )