import pymem
import pymem.process
import keyboard
import time
from offsets.offsets import *

def bhop(pm, client, engine, enginePointer):
    if keyboard.is_pressed("space"):
        force_jump = client + dwForceJump
        player = pm.read_int(client + dwLocalPlayer)
        on_ground = pm.read_int(player + m_fFlags)
        

        if player and on_ground and on_ground == 257:
            pm.write_int(force_jump, 5)
            time.sleep(0.06)
            pm.write_int(force_jump, 4)