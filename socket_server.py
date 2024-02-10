import socket

def server_program():
    host = socket.gethostname
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    #how many clients are listening
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("from sonnected user: " +str(data))
        data = input('->')
        conn.send(data.encoded())

    conn.close()