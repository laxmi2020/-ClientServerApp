import socket


def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("TCP Server is listening on port 12345...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established!")

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message.lower() == 'exit':  # Check for exit command
                break
            if not message:  # Break if the message is empty (client closed connection)
                break
            print(f"Received from client: {message}")
            response = f"Server received: {message}"
            client_socket.send(response.encode('utf-8'))

        client_socket.close()
        print(f"Connection with {addr} closed.")  # This line will execute when client disconnects

if __name__ == "__main__":
    tcp_server()
