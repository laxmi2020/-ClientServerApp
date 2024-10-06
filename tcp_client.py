import socket

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        message = input("Enter message to send to server (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Response from server: {response}")

    client_socket.close()

if __name__ == "__main__":
    tcp_client()
