import datetime

from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from django.db.models import Q

from birthdays.models import Friend
from birthdays.utils import send_email_to_me

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute=0, hour=12)),
    name="task_notify_about_birthday"
)
def task_notify_about_birthday():
    day = datetime.datetime.now().day + 1
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    friends = Friend.objects.filter(Q(birth_date__day=day) & Q(birth_date__month=month))
    for friend in friends:
        context = {
            'first_name': friend.first_name,
            'last_name': friend.last_name,
            'birth_date': friend.birth_date,
            'age': year - friend.birth_date.year,
        }
        send_email_to_me(context)
        logger.info("Email about {} {}'s birthday was sent.".format(friend.first_name, friend.last_name))
