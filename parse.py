class HTTPrequest:

    def __init__(self, cmd, path, headers, payload):
        self.cmd = cmd
        self.path = path
        self.headers = headers
        self.payload = payload


def parse_http_request(request):
    headers = request.decode().split('\r\n')
    reqline = headers.pop(0)
    payload = headers.pop()
    headers_dict = {}

    for header in headers:
        if header != '':
            k, v = header.split(': ')
            headers_dict[k] = v
    try:
        cmd, path, prot = reqline.split()
    except ValueError:
        cmd = ''
        path = ''
        payload = ''

    return HTTPrequest(cmd, path, headers_dict, payload)


def parse_post(post_str):
    pdata = {}
    items = post_str.strip().split('&')
    pet_count = 0
    for item in items:
        keyword, value = item.split('=')
        value = value.replace('+', ' ')
        keyword = keyword.replace('%5B', '[')
        keyword = keyword.replace('%5D', ']')
        if keyword == "pets[]":
            pdata[f'pet[{pet_count}]'] = value
            pet_count += 1
        else:
            pdata[keyword] = value

    return pdata
