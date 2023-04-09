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


def parse_post(pstring):
    pdata = {}
    items = pstring.strip().split('&')

    for item in items:
        keyword, value = item.split('=')
        value = value.replace('+', ' ')
        keyword = keyword.replace('%5B', '[')
        keyword = keyword.replace('%5D', ']')
        pdata[keyword] = value

    return pdata
