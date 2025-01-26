import socket
import threading

host = "127.0.0.1"
port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()
clients = []
positions = {}

def new_client(client_socket, client_address):

    global positions
    while True:
        try:
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                break
            data = data.strip()
            #player_id, positionX, positionY = map(int, data.split(","))
            #player_id = int(player_id)
            #positionX = float(positionX)
            #positionY = float(positionY)
            #player_id = len(clients) + 1
            #positions[player_id] = (positionX, positionY)
            for client in clients:
                client.sendall(str(positions).encode("utf-8"))
        except BrokenPipeError:
            clients.remove(client)
            break
    client_socket.close()
while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    thread = threading.Thread(target = new_client, args = (client_socket, client_address))
    thread.start()