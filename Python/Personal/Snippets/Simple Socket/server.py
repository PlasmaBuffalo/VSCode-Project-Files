# from https://realpython.com/python-sockets/#tcp-sockets
import socket


class Server():

    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 8000  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print('Bound socket to ip='+HOST+' on port='+str(PORT))
        s.listen()
        print('Socket now listening for new connections')
        conn, addr = s.accept()
        print('Socket accepted connection at conn='+str(conn)+' at address='+str(addr))
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
