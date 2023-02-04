import pymem
import pymem.process
from offsets.offsets import *


def noFlash(pm, client, engine, enginePointer, status):
    player = pm.read_int(client + dwLocalPlayer)
    flash_value = player + m_flFlashMaxAlpha
    if(status):
        pm.write_float(flash_value, float(0))
