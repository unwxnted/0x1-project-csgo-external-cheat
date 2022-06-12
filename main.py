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
from functions.wireframe import *
from functions.chams import *
from functions.rcs import *
from functions.junkcode import *
from functions.fakelag import *

#offsets
from offsets.autoUpdater import *
from offsets.offsets import *

os.system("wmic process where processid=\""+str(os.getpid())+"\" CALL   setpriority \"high priority\"")

os.system("cls")
print("[0x1]: Generating new junkcode, if not initialize please try again...")
junkcode()

print("[0x1]: Updating offets...")
update()

def thread1():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
    enginePointer = pm.read_uint(engine + dwClientState)
    while True:
        if(manager(pm, client, engine, enginePointer)):
                bhop(pm, client, engine, enginePointer)
                trigger(pm, client, engine, enginePointer, triggerbotDelay)

def thread2():
    glowActive = False
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
    enginePointer = pm.read_uint(engine + dwClientState)
    while True:
        if(manager(pm, client, engine, enginePointer)):
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

def thread3():
    rcsActive = False
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
    enginePointer = pm.read_uint(engine + dwClientState)
    while True:
        if(manager(pm, client, engine, enginePointer)):
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

def thread4():
    chamsActive = False
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
    enginePointer = pm.read_uint(engine + dwClientState)
    while True:
        if(manager(pm, client, engine, enginePointer)):
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
                    chams(pm, client, engine, enginePointer, colorChams)
                except Exception as error:
                    print(error)

def thread5():
    aimActive = False
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
    enginePointer = pm.read_uint(engine + dwClientState)
    while True:
        if(manager(pm, client, engine, enginePointer)):
            if keyboard.is_pressed("F9") and aimActive == False:
                aimActive = True
                print("[0x1]: Aimbot Active")
                time.sleep(0.2)
            elif keyboard.is_pressed("F9") and aimActive == True:
                aimActive = False
                print("[0x1]: Aimbot no active")
                time.sleep(0.2)

            if (aimActive):
                aimbot(pm, client, engine, enginePointer, aimfov)


def thread6():
    wireActive = False
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
    enginePointer = pm.read_uint(engine + dwClientState)
    while True:
        if(manager(pm, client, engine, enginePointer)):
            if keyboard.is_pressed("F10") and wireActive == False:
                wireActive = True
                print("[0x1]: Wireframe Active")
                wireframe(wireActive, pm, client, engine, enginePointer)
                time.sleep(0.2)
            elif keyboard.is_pressed("F10") and wireActive == True:
                wireActive = False
                print("[0x1]: Wireframe no active")
                wireframe(wireActive, pm, client, engine, enginePointer)
                time.sleep(0.2)

def thread7():
    fakelagActive = False
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
    enginePointer = pm.read_uint(engine + dwClientState)
    while True:
        if(manager(pm, client, engine, enginePointer)):
            if keyboard.is_pressed("F11") and fakelagActive == False:
                fakelagActive = True
                print("[0x1]: Fakelag Active")
                fakelag(fakelagActive, fakelagDelay,pm, client, engine, enginePointer)
                time.sleep(0.2)
            elif keyboard.is_pressed("F11") and fakelagActive == True:
                fakelagActive = False
                print("[0x1]: Fakelag no active")
                fakelag(fakelagActive, fakelagDelay, pm, client, engine, enginePointer)
                time.sleep(0.2)


def main():

    print("[0x1]: Finding csgo.exe ...")
    
    os.system("cls")
    print("Welcome to 0x1")
    print("Coded by: weakness#0054")
    print("\n \nHotkeys:")
    print("----------[Hold]----------")
    print("Bhop: Space")
    print("TriggerBot: Alt")
    print("----------[Toggle]----------")
    print("Glow: F6")
    print("Chams visible: F7")
    print("RCS: F8")
    print("Aimbot: F9, C key to use")
    print("Wireframe: F10")
    print("\n----------[Console]----------")
    print("\n \nLogs:")

    t1 = threading.Thread(target=thread1).start()
    t2 = threading.Thread(target=thread2).start()
    t3 = threading.Thread(target=thread3).start()
    t4 = threading.Thread(target=thread4).start()
    t5 = threading.Thread(target=thread5).start()
    t6 = threading.Thread(target=thread6).start()
    t7 = threading.Thread(target=thread7).start()

    print("[0x1]: Injected!")


if __name__ == "__main__":
  main()
