# microservices is a design pattern
# break a complex system into smaller parts
# each part solves a single problem
# each service then interacts with each other service
# this makes the whole operation
# Each part of the whole is run in its OWN copy of Python
import socket # this lets us make clients and services

def MyServer():
    '''This microservice will receive request from clients'''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    config_t = ('localhost', 9874)
    server.bind(config_t) # our server knows which IP address and port is should use
    server.listen() # our server begins listening for requests
    # we need our serve to continue indefinitely - a run loop
    while True:
        # begin responding  to requests
        (client, addr) = server.accept()
        # print(client, addr) # not actually useful - except debug
        # echo back whatever the client sent as an upper-case string
        buf = client.recv(1024) # the first 1024 bytes of the request
        # break
        resp = buf.decode().upper() # force to upper case
        print(f'Server received {buf} and will send {resp}')
        client.send(resp.encode())

if __name__ == '__main__':
    MyServer()