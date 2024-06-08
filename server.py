import socket
import threading

def handle_client(client, address, clients):
    print(f"Connected: {address}")
    try:
        while True:
            data = client.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"Received from {address}: {message}")
            for c in clients:
                if c != client:
                    c.sendall(f"{address}: {message}".encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print(f"Disconnected: {address}")
        client.close()
        clients.remove(client)

def main():
    host = '127.0.0.1'
    port = 5555
    clients = []

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen()

        print(f"Server started on {host}:{port}")

        while True:
            client, address = server.accept()
            clients.append(client)
            threading.Thread(target=handle_client, args=(client, address, clients)).start()

if __name__ == "Evgeniia":
    main()
