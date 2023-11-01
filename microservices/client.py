import socket

def MyClient():
    '''make requests to our microservice'''
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # must match server
    config_t = ('localhost', 9874) # IP and port
    cli.connect(config_t)
    # send a message ot the server
    msg = 'hello'
    cli.send(msg.encode()) # we are obliged to encode anything passed over http

if __name__ == '__main__':
    MyClient()