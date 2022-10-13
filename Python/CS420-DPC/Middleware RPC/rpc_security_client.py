from xmlrpc.client import ServerProxy
import json
import sys

if __name__ == "__main__":

    name = sys.argv[1]
    item = sys.argv[2]

    rpcClient = ServerProxy('http://169.254.213.62:8000')

    msg = rpcClient.isAllowedIn(name, item)

    isAllowed = True if msg['request'] == 'accepted' else False
    print('{} is allowed in to {}: {}'.format(name, item, isAllowed))

    msg = rpcClient.allowedItems(name)
    print(msg)
