import pymem
import pymem.process
import re
from offsets.offsets import *

def wireframe(active, pm, client, engine, enginePointer):
    if active:
        client2 = pymem.process.module_from_name(pm.process_handle,'client.dll')
        clientModule = pm.read_bytes(client2.lpBaseOfDll, client2.SizeOfImage)
        address = client2.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F', clientModule).start() + 2
        pm.write_uchar(address, 1)
        print("[0x1]: Wireframe Active")
    else:
        client2 = pymem.process.module_from_name(pm.process_handle,'client.dll')
        clientModule = pm.read_bytes(client2.lpBaseOfDll, client2.SizeOfImage)
        address = client2.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F', clientModule).start() + 2
        pm.write_uchar(address, 2)
        print("[0x1]: Wireframe no active")