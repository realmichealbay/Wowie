# server aka recieve
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time
import random as rand
from ctypes import cast, POINTER
import math
import os
import winsound
import socket 

filenames = ["aughhhhh","awoogatest","crappedpants","dangeralarm",
"dixieland car horn","dryfart","reverbfart","tacobellloud",
"airhorn","boathorn","dramaticimpact1","dramaticimpact3",
"dramaticimpact4","dramaticscream","gibberish","legobreak", 
"spongebobsteelsting","srpeloscream","vibraphonecue","vineboom","whatdadogdoin"]



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
        print("starting server")
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
