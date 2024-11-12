
# Socket Programming Client-Server Project

This project demonstrates basic socket programming using TCP and UDP protocols in Python. The project includes the following four Python scripts:

- **TCP Server** (`tcp_server.py`): A server that listens for TCP client connections, receives messages, and responds with the uppercase version of the message.
- **TCP Client** (`tcp_client.py`): A client that connects to a TCP server, sends messages, and receives modified responses.
- **UDP Server** (`udp_server.py`): A server that listens for UDP client messages and sends back the uppercase version of the message.
- **UDP Client** (`udp_client.py`): A client that sends messages to a UDP server and receives modified responses.

## Project Structure

```
/SocketProgramming
│
├── tcp_server.py          # TCP server script
├── tcp_client.py          # TCP client script
├── udp_server.py          # UDP server script
└── udp_client.py          # UDP client script
```

## Requirements

- Python 3.x
- No external libraries required

## Instructions

### 1. TCP Server and Client

#### **Running the TCP Server:**
1. Open a terminal and navigate to the directory containing the `tcp_server.py` file.
2. Run the server with the following command:
   ```bash
   python tcp_server.py
   ```
   The server will start listening for incoming client connections.

#### **Running the TCP Client:**
1. In another terminal window, navigate to the directory containing the `tcp_client.py` file.
2. Run the client with the following command:
   ```bash
   python tcp_client.py
   ```
   The client will connect to the server, send messages, and receive modified responses.

### 2. UDP Server and Client

#### **Running the UDP Server:**
1. Open a terminal and navigate to the directory containing the `udp_server.py` file.
2. Run the server with the following command:
   ```bash
   python udp_server.py
   ```
   The server will start listening for UDP client messages.

#### **Running the UDP Client:**
1. In another terminal window, navigate to the directory containing the `udp_client.py` file.
2. Run the client with the following command:
   ```bash
   python udp_client.py
   ```
   The client will send messages to the server and receive modified responses.

## Code Explanation

### **TCP Server (`tcp_server.py`):**
- Creates a TCP server socket using `socket.AF_INET` and `socket.SOCK_STREAM`.
- Binds the socket to the specified IP and port.
- Waits for a client to connect, accepts the connection, and then waits for messages.
- For each received message, the server sends back the uppercase version of the message.
- The server will close the connection once the client disconnects or sends an empty message.

### **TCP Client (`tcp_client.py`):**
- Creates a TCP client socket and connects to the server using `socket.connect()`.
- Sends user input messages to the server.
- Receives and prints the server's modified response (uppercase version of the sent message).
- Closes the connection when the user types "exit".

### **UDP Server (`udp_server.py`):**
- Creates a UDP server socket using `socket.AF_INET` and `socket.SOCK_DGRAM`.
- Binds the socket to the specified IP and port.
- Waits for incoming messages from clients.
- For each received message, the server sends back the uppercase version of the message.
- The server continues to run until stopped manually.

### **UDP Client (`udp_client.py`):**
- Creates a UDP client socket.
- Sends user input messages to the server and waits for a response.
- Receives the server's modified response (uppercase version of the sent message).
- The client continues to send messages until the user types "exit".

## Example Usage

### **TCP Example**:
1. Start the TCP server:
   ```bash
   python tcp_server.py
   ```
2. In a new terminal, start the TCP client:
   ```bash
   python tcp_client.py
   ```
3. Input a message on the client:
   ```
   Enter your message: hello
   ```
   The client will receive the server's response:
   ```
   "HELLO" has been sent
   ```

### **UDP Example**:
1. Start the UDP server:
   ```bash
   python udp_server.py
   ```
2. In a new terminal, start the UDP client:
   ```bash
   python udp_client.py
   ```
3. Input a message on the client:
   ```
   Enter your message: hello
   ```
   The client will receive the server's response:
   ```
   "HELLO" has been sent
   ```

## Conclusion

This project demonstrates how to use Python's socket module to implement simple client-server communication using both TCP and UDP protocols. It provides a solid foundation for learning about network programming and can be expanded for more complex applications.

