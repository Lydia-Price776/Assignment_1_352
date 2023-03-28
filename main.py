import _thread
import socket

import delivery
from parse import *
from delivery import *


def authorised(headers):
    if 'Authorization' in headers:
        given_key = headers['Authorization']
        random, key = given_key.split(' ')
    else:
        return False
    auth_key = 'MjAwMDQ1MjE6MjAwMDQ1MjE='
    if key == auth_key:
        return True
    else:
        return False


def get_filename(path):
    match path.strip('/'):
        case '':
            return 'index.html'
        case 'form':
            return 'psycho.html'
        case _:
            return None


def do_request(connection_socket):
    request = connection_socket.recv(10240)
    httpr = parse_http_request(request)

    # if authorised() access content
    # else authorise?
    if authorised(httpr.headers):
        print(httpr.cmd, httpr.path)

        filename = get_filename(httpr.path)
        if filename is not None:
            filetype = filename.split('.').pop()

        if filetype == 'html':
            delivery.deliver_html(connection_socket, 'index.html')
        elif httpr.path == '/form':
            delivery.deliver_html(connection_socket, 'psycho.html')

    else:
        connection_socket.send(b'HTTP/1.1 401 Unauthorised\r\n')
        connection_socket.send(b'WWW-Authenticate: Basic realm="Web 159352"')

    connection_socket.close()


def main(port):
    # Create the server socket object
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the server socket to the port
    my_socket.bind(('', port))

    # Start listening for new connections
    my_socket.listen()
    print("The server is ready to receive messages on port: ", server_port)

    while True:
        # Accept a message from the client
        connection_socket, addr = my_socket.accept()

        # Handle each connection in a separate thread
        _thread.start_new_thread(do_request, (connection_socket,))


if __name__ == '__main__':
    server_port = 8080
    main(server_port)
