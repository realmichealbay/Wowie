# client 
import time
import json
import socket
import os
import platform
import prompt_toolkit
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import CompleteStyle


with open("E:/Nuclear_Silo/ips.json", "r") as file:
    ip_addresses = json.load(file)

ip_completer = WordCompleter(ip_addresses.keys(),ignore_case=True)

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

    while True:
        clear_screen()
        print_ip(ip_addresses)
        print("-----------------Select ip---------------")
        ip = prompt(": ",completer=ip_completer,complete_style=CompleteStyle.MULTI_COLUMN)
        host = ip_addresses.get(ip)
        if host == None:
            continue
        port = 8005
        while True:
            print("Send Command")
            data = input(": ")
            data = "CMD:"+data
            print(data)
            try:  
                send_data(host,port,data)
                break
            except Exception as Error:
                print(f"Failed to send: {data}, {host} @ {port}")
                time.sleep(2)
                break
            
