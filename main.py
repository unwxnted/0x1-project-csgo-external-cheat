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
    j1252=0.5542613309991876
    print(j1252)

    j1292=0.9461924638083895
    print(j1292)

    j850=0.37211867343007843
    print(j850)

    j743=0.13757938545836856
    print(j743)

    j22=0.16690552359232924
    print(j22)

    j882=0.7136906338614115
    print(j882)

    j259=0.3198420091824459
    print(j259)

    j399=0.39687050069676766
    print(j399)

    j888=0.9026705135136902
    print(j888)

    j902=0.7743603712662408
    print(j902)

    j849=0.837501844024223
    print(j849)

    j793=0.5029577771243116
    print(j793)

    j1308=0.705645666876606
    print(j1308)

    j329=0.6764045958754771
    print(j329)

    j390=0.9831425541819124
    print(j390)

    j649=0.5220097875777194
    print(j649)

    j1046=0.8744242396749736
    print(j1046)

    j604=0.921061152387343
    print(j604)

    j191=0.07264780040208296
    print(j191)

    j938=0.37102997590070963
    print(j938)

    j206=0.8008128695609035
    print(j206)

    j860=0.9569752111069726
    print(j860)

    j87=0.5056350222303374
    print(j87)

    j1134=0.15925434011815154
    print(j1134)

    j747=0.15048933015576438
    print(j747)

    j236=0.7265576947280799
    print(j236)

    j683=0.03998572118959598
    print(j683)

    j333=0.050863133605147715
    print(j333)

    j103=0.3405566985286337
    print(j103)

    j1035=0.1787328276183192
    print(j1035)

    j52=0.3738174813864945
    print(j52)

    j6=0.2967710251797364
    print(j6)

    j1106=0.8759096136937301
    print(j1106)

    j1135=0.5195614643901055
    print(j1135)

    j916=0.9978666709680358
    print(j916)

    j1222=0.6631305689544226
    print(j1222)

    j1164=0.3545725323264298
    print(j1164)

    j12=0.5602650863385705
    print(j12)

    j750=0.41592564758411443
    print(j750)

    j1244=0.057451202991433914
    print(j1244)

    j1091=0.8110524307389877
    print(j1091)

    j61=0.7237075169382263
    print(j61)

    j578=0.29273446742589304
    print(j578)

    j1266=0.28703118408351913
    print(j1266)

    j585=0.4570073394287748
    print(j585)

    j926=0.6856375406567711
    print(j926)

    j540=0.4147009981492519
    print(j540)

    j638=0.9109663035182067
    print(j638)

    j734=0.8010816258102353
    print(j734)

    j830=0.07299036479219334
    print(j830)

    j760=0.38366262179720656
    print(j760)

    j1061=0.14390536653785813
    print(j1061)

    j855=0.9189006347715931
    print(j855)

    j345=0.4413472024531847
    print(j345)

    j124=0.8066078973570442
    print(j124)

    j926=0.7010154215526802
    print(j926)

    j680=0.4904894099988818
    print(j680)

    j259=0.8766858235138075
    print(j259)

    j484=0.19256538135976553
    print(j484)

    j228=0.16312890950340664
    print(j228)

    j1127=0.4666342930513532
    print(j1127)

    j154=0.8269545591313044
    print(j154)

    j506=0.027979066115144224
    print(j506)

    j128=0.36698070572896246
    print(j128)

    j619=0.9239443301750716
    print(j619)

    j168=0.747143266859761
    print(j168)

    j35=0.8607247409874534
    print(j35)

    j118=0.9980720645605515
    print(j118)

    j58=0.6428142557371803
    print(j58)

    j600=0.9047781308278007
    print(j600)

    j428=0.5852255332651906
    print(j428)

    j366=0.6669165386402286
    print(j366)

    j405=0.8501770588658913
    print(j405)

    j398=0.5223256765001498
    print(j398)

    j611=0.30889556949013697
    print(j611)

    j263=0.7775891460400292
    print(j263)

    j771=0.7072632206840562
    print(j771)

    j158=0.10962190604077238
    print(j158)

    j1045=0.8745671284984459
    print(j1045)

    j198=0.5787252621984807
    print(j198)

    j468=0.2795091849369561
    print(j468)

    j1203=0.6903858422840882
    print(j1203)

    j1237=0.3409351465888284
    print(j1237)

    j341=0.4613429797399101
    print(j341)

    j232=0.9866952175962431
    print(j232)

    j1221=0.07834265613708635
    print(j1221)

    j270=0.01599594839272367
    print(j270)

    j358=0.3985890960023727
    print(j358)

    j1292=0.8462289918172115
    print(j1292)

    j479=0.35071524124336206
    print(j479)

    j459=0.5275724937466949
    print(j459)

    j71=0.7778165427202592
    print(j71)

    j568=0.7110917920106495
    print(j568)

    j1227=0.9117082365879507
    print(j1227)

    j551=0.4021199312481001
    print(j551)
