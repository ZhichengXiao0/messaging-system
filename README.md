# messaging-system
a basic client-server interaction with a messaging system in Python using TCP sockets involves creating a server that listens for incoming connections and a client that can connect to the server to send and receive messages.

Running the Code:
Run the Server
Run the Client
The client will start in a new terminal tab, and you can interact with it through the terminal by inputting messages.

Observing Output:
The server terminal will display messages about incoming connections and received messages.
The client terminal will prompt you to input messages. Once you input a message, it will send it to the server, and if the server sends a message back (broadcasted from other clients), you'll see it in the client terminal.
For the communication to work properly, the server should be running before the client tries to connect. Also, ensure that there are no firewall restrictions blocking the communication on the specified port.

Always consider any necessary adjustments, especially if running on a different host or port than the default localhost and 5555.
