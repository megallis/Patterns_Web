from datetime import date
from views import Index, About, Home

routes = {
    "/": Index(),
    "/about/": About(),
    "/home/": Home(),
}


def date_front(request):
    request["data"] = date.today()


def key_front(request):
    request["user"] = "Petr"


fronts = [key_front, date_front]
