import time
import threading # Question 2 Code
from django.db import transaction # Question 3 Code


from django.http import HttpResponse

from .models import TestModel


def test_signal(request):
    
    """
    # Question 2 Code
    print("Caller Thread ID:", threading.get_ident())
    
    # Question 1 Code
    start = time.time()

    TestModel.objects.create(name="AB")

    end = time.time()

    total = end - start

    return HttpResponse(f"Time Taken: {total}") """

    try:

        with transaction.atomic():

            TestModel.objects.create(name="AB")

            raise Exception("Transaction Rollback")

    except Exception as e:

        return HttpResponse(str(e))