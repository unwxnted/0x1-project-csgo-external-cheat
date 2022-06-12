import pymem
import time
import pymem.process
from offsets.offsets import *

def fakelag(fakelagActive, fakelagDelay,pm, client, engine, enginePointer):
    if fakelagActive:
        pm.write_bool(engine +dwbSendPackets, False)
        time.sleep(fakelagDelay)
        pm.write_bool(engine +dwbSendPackets, True)
    else:
        pm.write_bool(engine +dwbSendPackets, True)
