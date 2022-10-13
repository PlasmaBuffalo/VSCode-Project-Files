from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread


def add(num1, num2):
    print('\nAdding numbers {} and {}'.format(num1, num2))
    result = num1 + num2
    return result


def subtract(num1, num2):
    print('\nSubtracting numbers {} and {}'.format(num1, num2))
    result = num1 - num2
    return result


if __name__ == "__main__":

    rpcServer = SimpleXMLRPCServer(('169.254.213.62', 8000))
    rpcServer.register_function(add)
    rpcServer.register_function(subtract)

    thread = Thread(target=rpcServer.serve_forever, args=())
    thread.start()

    print('RPC Server is running..')
