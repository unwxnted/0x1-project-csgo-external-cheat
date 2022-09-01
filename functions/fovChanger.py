import pymem
import pymem.process
from offsets.offsets import *

def fovChanger(pm, client, engine, enginePointer, fovValue, status):
    player = pm.read_int(client + dwLocalPlayer)
    localTeam = pm.read_int(player + m_iTeamNum)

    if(status):
        pm.write_int(player + m_iFOV, fovValue)
    else:
        pm.write_int(player + m_iFOV, 69)