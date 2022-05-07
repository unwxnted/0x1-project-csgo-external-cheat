import pymem
import pymem.process
from offsets.offsets import *

def chams(pm, client, engine, enginePointer, color):
    for i in range(32):
        entity = pm.read_int(client + dwEntityList + i * 0x10)

        if entity:
            entity_team_id = pm.read_int(entity + m_iTeamNum)
            entityTeamID = pm.read_int(entity + m_iTeamNum)
            entityGlow = pm.read_int(entity + m_iGlowIndex)
            player = pm.read_int(client + dwLocalPlayer)
            playerTeam = pm.read_int(player + m_iTeamNum)

            if (entity_team_id != playerTeam):
                pm.write_int(entity + m_clrRender, (color[0]))
                pm.write_int(entity + m_clrRender + 0x1, (color[1]))
                pm.write_int(entity + m_clrRender + 0x2, (color[2]))
                                     
        else:
            pass