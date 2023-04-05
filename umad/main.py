import time
import random as rand
from ctypes import cast, POINTER
import os
import winsound

folder_path = "E:/umad/Audio"
filenames_1 = os.listdir(folder_path)
filenames = []

for file_name in filenames_1:
    filenames.append(file_name.split(".")[0])
    

def run():
    for x in range(5):
        winsound.Beep(3000,50)
run()

time.sleep(0)

# import libraries
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from playsound import playsound
import mouse

# get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def repeat():
    currentVolumeDb = volume.GetMasterVolumeLevel() # get the computer's current volume
    mouse.move(rand.randint(-2000,2000),rand.randint(-2000,2000),absolute=False,duration=0.01) # move the mouse
    volume.SetMasterVolumeLevel(-2.0, None) # sets the volume to max
    volume.SetMute(0, None) #unmutes the computer so you cannot escape it
    winsound.PlaySound("audio/" + filenames[rand.randint(0,len(filenames)-1)], winsound.SND_LOOP)
    repeat()
repeat()