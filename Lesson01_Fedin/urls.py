from datetime import date

def date_front(request):
    request["date"] = date.today()


def key_front(request):
    request["user"] = "Petr"


fronts = [key_front, date_front]
