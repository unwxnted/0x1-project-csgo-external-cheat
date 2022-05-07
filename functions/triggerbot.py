import pymem
import pymem.process
import keyboard
import time
from offsets.offsets import *


def trigger(pm, client, engine, enginePointer, ONdelay):
    if keyboard.is_pressed("alt"):
        player = pm.read_int(client + dwLocalPlayer)
        entity_id = pm.read_int(player + m_iCrosshairId)
        entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

        entity_team = pm.read_int(entity + m_iTeamNum)
        player_team = pm.read_int(player + m_iTeamNum)

        if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
            time.sleep(ONdelay)
            pm.write_int(client + dwForceAttack, 6)
