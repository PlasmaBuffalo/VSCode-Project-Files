from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread


class MathFuncs():

    def __init__(self):
        pass

    def multiply(self, num1, num2):
        print('\nMultiplying numbers {} and {}'.format(num1, num2))
        result = num1 * num2
        return result

    def divide(self, num1, num2):
        print('\nDividing numbers {} and {}'.format(num1, num2))
        result = num1 / num2
        return result


if __name__ == "__main__":

    rpcServer = SimpleXMLRPCServer(('169.254.213.62', 8000))
    rpcServer.register_instance(MathFuncs())

    thread = Thread(target=rpcServer.serve_forever, args=())
    thread.start()

    print('RPC Server is running..')
