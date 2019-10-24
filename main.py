from api.models import Agent, Event, User, Group
import datetime

def get_active_users() -> User:
    today = datetime.date.today()
    then_days_ago = datetime.timedelta(days=10)
    return User.objects.filter(last_login__gte=today-then_days_ago)


def get_amount_users() -> User:
    return len(User.objects.all())


def get_admin_users() -> User:
    return User.objects.filter(group=1)


def get_all_debug_events() -> Event:
    return Event.objects.filter(level__contains='debug')


def get_all_critical_events_by_user(agent) -> Event:
    return Event.objects.filter(level__contains='critical')


def get_all_agents_by_user(username) -> Agent:
    return Agent.objects.filter(user_id__name__contains=username)


def get_all_events_by_group() -> Group:
    return Group.objects.filter(user__agent__event__level__contains='information')
