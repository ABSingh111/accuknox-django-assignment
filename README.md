# Accuknox Django Trainee Assignment

## Topic 1: Django Signals

### Question 1

By default, Django signals are executed synchronously.

Proof:
A delay of 5 seconds was added using time.sleep(5) inside the signal. The browser response also took approximately 5 seconds, proving the caller waited for the signal execution to complete.

![image](https://github.com/ABSingh111/accuknox-django-assignment/blob/main/screenshots/a1.jpg)

![image](https://github.com/ABSingh111/accuknox-django-assignment/blob/main/screenshots/a2.jpg)
---

### Question 2

Django signals run in the same thread as the caller.

Proof:
The caller thread ID and signal thread ID were printed and both values were identical.

---

### Question 3

Django signals run in the same database transaction as the caller.

Proof:
Inside a transaction block, a model object was created and the signal also created another database entry. An exception forced the transaction to rollback. After rollback, both database tables were empty, proving both operations were part of the same transaction.

---

## Topic 2: Custom Rectangle Class

A custom Rectangle class was created which supports iteration.

Example Output:

{'length': 10}
{'width': 5}

---

## Setup Instructions

```bash
pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```
