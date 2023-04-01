# client 
import socket
import os
import platform

filenames = ["aughhhhh","awoogatest","crappedpants","dangeralarm",
"dixieland car horn","dryfart","reverbfart","tacobellloud",
"airhorn","boathorn","dramaticimpact1","dramaticimpact3",
"dramaticimpact4","dramaticscream","gibberish","legobreak", 
"spongebobsteelsting","srpeloscream","vibraphonecue","vineboom","whatdadogdoin"]

ip_addresses = {
    "jacob":"10.35.42.176",
    "loopback":"127.0.0.1"
}

def clear_screen():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")
        
def print_ip(list):
    for key, value in list.items():
        print(key, value)
def printfilenames(list):
    for item in list:
        print(item)

def send_data(host,port,data):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host,port))
        client_socket.sendall(data.encode())
        response = client_socket.recv(1024).decode()
        print(response)

if __name__ == "__main__":
    clear_screen()
    print_ip(ip_addresses)
    print("-----------------Select ip---------------")
    ip = input(":")
    host = ip_addresses.get(ip)
    port = 8005
    clear_screen()
    print("-----------------Options-----------------")
    printfilenames(filenames)
    print("random")
    print("-----------------------------------------")
    data = input("Choice: ")
    send_data(host,port,data)

