#dependencies
import os
import pymem
import pymem.process
import keyboard
import time
import random

# config
from config import *

#functions
from functions.manager import *
from functions.aimbot import *
from functions.bhop import *
from functions.triggerbot import *
from functions.glow import *
from functions.wireframe import *
from functions.chams import *
from functions.rcs import *
from functions.junkcode import *
from functions.fakelag import *
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
wireActive = False
fakelagActive = False
fovActive = False
aspectRatioActive = False
noFlashActive = False

def main():
    try:

        print("[0x1]: Finding csgo.exe ...")
        pm = pymem.Pymem("csgo.exe")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
        enginePointer = pm.read_uint(engine + dwClientState)

        print("[0x1]: Injected!")

        global glowActive
        global chamsActive
        global rcsActive
        global aimActive
        global wireActive
        global fakelagActive
        global fovActive
        global noFlashActive

        os.system("cls")
        print("Welcome to 0x1")
        print("Coded by: weakness#0054")
        print("\n \nHotkeys:")
        print("----------[Hold]----------")
        print("Bhop: Space")
        print("TriggerBot: Alt\n")
        print("----------[Toggle]----------")
        print("FovChanger: F1")
        print("NoFlash: F2")
        print("Glow: F6")
        print("Chams visible: F7")
        print("RCS: F8")
        print("Aimbot: F9, C key to use")
        print("Wireframe: F10")
        print("FakeLag: F11")
        print("\n----------[Console]----------")
        print("\n \nLogs:")

        while True:
        
            if(manager(pm, client, engine, enginePointer)):
                bhop(pm, client, engine, enginePointer)
                trigger(pm, client, engine, enginePointer, triggerbotDelay)

                #fakelag 
                if keyboard.is_pressed("F11") and fakelagActive == False:
                    fakelagActive = True
                    print("[0x1]: Fakelag active")
                    time.sleep(0.2)
                elif keyboard.is_pressed("F6") and fakelagActive == True:
                    fakelagActive = False
                    print("[0x1]:Fakelag no active")
                    time.sleep(0.2)

                if(fakelagActive):
                    fakelag(fakelagActive, fakelagDelay,pm, client, engine, enginePointer)

                # FovChanger 
                if(keyboard.is_pressed("F1") and fovActive == False):
                    fovActive = True
                    time.sleep(0.2)
                    print("[0x1]: Fov active")
                elif keyboard.is_pressed("F1") and fovActive == True:
                    fovActive = False
                    time.sleep(0.2)
                    print("[0x1]: Fov no active")
                
                if(fovActive):
                    fovChanger(pm, client, engine, enginePointer, fovValue, True)
                else:
                    fovChanger(pm, client, engine, enginePointer, fovValue, False)
                

                # NoFlash

                if(keyboard.is_pressed("F2") and noFlashActive == False):
                    noFlashActive = True
                    print("[0x1]: NoFlash active")
                    time.sleep(0.2)
                elif (keyboard.is_pressed("F2") and noFlashActive == True):
                    noFlashActive = False
                    print("[0x1]: NoFlash no active")
                    time.sleep(0.2)
                
                if(noFlashActive):
                    noFlash(pm, client, engine, enginePointer, True)
                else:
                    noFlash(pm, client, engine, enginePointer, False)

                # glow
                if keyboard.is_pressed("F6") and glowActive == False:
                    glowActive = True
                    print("[0x1]: glow active")
                    time.sleep(0.2)
                elif keyboard.is_pressed("F6") and glowActive == True:
                    glowActive = False
                    print("[0x1]:glow no active")
                    time.sleep(0.2)

                if(glowActive):
                    glow(pm, client, engine, enginePointer)

                #rcs            
                if keyboard.is_pressed("F8") and rcsActive == False:
                    rcsActive = True
                    print("[0x1]: rcs active")
                    time.sleep(0.2)
                elif keyboard.is_pressed("F8") and rcsActive == True:
                    rcsActive = False
                    print("[0x1]: rcs no active")
                    time.sleep(0.2)

                if (rcsActive):
                    rcs(pm, client, engine, enginePointer)

                #chams
                if keyboard.is_pressed("F7") and chamsActive == False:
                    chamsActive = True
                    print("[0x1]: chams active")
                    time.sleep(0.2)
                elif keyboard.is_pressed("F7") and chamsActive == True:
                    chamsActive = False
                    print("[0x1]: chams no active")
                    time.sleep(0.2)
                    
                if(chamsActive):
                    try:
                        chams(pm, client, engine, enginePointer, colorChams, chamsbrightness)
                    except Exception as error:
                        print(error)

                # aimbot
                if keyboard.is_pressed("F9") and aimActive == False:
                    aimActive = True
                    print("[0x1]: Aimbot Active")
                    time.sleep(0.2)
                elif keyboard.is_pressed("F9") and aimActive == True:
                    aimActive = False
                    print("[0x1]: Aimbot no active")
                    time.sleep(0.2)

                if (aimActive):
                    aimbot(pm, client, engine, enginePointer, aimfov, bone, autoShot)

                # wireframe
                if keyboard.is_pressed("F10") and wireActive == False:
                    wireActive = True
                    wireframe(wireActive, pm, client, engine, enginePointer)
                    
                elif keyboard.is_pressed("F10") and wireActive == True:
                    wireActive = False
                    wireframe(wireActive, pm, client, engine, enginePointer)
    except Exception as error:
        print(error)
        main()

if __name__ == "__main__":
    main()
