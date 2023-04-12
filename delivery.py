"""
Lydia Price, 200004521
The below functions are helper functions to deliver relevant information to the web
"""


def read_file_content(filename, binary=False):
    # General utility to read entire content of file that could be binary
    if binary:
        mode = 'rb'
    else:
        mode = 'r'
    with open(filename, mode) as fin:
        content = fin.read()
    return content


def deliver_html(conn, filename):
    # Deliver content of HTML file
    content = read_file_content(filename)
    deliver_200(conn)
    http_header(conn, 'Content-Type: text/html; charset=utf-8')
    http_body(conn, content.encode())


def deliver_css(conn, filename):
    # Deliver content of CSS file
    content = read_file_content(filename)
    deliver_200(conn)
    http_header(conn, 'Content-Type: text/css')
    http_body(conn, content.encode())


def deliver_jpeg(conn, filename):
    # Deliver content of JPEG image file
    content = read_file_content(filename, binary=True)
    deliver_200(conn)
    http_header(conn, 'Content-Type: image/jpeg')
    http_header(conn, 'Accept-Ranges: bytes')
    http_body(conn, content)


def deliver_json_string(conn, jsonstr):
    # Deliver JSON String
    deliver_200(conn)
    http_header(conn, 'Content-Type: application/json')
    http_body(conn, jsonstr.encode())


def deliver_json_file(conn, filename):
    # Deliver JSON server side file
    content = read_file_content(filename)
    deliver_json_string(conn, content)


def deliver_gif(conn, filename):
    # Deliver content of GIF image file
    content = read_file_content(filename, binary=True)
    deliver_200(conn)
    http_header(conn, 'Content-Type: image/gif')
    http_header(conn, 'Accept-Ranges: bytes')
    http_body(conn, content)


def deliver_js(conn, filename):
    # Dekiver the contents of a JavaScript fucntion
    content = read_file_content(filename)
    deliver_200(conn)
    http_header(conn, 'Content-Type: text/javascript')
    http_body(conn, content.encode())


def http_header(conn, header_line):
    # Send the header line as string instance
    conn.send((header_line + '\r\n').encode())


def http_body(conn, payload):
    # Send payload as byte string
    conn.send('\r\n'.encode())
    conn.send(payload)


def http_status(conn, status):
    # Send status line
    conn.send(('HTTP/1.1 ' + status + '\r\n').encode())


def deliver_200(conn):
    # Send 200 OK Status response
    http_status(conn, '200 OK')


def deliver_404(conn):
    # Send 404 not found status response
    http_status(conn, '404 Not Found')
