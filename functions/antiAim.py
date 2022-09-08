import pymem
import pymem.process
import keyboard
from offsets.offsets import *
import math
import time


def antiAim(pm, client, engine, enginePointer, view):
    player = pm.read_int(client + dwLocalPlayer)
    pm.write_int(player + m_iObserverMode, 1)

    pm.write_float(enginePointer + dwClientState_ViewAngles + 0x4, view + 60.0)

    pm.write_float(enginePointer + dwClientState_ViewAngles + 0x4, view - 60.0)

    pm.write_float(enginePointer + dwClientState_ViewAngles + 0x4, view)


 