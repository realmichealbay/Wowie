# client 
import socket

testing_ip = "127.0.0.1"
ip_addresses = {
    "jacob":"10.35.42.176"
}


def send_data(host,port,data):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host,port))
        client_socket.sendall(data.encode())
        response = client_socket.recv(1024).decode()
        print(response)

if __name__ == "__main__":
    host = testing_ip
    port = 8005
    data = input(": ")
    send_data(host,port,data)