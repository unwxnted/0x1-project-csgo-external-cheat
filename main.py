#dependencies
import os
import pymem
import pymem.process
import keyboard
import time
import random
import threading

# config
from config import *

#functions
from functions.manager import *
from functions.aimbot import *
from functions.bhop import *
from functions.triggerbot import *
from functions.glow import *
from functions.chams import *
from functions.rcs import *
from functions.junkcode import *
from functions.fovChanger import *
from functions.noFlash import *

#offsets
from offsets.autoUpdater import *
from offsets.offsets import *

os.system("wmic process where processid=\""+str(os.getpid())+"\" CALL   setpriority \"high priority\"")

os.system("cls")
print("[0x1]: Generating new junkcode, if not initialize please try again...")
junkcode()

print("[0x1]: Updating offets...")
update()

glowActive = False
chamsActive = False
rcsActive = False
aimActive = False
fovActive = False
noFlashActive = False


class main():
    def __init__(self):
        self.pm = pymem.Pymem("csgo.exe")
        self.client = pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll
        self.engine = pymem.process.module_from_name(self.pm.process_handle, "engine.dll").lpBaseOfDll
        self.enginePointer = self.pm.read_uint(self.engine + dwClientState)
    
    def UI(self):
        os.system("cls")
        print("Welcome to 0x1")
        print("Coded by: weakness#0054")
        print("\n \nHotkeys:")
        print("----------[Hold]----------")
        print("Bhop and autoStrafe: Space")
        print("TriggerBot: "+ triggerKey + "\n")
        print("----------[Toggle]----------")
        print("FovChanger: F1")
        print("NoFlash: F2")
        print("Glow: F6")
        print("Chams visible: F7")
        print("RCS: F8")
        print("Aimbot: F9, " + aimKey + " key to use")
        print("\n----------[Console]----------")
        print("\n \nLogs:")

    def UpdateUI(self, hackActive, hackName):
        if hackActive:
            time.sleep(0.1)
            return print("[0x1]: " + hackName + " is active")
        time.sleep(0.1)
        return print("[0x1]: " + hackName + " is not active")



    def activator(self, hackActive, key, hackName):
        if(keyboard.is_pressed(key)):
            self.UpdateUI(not hackActive, hackName)
            if(hackActive == True):
                return False
            else:
                return True
        
        return hackActive
            
            
    def mainLoop(self):
        global glowActive
        global chamsActive
        global rcsActive
        global aimActive
        global fovActive
        global noFlashActive
        self.UI()

        def misc():
            bhop(self.pm, self.client, self.engine, self.enginePointer, autoStrafe)
            trigger(self.pm, self.client, self.engine, self.enginePointer, triggerbotDelay, triggerKey)

        while True:
            
            if(manager(self.pm, self.client, self.engine, self.enginePointer)):

                threading.Thread(target=misc, name='misc', daemon=True).start()

                fovActive = self.activator(fovActive, "F1", "FovChanger")
                if(fovActive):
                    fovChanger(self.pm, self.client, self.engine, self.enginePointer, fovValue)
                    fovActive = False
                
                noFlashActive = self.activator(noFlashActive, "F2", "NoFlash")
                if(noFlashActive):
                    noFlash(self.pm, self.client, self.engine, self.enginePointer, True)
                    noFlashActive = False
                
                glowActive = self.activator(glowActive, "F6", "Glow")
                if(glowActive):
                    glow(self.pm, self.client, self.engine, self.enginePointer, glowColor)
                
                rcsActive = self.activator(rcsActive, "F8", "RCS")
                if(rcsActive):
                    rcs(self.pm, self.client, self.engine, self.enginePointer)
                
                chamsActive = self.activator(chamsActive, "F7", "Chams")
                if(chamsActive):
                    chams(self.pm, self.client, self.engine, self.enginePointer, colorChams, chamsbrightness)
                
                aimActive = self.activator(aimActive, "F9", "Aimbot")
                if(aimActive):
                    aimbot(self.pm, self.client, self.engine, self.enginePointer, aimfov, bone, autoShot, aimKey, aimDelay)
            


try:
    program = main()
    program.mainLoop()
except Exception as err:
    print(err)