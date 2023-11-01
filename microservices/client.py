import socket

def MyClient():
    '''make requests to our microservice'''
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # must match server
    config_t = ('localhost', 9874) # IP and port
    cli.connect(config_t)
    # send a message ot the server
    msg = 'quit'
    cli.send(msg.encode()) # we are obliged to encode anything passed over http
    # we can choose to handle any respoinse from the server
    response = cli.recv(1024)
    print(f'Client received {response}') # bytes
    cli.close() # a good idea to tidy up

if __name__ == '__main__':
    MyClient()