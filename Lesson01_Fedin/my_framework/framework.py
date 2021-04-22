from wsgiref.util import setup_testing_defaults


class Not_Found:
    def __call__(self, *args, **kwargs):
        return "404 Not Found", [b"404 Not Found"]


class Framework:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        setup_testing_defaults(environ)
        print("work")
        path = environ["PATH_INFO"]
        if not path.endswith("/"):
            path += "/"
        if path in self.routes:
            view = self.routes[path]
        else:
            view = Not_Found()
        request = {}
        for front in self.fronts:
            front(request)
        print(request)
        code, body = view(request)
        start_response(code, [("Content-Type", "text/html")])
        return [body.encode("utf-8")]
