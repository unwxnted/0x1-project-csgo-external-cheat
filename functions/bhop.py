import pymem
import pymem.process
import keyboard
import time
from offsets.offsets import *

def bhop(pm, client, engine, enginePointer, autoStrafe):
    oldAngle = 0
    currectAngle = pm.read_float(enginePointer + dwClientState_ViewAngles + 0x4)
    if keyboard.is_pressed("space"):
        force_jump = client + dwForceJump
        player = pm.read_int(client + dwLocalPlayer)
        on_ground = pm.read_int(player + m_fFlags)
        moveType = pm.read_int(player + m_MoveType)

        if player and on_ground and (on_ground == 257 or on_ground == 264) and moveType != 9:
            pm.write_int(force_jump, 5)
        else:
            pm.write_int(force_jump, 4)
        
        if(autoStrafe):
            if currectAngle > oldAngle:
                pm.write_int(client + dwForceLeft, 6)
            elif currectAngle < oldAngle:
                pm.write_int(client + dwForceRight, 6)
        
    oldAngle = currectAngle

