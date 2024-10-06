import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))
    print("UDP Server is listening on port 12345...")

    while True:
        message, addr = server_socket.recvfrom(1024)
        message = message.decode('utf-8')
        print(f"Received from {addr}: {message}")
        response = f"Server received: {message}"
        server_socket.sendto(response.encode('utf-8'), addr)

if __name__ == "__main__":
    udp_server()
