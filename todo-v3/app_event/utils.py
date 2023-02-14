from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime


def date_time_valicator(value):
    day = value.weekday()
    time = value.strftime("%H")
    inp = value
    now = datetime.datetime.now()
    if inp.strftime("%d/%m/%Y %H:%M:%S") < now.strftime("%d/%m/%Y %H:%M:%S"):
        raise ValidationError(
            _("appoinment should be after present time"),
            params={"value":value}
        )
    if day == 5 or day == 6:
        raise ValidationError(
            _("appoinment not possible on weekends"),
            params={"day":day}
        )
    if time > '9' and time < '17':
        raise ValidationError(
            _("appoinment is schedule in betn 9 to 5 Pm"),
            params={"time":time}
        )



status_choices = (
    ("progress", "In Progress"),
    ("completed", "Completed"),
    ("pending", "Pending"),
    ("late","Done Late")
)