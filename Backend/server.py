"""
Lydia Price, 20004521
This is the main server component
"""
import _thread
import os
import socket

import json
import sys

from parse import *
from delivery import *
from analyse import analyse_form_data


# Authorise the user, and return true if the auth_key matches and false otherwise
def authorised(headers):
    if 'Authorization' in headers:
        given_key = headers['Authorization']
        random, key = given_key.split(' ')
    elif 'authorization' in headers:
        given_key = headers['authorization']
        random, key = given_key.split(' ')
    else:
        return False
    auth_key = 'MjAwMDQ1MjE6MjAwMDQ1MjE='
    if key == auth_key:
        return True
    else:
        return False


# Handles all requests for the server
def do_request(connection_socket):
    request = connection_socket.recv(10240)
    # Parses the request so we can use it
    http_request = parse_http_request(request)

    # If the user has been authorised, then continue
    if authorised(http_request.headers):
        # Dictionary of allowed paths
        use_paths = {'/': 'Frontend/HTML_Files/index.html', '/form': 'Frontend/HTML_Files/psycho.html',
                     '/view/input': 'Frontend/HTML_Files/input.html',
                     '/view/profile': 'Frontend/HTML_Files/profile.html'
                     }
        # Delivers our path URI's
        if http_request.cmd == 'GET' and http_request.path in use_paths:
            if os.path.exists(use_paths[http_request.path]):
                deliver_200(connection_socket)
                deliver_html(connection_socket, use_paths[http_request.path])

        elif http_request.cmd == 'POST' and http_request.path == '/analysis':
            if os.path.exists('Backend/user_data/user_data.json'):
                deliver_200(connection_socket)
                write_json_datafile(parse_post(http_request.payload), 'Backend/user_data/user_data.json')
                if os.path.exists('Backend/user_data/analysed_data.json'):
                    deliver_200(connection_socket)
                    write_json_datafile(analyse_form_data(), 'Backend/user_data/analysed_data.json')
                if os.path.exists('Frontend/HTML_Files/analysis.html'):
                    deliver_html(connection_socket, 'Frontend/HTML_Files/analysis.html')

        # The below handles other useful files/paths
        elif http_request.path == '/user_data/user_data.json':
            if os.path.exists('Backend/user_data/user_data.json'):
                deliver_json_file(connection_socket, 'Backend/user_data/user_data.json')

        elif http_request.path == '/user_data/analysed_data.json':
            if os.path.exists('Backend/user_data/analysed_data.json'):
                deliver_json_file(connection_socket, 'Backend/user_data/analysed_data.json')

        elif http_request.path == '/frontend.js':
            if os.path.exists('Frontend/frontend.js'):
                deliver_js(connection_socket, 'Frontend/frontend.js')

        elif http_request.path == '/main.css':
            if os.path.exists('Frontend/main.css'):
                deliver_css(connection_socket, 'Frontend/main.css')

        elif http_request.path.endswith('.jpg'):
            if os.path.exists(http_request.path[1:]):
                deliver_jpeg(connection_socket, http_request.path[1:])

        elif http_request.path.endswith('.gif'):
            if os.path.exists(http_request.path[1:]):
                deliver_gif(connection_socket, http_request.path[1:])

        else:  # If the path doesn't match any of the above, return 404 response
            deliver_404(connection_socket)


    else:  # Otherwise request authentication.
        connection_socket.send(b'HTTP/1.1 401 Unauthorised\r\n')
        connection_socket.send(b'WWW-Authenticate: Basic realm="Web 159352"')

    connection_socket.close()


def write_json_datafile(data, filename):
    json_data_str = json.dumps(data)
    json_file = open(filename, 'w')
    json_file.write(json_data_str)
    json_file.close()


def main(port):
    # Create the server socket object
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the server socket to the port
    my_socket.bind(('', port))

    # Start listening for new connections
    my_socket.listen()
    print("The server is ready to receive messages on port: ", port)

    while True:
        # Accept a message from the client
        connection_socket, addr = my_socket.accept()

        # Handle each connection in a separate thread
        _thread.start_new_thread(do_request, (connection_socket,))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        server_port = int(sys.argv[1])
    else:
        server_port = 8080

    main(server_port)
