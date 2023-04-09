def gobble_file(filename, binary=False):
    """General utility to read entire content of file that could be binary"""
    if binary:
        mode = 'rb'
    else:
        mode = 'r'
    with open(filename, mode) as fin:
        content = fin.read()
    return content


def deliver_html(connection_socket, filename):
    # Deliver content of HTML file
    content = gobble_file(filename)
    http_header(connection_socket, 'Content-Type: text/html')
    http_body(connection_socket, content.encode())


def deliver_jpeg(conn, filename):
    # Deliver content of JPEG image file
    content = gobble_file(filename, binary=True)
    http_header(conn, 'Content-Type: image/jpeg')
    http_header(conn, 'Accept-Ranges: bytes')
    http_body(conn, content)


def deliver_ico(conn, filename):
    # Deliver content of ICON image file
    content = gobble_file(filename, binary=True)
    http_header(conn, 'Content-Type: image/x-icon')
    http_header(conn, 'Accept-Ranges: bytes')
    http_body(conn, content)


def http_header(connection_socket, header_line):
    # Send the header line as string instance
    connection_socket.send((header_line + '\r\n').encode())


def http_body(connection_socket, payload):
    # Send payload as byte string
    connection_socket.send('\r\n'.encode())
    connection_socket.send(payload)


def http_status(conn, status):
    # Send status line
    conn.send(('HTTP/1.1 ' + status + '\r\n').encode())


def deliver_200(connection_socket):
    # Send 200 OK Status response
    http_status(connection_socket, '200 OK')


def deliver_404(connection_socket):
    # Send 404 not found status response
    http_status(connection_socket, '404 Not Found')
