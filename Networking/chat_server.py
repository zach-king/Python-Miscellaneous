import socket
import select
import sys

sock_list = []

def chat_server():
    global sock_list
    buff_size = 1024
    s = socket.socket()
    s.bind(('127.0.0.1', 9000))
    s.listen(5)
    print('Server started on port 9000')

    conn, addr = s.accept()
    sock_list.append(conn)

    while True:
        
        ready_to_read, ready_to_write, in_error = select.select(sock_list, [], [], 0)

        for sock in ready_to_read:
            # A new connection
            if sock == s:
                conn, addr = s.accept()
                print('Connection from', addr)
                sock_list.append(conn)
                broadcast(s, conn, '[%s:%s] entered the network\n' % addr)
            else:
                # A message from client
                try:
                    data = sock.recv(buff_size)
                    if data:
                        broadcast(s, sock, '\r' + '[' + str(sock.getpeername()) + ']: ' + data)
                    else:
                        if sock in sock_list:
                            sock_list.remove(sock)

                        broadcast(s, sock, 'Client (%s, %s) is offline\n' % addr)
                except:
                    broadcast(s, sock, 'Client (%s, %s) is offline\n' % addr)
                    continue
    s.close()


def broadcast(server_socket, sock, message):
    global sock_list
    for socket in sock_list:
        if socket != server_socket and socket != sock:
            try:
                socket.send(message)
            except:
                socket.close()
                if socket in sock_list:
                    sock_list.remove(socket)


if __name__ == '__main__':
    sys.exit(chat_server())