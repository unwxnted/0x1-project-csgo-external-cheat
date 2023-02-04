import pymem
import pymem.process
import mouse
from offsets.offsets import *

def rcs(pm, client, engine, enginePointer):
    player = pm.read_int(client + dwLocalPlayer)
    Punch_x = pm.read_float(player + m_aimPunchAngle)
    Punch_y = pm.read_float(player + m_aimPunchAngle + 0x4)
    ShotsFired = pm.read_int(player + m_iShotsFired)
    global old_aim_punch_x
    global old_aim_punch_y

    if ShotsFired >= 1:
        ClientState = pm.read_int(engine + dwClientState)
        curr_view_angles_x = pm.read_float(enginePointer + dwClientState_ViewAngles)
        curr_view_angles_y = pm.read_float(enginePointer + dwClientState_ViewAngles + 0x4)
        new_view_angles_x = ((curr_view_angles_x + old_aim_punch_x) - (Punch_x * float(2)))
        new_view_angles_y = ((curr_view_angles_y + old_aim_punch_y) - (Punch_y * float(2)))

        while new_view_angles_y > 180:
            new_view_angles_y -= 360

        while new_view_angles_y < -180:
            new_view_angles_y += 360

        if new_view_angles_x > 89.0:
            new_view_angles_x = 89.0

        if new_view_angles_x < -89.0:
            new_view_angles_x = -89.0

        old_aim_punch_x = Punch_x * float(2)
        old_aim_punch_y = Punch_y * float(2)

        pm.write_float(enginePointer + dwClientState_ViewAngles, new_view_angles_x)
        mouse.move(int(new_view_angles_x), int(new_view_angles_y), absolute=False, duration=0.001)
        pm.write_float(enginePointer + dwClientState_ViewAngles + 0x4, new_view_angles_y)
    else:
        old_aim_punch_x = old_aim_punch_y = 0