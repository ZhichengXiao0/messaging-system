import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            # Receive data from the server
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print("Received:", message)
        except ConnectionResetError:
            print("Connection to the server closed")
            break

# Client configuration
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))  # Connect to the server's IP and port

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

# Main loop to send messages to the server
while True:
    message = input("Enter message: ")
    client.send(message.encode('utf-8'))
