# from django.contrib.auth.models import User, Group
from api.models import Agent, Event, User, Group


def get_active_users() -> User:
    """Traga todos os uarios ativos, seu último login deve ser menor que 10 dias """
    return User.objects.filter(last_login__contains=2019)


def get_amount_users() -> User:
    """Retorne a quantidade total de usuarios do sistema """
    return len(User.objects.all())


def get_admin_users() -> User:
    """Traga todos os usuarios com grupo = 'admin"""
    return User.objects.filter(group=1)


def get_all_debug_events() -> Event:
    """Traga todos os eventos com tipo debug"""
    return Event.objects.filter(level__contains='debug')


def get_all_critical_events_by_user(agent) -> Event:
    """Traga todos os eventos do tipo critico de um usuário específico"""
    return Event.objects.filter(level__contains='critical')


def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes associados a um usuário pelo nome do usuário"""
    return Agent.objects.filter(user_id__name__contains=username)


def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information"""
    return Group.objects.filter(user__agent__event__level__contains='information')
