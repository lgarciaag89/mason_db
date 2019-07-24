from django.utils import timezone
import datetime
from django.core.exceptions import ValidationError


def validar_fecha_en_pasado(date):
    if (date >= timezone.now().date()):
        raise ValidationError(('%(date)s es en el futuro'), params={'date': date}, )
