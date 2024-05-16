
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Tratamiento_1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    Opcion_1 = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='¿Quieres opción 1?')
    Opcion_2 = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='¿Quieres opción 2?')
class Opcion_1(Page):
    form_model = 'player'
    form_fields = ['Opcion_1']
class Opcion_2(Page):
    form_model = 'player'
    form_fields = ['Opcion_2']
page_sequence = [Opcion_1, Opcion_2]