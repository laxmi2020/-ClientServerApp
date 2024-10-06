import socket

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Enter message to send to server (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.sendto(message.encode('utf-8'), ('localhost', 12345))
        response, addr = client_socket.recvfrom(1024)
        print(f"Response from server: {response.decode('utf-8')}")

    client_socket.close()

if __name__ == "__main__":
    udp_client()
