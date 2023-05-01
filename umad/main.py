import time
import random as rand
from ctypes import cast, POINTER
import os
import winsound
from multiprocessing import Process

os.chdir(os.path.dirname(os.path.realpath(__file__)))

folder_path = "Audio/"
filenames_1 = os.listdir(folder_path)
filenames = []
for file_name in filenames_1:
    filenames.append(file_name.split(".")[0])


def run():
    for x in range(2):
        winsound.Beep(3000,50)
run()

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

def volume_1():
    while True:
        time.sleep(.5)
        print("unmuting")
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(-2.0, None)
        volume.SetMute(0, None)

#def move_mouse():
    #while True:
        #print("moving mouse")
        #time.sleep(5)
        #mouse.move(rand.randint(-2000,2000),rand.randint(-2000,2000),absolute=False,duration=0.01)

def repeat():
    while True:
        print("playing noise")
        time.sleep(rand.randint(360,2400))
        winsound.PlaySound("audio/" + filenames[rand.randint(0,len(filenames)-1)], winsound.SND_FILENAME)


def main():
    vol_process = Process(target=volume_1)
    repeat_process = Process(target=repeat)
    #mouse_process = Process(target=move_mouse)
    
    vol_process.start()
    repeat_process.start()
    #mouse_process.start()
    
    repeat_process.join()
    vol_process.join()
    #mouse_process.join()
    
    
if __name__ == "__main__":
    main()