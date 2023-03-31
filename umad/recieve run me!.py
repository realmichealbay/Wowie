# server aka recieve
import socket 
def process_data(data):
    if data:
        response = f"Recieved:{data}"
        return response
    return ""
def start_server(host,port):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host,port))
        server_socket.listen(1)
        print("starting server")
        while True:
            conn, addr = server_socket.accept()
            with conn:
                print("Connected by ", addr)
                data = conn.recv(1024).decode()
                if not data:
                    continue
                print("Recieved Data ",data)    
                response = process_data(data)
                conn.sendall(response.encode())

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8005
    start_server(host,port)
