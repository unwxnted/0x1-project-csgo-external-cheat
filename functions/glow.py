import pymem
import pymem.process
from offsets.offsets import *

def glow(pm, client, engine, enginePointer, glowColor):
    glowManager = pm.read_int(client + dwGlowObjectManager)

    for i in range(1, 32):

        entity = pm.read_int(client + dwEntityList + i * 0x10)

        if entity:

            entityTeamID = pm.read_int(entity + m_iTeamNum)
            entityGlow = pm.read_int(entity + m_iGlowIndex)
            player = pm.read_int(client + dwLocalPlayer)
            playerTeam = pm.read_int(player + m_iTeamNum)

            if entityTeamID != playerTeam:
                pm.write_float(glowManager + entityGlow * 0x38 + 0x8, float(glowColor[0]))
                pm.write_float(glowManager + entityGlow * 0x38 + 0xC , float(glowColor[1]))
                pm.write_float(glowManager + entityGlow * 0x38 + 0x10, float(glowColor[2]))
                pm.write_float(glowManager + entityGlow * 0x38 + 0x14, float(glowColor[3]))
                pm.write_int( glowManager + entityGlow * 0x38 + 0x28, 1 )