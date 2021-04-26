from my_framework.templator import render


class Index:
    def __call__(self, request):
        return "200 OK", render("index.html", data=request.get("data", None))


class About:
    def __call__(self, request):
        return "200 OK", render("about.html", data=request.get("", None))


class Home:
    def __call__(self, request):
        return "200 OK", "<h2>HOME</h2>"


class Contact_Form:
    def __call__(self, request):
        return "200 OK", render("contact.html", data=request.get("data", None))
