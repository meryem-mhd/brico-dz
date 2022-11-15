from django_choice import DjangoChoice, DjangoChoices

class PerExpChoice(DjangoChoices):
    Paint = DjangoChoice('Paint')
    Electricity = DjangoChoice('Electricity')
    Plombing = DjangoChoice('Plombing')
    