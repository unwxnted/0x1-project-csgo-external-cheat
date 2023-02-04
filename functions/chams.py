import pymem
import pymem.process
from offsets.offsets import *

buf = 1084227584

def chams(pm, client, engine, enginePointer, color, chamsbrightness):
    if(chamsbrightness):
        point = pm.read_int(engine + model_ambient_min - 44)
        xored = buf ^ point
        pm.write_int(engine + model_ambient_min, xored)
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