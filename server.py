import socket
import threading

# Function to handle client connections
def handle_client(client_socket, address):
    while True:
        try:
            # Receive data from the client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            print(f"Received from {address[0]}:{address[1]}: {message}")

            # Broadcast the received message to all connected clients
            broadcast(message, client_socket)

        except ConnectionResetError:
            break

    # If a client disconnects, close the socket
    print(f"Connection with {address[0]}:{address[1]} closed")
    client_socket.close()

# Function to broadcast messages to all connected clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

# Server configuration
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))  # Change the port if needed
server.listen(5)

print("Server is listening...")

clients = []

while True:
    client_socket, address = server.accept()
    print(f"Connection from {address[0]}:{address[1]} established")

    clients.append(client_socket)

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
