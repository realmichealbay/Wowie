import time
import random as rand
from ctypes import cast, POINTER
import math
import os
import winsound
filenames = ["aughhhhh","awoogatest","crappedpants","dangeralarm",
"dixieland car horn","dryfart","reverbfart","tacobellloud",
"airhorn","boathorn","dramaticimpact1","dramaticimpact3",
"dramaticimpact4","dramaticscream","gibberish","legobreak", 
"spongebobsteelsting","srpeloscream","vibraphonecue","vineboom","whatdadogdoin"]

def run():
    for x in range(5):
        winsound.Beep(3000,50)
run()

time.sleep(30)

# import libraries
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from playsound import playsound
import mouse

# get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
os.chdir(os.path.dirname(os.path.realpath(__file__))) # changes directory to the current folder to play sounds from
count = 0 # count that will increase for each fart (or sound) played, in case we have a set designated amount

def repeat():
    currentVolumeDb = volume.GetMasterVolumeLevel() # get the computer's current volume
    mouse.move(rand.randint(-2000,2000),rand.randint(-2000,2000),absolute=False,duration=0.01) # move the mouse
    volume.SetMasterVolumeLevel(-2.0, None) # sets the volume to max
    volume.SetMute(0, None) #unmutes the computer so you cannot escape it
    #playsound(filenames[rand.randint(0,len(filenames)-1)]) # plays the sound
    winsound.PlaySound(filenames[rand.randint(0,len(filenames)-1)], winsound.SND_LOOP)
    repeat()
repeat()