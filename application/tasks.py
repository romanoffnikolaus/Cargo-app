from celery import shared_task

from .add_utils.task import change_car_location


@shared_task
def setup_periodic_tasks():
    change_car_location()
