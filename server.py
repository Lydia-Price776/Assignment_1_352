import _thread
import socket

import json
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
    print(http_request.cmd, http_request.path)

    # Dictionary of allowed paths
    use_paths = {'/': 'HTML_Files/index.html', '/form': 'HTML_Files/psycho.html',
                 '/view/input': 'HTML_Files/input.html', '/view/profile': 'HTML_Files/profile.html'
                 }

    # If the user has been authorised, then continue
    if authorised(http_request.headers):
        # Delivers our path URI's
        if http_request.cmd == 'GET' and http_request.path in use_paths:
            deliver_200(connection_socket)
            deliver_html(connection_socket, use_paths[http_request.path])

        elif http_request.cmd == 'POST' and http_request.path == '/analysis':
            deliver_200(connection_socket)
            write_json_datafile(parse_post(http_request.payload), 'user_data/user_data.json')
            write_json_datafile(analyse_form_data(), 'user_data/analysed_data.json')
            deliver_json_string(connection_socket, '{"Status" : "Success"}')

        # The below handles other useful files/paths
        elif http_request.path == '/user_data/user_data.json':
            deliver_json_file(connection_socket, 'user_data/user_data.json')

        elif http_request.path == '/user_data/analysed_data.json':
            deliver_json_file(connection_socket, 'user_data/analysed_data.json')

        elif http_request.path == '/frontend.js':
            deliver_js(connection_socket, 'frontend.js')

        elif http_request.path.endswith('.jpg'):
            deliver_jpeg(connection_socket, http_request.path[1:])

        elif http_request.path.endswith('.gif'):
            deliver_gif(connection_socket, http_request.path[1:])

        else: # If the path doesnt match any of the above, return 404 response
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
    print("The server is ready to receive messages on port: ", server_port)

    while True:
        # Accept a message from the client
        connection_socket, addr = my_socket.accept()

        # Handle each connection in a separate thread
        _thread.start_new_thread(do_request, (connection_socket,))


if __name__ == '__main__':
    server_port = 8080
    main(server_port)
