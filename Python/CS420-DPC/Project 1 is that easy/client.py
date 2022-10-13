import sys
from xmlrpc.client import ServerProxy

if __name__ == "__main__":

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    rpcClient = ServerProxy('http://169.254.213.62:8000')

    val = rpcClient.add(num1, num2)
    print('Adding :', val)

    val = rpcClient.subtract(num1, num2)
    print('Subtracting :', val)
