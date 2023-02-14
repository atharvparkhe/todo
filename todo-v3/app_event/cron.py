from .models import EventModel
from datetime import datetime


def change_event_status():
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    event_objs = EventModel.objects.filter(expiered=False)
    for obj in event_objs:
        check = obj.finish.strftime("%d/%m/%Y %H:%M:%S")
        if check < now:
            obj.expiered = True
            obj.save()
            print("done")