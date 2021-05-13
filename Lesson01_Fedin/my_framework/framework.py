import quopri, json
from my_framework.requests import post_req, get_req
from patterns.creational_patterns import Logger

logger = Logger("main")

class Not_Found:
    def __call__(self, request):
        return "404 Not Found", "404 Not Found"


class Framework:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        # setup_testing_defaults(environ)
        # print("work")
        path = environ["PATH_INFO"]
        if not path.endswith("/"):
            path += "/"
        logger.log(path)

        request = {}
        method = environ["REQUEST_METHOD"]
        request["method"] = method

        if method == "POST":
            data = post_req(environ)
            request["data"] = data
            norm_data = decode_mime(data)
            write_file(norm_data)
            print(f"Получен post запрос {norm_data}")

        if method == "GET":
            data = get_req(environ)
            request["request_params"] = data
            print(f"Получен get запрос {data}")

        if path in self.routes:
            view = self.routes[path]
        else:
            view = Not_Found()

        for front in self.fronts:
            front(request)

        code, body = view(request)
        start_response(code, [("Content-Type", "text/html")])
        return [body.encode("utf-8")]


def write_file(data):
    with open("post_data.json", "a") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def decode_mime(data):
    ret_data = {}
    for param, value in data.items():
        normalize_value = bytes(
            value.replace("%", "=").replace("+", " "), "UTF-8"
        )
        decoded_value = quopri.decodestring(normalize_value).decode("UTF-8")
        ret_data[param] = decoded_value
    return ret_data
