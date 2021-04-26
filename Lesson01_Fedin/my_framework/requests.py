def post_req(environ):
    content_length_data = environ.get("CONTENT_LENGTH")
    content_length = int(content_length_data) if content_length_data else 0
    if content_length == 0:
        data = b""
    else:
        data = environ["wsgi.input"].read(content_length)
        result = {}
        data_str = data.decode(encoding="utf-8")
        params = data_str.split("&")
        for item in params:
            k, v = item.split("=")
            result[k] = v
    return result


def get_req(environ):
    data = environ["QUERY_STRING"]
    result = {}
    if data:
        params = data.split("&")
        for item in params:
            k, v = item.split("=")
            result[k] = v
    return result
