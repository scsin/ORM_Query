# from django.contrib.auth.models import User, Group
from api.models import Agent, Event, User, Group


def get_active_users() -> User:
    """Traga todos os uarios ativos, seu último login deve ser menor que 10 dias """
    return User.objects.all()
    #raise NotImplementedError

def get_amount_users() -> User:
    """Retorne a quantidade total de usuarios do sistema """
    return len(User.objects.all())
    #raise NotImplementedError


def get_admin_users() -> User:
    """Traga todos os usuarios com grupo = 'admin"""
    return User.objects.filter(group=1)
    # raise NotImplementedError


def get_all_debug_events() -> Event:
    """Traga todos os eventos com tipo debug"""
    return Event.objects.filter(level__contains='debug')
    #raise NotImplementedError


def get_all_critical_events_by_user(agent) -> Event:
    """Traga todos os eventos do tipo critico de um usuário específico"""
    # return Event.objects.filter(level__contains='debug')
    raise NotImplementedError


def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes de associados a um usuário pelo nome do usuário"""
    raise NotImplementedError


def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information"""
    raise NotImplementedError
