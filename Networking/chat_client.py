import sys
import socket
import select

def chat_client():
    host = '127.0.0.1'
    port = 9000

    s = socket.socket()
    s.settimeout(2)

    # Connect to remote host
    s.connect((host, port))

    print('Connected to remote host. You can start sending messages')
    socket_list = [s]

    while True:
        msg = input('>> ').encode()
        s.send(msg)

    # while True:
    #     # Get the list sockets which are readable
    #     ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [])

    #     for sock in ready_to_read:
    #         if sock == s:
    #             # incoming message from remote server, s
    #             data = sock.recv(1024)
    #             if not data:
    #                 print('\nDisconnected from network')
    #                 sys.exit()
    #             else:
    #                 print(data)
    #         else:
    #             # User entered a message
    #             msg = sys.stdin.readline()
    #             s.send(msg)
    #             print('[Me] ', end='')                


if __name__ == '__main__':
    sys.exit(chat_client())