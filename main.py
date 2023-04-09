import _thread
import json
import socket

from parse import *
from delivery import *


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


def do_request(connection_socket):
    request = connection_socket.recv(10240)
    http_request = parse_http_request(request)
    print(http_request.cmd, http_request.path)

    if authorised(http_request.headers):

        deliver_200(connection_socket)

        if http_request.cmd == 'GET' and http_request.path == '/':
            deliver_html(connection_socket, 'index.html')
        elif http_request.cmd == 'GET' and http_request.path == '/form':
            deliver_html(connection_socket, 'psycho.html')
        elif http_request.cmd == 'POST' and http_request.path == '/analysis':
            get_form_data(http_request)
            analyse_form_data()
        else:
            deliver_404(connection_socket)

    else:
        connection_socket.send(b'HTTP/1.1 401 Unauthorised\r\n')
        connection_socket.send(b'WWW-Authenticate: Basic realm="Web 159352"')

    connection_socket.close()


def get_form_data(http_request):
    data = parse_post(http_request.payload)
    jsonDataStr = json.dumps(data)
    jsonFile = open('user_data/user_data.json', 'w')
    jsonFile.write(jsonDataStr)
    jsonFile.close()


def analyse_form_data():
    file = open('user_data/user_data.json')
    data = json.load(file)
    file.close()
    print(type(data))
    for i in data:
        #keyword, value = item.split(':')
        print( i, data[i])



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
