import os
import pymem
import pymem.process
import keyboard
import time
import math
import re


# offsets

dwClientState = (0x588FEC)
dwClientState_GetLocalPlayer = (0x180)
dwClientState_IsHLTV = (0x4D48)
dwClientState_Map = (0x28C)
dwClientState_MapDirectory = (0x188)
dwClientState_MaxPlayer = (0x388)
dwClientState_PlayerInfo = (0x52C0)
dwClientState_State = (0x108)
dwClientState_ViewAngles = (0x4D90)
clientstate_delta_ticks = (0x174)
clientstate_last_outgoing_command = (0x4D2C)
clientstate_choked_commands = (0x4D30)
clientstate_net_channel = (0x9C)
dwEntityList = (0x4DA215C)
dwForceAttack = (0x31D2690)
dwForceAttack2 = (0x31D269C)
dwForceBackward = (0x31D26CC)
dwForceForward = (0x31D26A8)
dwForceJump = (0x524BF4C)
dwForceLeft = (0x31D26C0)
dwForceRight = (0x31D26E4)
dwGameDir = (0x627780)
dwGameRulesProxy = (0x52BF23C)
dwGetAllClasses = (0xDB0FC4)
dwGlobalVars = (0x588CF0)
dwGlowObjectManager = (0x52EA5D0)
dwInput = (0x51F3720)
dwInterfaceLinkList = (0x945514)
dwLocalPlayer = (0xD892CC)
dwMouseEnable = (0xD8EE18)
dwMouseEnablePtr = (0xD8EDE8)
dwPlayerResource = (0x31D0A10)
dwRadarBase = (0x51D6ED4)
dwSensitivity = (0xD8ECB4)
dwSensitivityPtr = (0xD8EC88)
dwSetClanTag = (0x8A1B0)
dwViewMatrix = (0x4D93A74)
dwWeaponTable = (0x51F41E0)
dwWeaponTableIndex = (0x325C)
dwYawPtr = (0xD8EA78)
dwZoomSensitivityRatioPtr = (0xD93D18)
dwbSendPackets = (0xD76DA)
dwppDirect3DDevice9 = (0xA7050)
m_pStudioHdr = (0x294C)
m_yawClassPtr = (0xD8EA78)
m_pitchClassPtr = (0x51D7170)
interface_engine_cvar = (0x3E9EC)
convar_name_hash_table = (0x2F0F8)
m_bDormant = (0xED)
model_ambient_min = (0x58C064)
set_abs_angles = (0x1E0B80)
set_abs_origin = (0x1E09C0)
is_c4_owner = (0x3BCB10)
force_update_spectator_glow = (0x3AFECA)
anim_overlays = (0x2980)
m_flSpawnTime = (0xA370)
find_hud_element = (0x249EF980)

#--------------------------
#Netvars
#--------------------------

m_ArmorValue = (0xB37C)
m_Collision = (0x320)
m_CollisionGroup = (0x474)
m_Local = (0x2FBC)
m_MoveType = (0x25C)
m_OriginalOwnerXuidHigh = (0x31C4)
m_OriginalOwnerXuidLow = (0x31C0)
m_aimPunchAngle = (0x302C)
m_aimPunchAngleVel = (0x3038)
m_bGunGameImmunity = (0x3944)
m_bHasDefuser = (0xB38C)
m_bHasHelmet = (0xB370)
m_bInReload = (0x32A5)
m_bIsDefusing = (0x3930)
m_bIsScoped = (0x3928)
m_bSpotted = (0x93D)
m_bSpottedByMask = (0x980)
m_dwBoneMatrix = (0x26A8)
m_fAccuracyPenalty = (0x3330)
m_fFlags = (0x104)
m_flFallbackWear = (0x31D0)
m_flFlashDuration = (0xA420)
m_flFlashMaxAlpha = (0xA41C)
m_flNextPrimaryAttack = (0x3238)
m_hActiveWeapon = (0x2EF8)
m_hMyWeapons = (0x2DF8)
m_hObserverTarget = (0x338C)
m_hOwner = (0x29CC)
m_hOwnerEntity = (0x14C)
m_iAccountID = (0x2FC8)
m_iClip1 = (0x3264)
m_iCompetitiveRanking = (0x1A84)
m_iCompetitiveWins = (0x1B88)
m_iCrosshairId = (0xB3E8)
m_iEntityQuality = (0x2FAC)
m_iFOVStart = (0x31E8)
m_iFOV = (0x31E4)
m_iGlowIndex = (0xA438)
m_iHealth = (0x100)
m_iItemDefinitionIndex = (0x2FAA)
m_iItemIDHigh = (0x2FC0)
m_iObserverMode = (0x3378)
m_iShotsFired = (0xA390)
m_iState = (0x3258)
m_iTeamNum = (0xF4)
m_lifeState = (0x25F)
m_nFallbackPaintKit = (0x31C8)
m_nFallbackSeed = (0x31CC)
m_nFallbackStatTrak = (0x31D4)
m_nForceBone = (0x268C)
m_nTickBase = (0x3430)
m_rgflCoordinateFrame = (0x444)
m_szCustomName = (0x303C)
m_szLastPlaceName = (0x35B4)
m_vecOrigin = (0x138)
m_vecVelocity = (0x114)
m_vecViewOffset = (0x108)
m_viewPunchAngle = (0x3020)
m_thirdPersonViewAngles = (0x31D8)
m_clrRender = (0x70)
m_flC4Blow = (0x2990)
m_flTimerLength = (0x2994)
m_flDefuseLength = (0x29A8)
m_flDefuseCountDown = (0x29AC)
cs_gamerules_data = (0x0)
m_SurvivalRules = (0xD00)
m_SurvivalGameRuleDecisionTypes = (0x1328)
m_bIsValveDS = (0x7C)
m_bFreezePeriod = (0x20)
m_bBombPlanted = (0x9A5)
m_bIsQueuedMatchmaking = (0x74)
m_flSimulationTime = (0x268)
m_flLowerBodyYawTarget = (0x3A90)
m_angEyeAnglesX = (0xB380)
m_angEyeAnglesY = (0xB384)
m_flNextAttack = (0x2D70)
m_iMostRecentModelBoneCounter = (0x2690)
m_flLastBoneSetupTime = (0x2924)
m_bStartedArming = (0x33F0)
m_bUseCustomBloomScale = (0x9DA)
m_bUseCustomAutoExposureMin = (0x9D8)
m_bUseCustomAutoExposureMax = (0x9D9)
m_flCustomBloomScale = (0x9E4)
m_flCustomAutoExposureMin = (0x9DC)
m_flCustomAutoExposureMax = (0x9E0)



# with this you can change the file hash
antivac1 = "85839552263df67e724a2d38519247e2" # change this 
antivac2 = 32740525034503245034873407523400355400100213487323 # change this 
antivac3 = ["af54eae5714cd8107f886b1659f2138e", 2151253|243, 21347631241243, 2159381251235423253215,  2319659126518275608194, 92154361023] # change this 

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
enginepointer = pm.read_int(engine + dwClientState)


glowActive = False
chamsActive = False
rcsActive = False
aimActive = False
wireActive = False

aimfov = 0.8

rgbT = [255, 0, 0]
rgbCT = [0, 0, 255]




ranks = ["Unranked" , 
                "Silver I",
                "Silver II",
                "Silver III",
                "Silver IV",
                "Silver Elite",
                "Silver Elite Master",
                "Gold Nova I",
                "Gold Nova II",
                "Gold Nova III",
                "Gold Nova Master",
                "Master Guardian I",
                "Master Guardian II",
                "Master Guardian Elite",
                "Distinguished Master Guardian",
                "Legendary Eagle",
                "Legendary Eagle Master",
                "Supreme Master First Class",
                "The Global Elite"]


def rankRevealer():
    
        for i in range(0, 32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_i = pm.read_int(client + dwLocalPlayer)
                if entity_team_id != pm.read_int(entity_i + m_iTeamNum):
                    player_info = pm.read_int(
                        (pm.read_int(engine + dwClientState)) + dwClientState_PlayerInfo)
                    player_info_items = pm.read_int(pm.read_int(player_info + 0x40) + 0xC)
                    info = pm.read_int(player_info_items + 0x28 + (i * 0x34))
                    playerres = pm.read_int(client + dwPlayerResource)
                    rank = None
                    rank = pm.read_int(playerres + m_iCompetitiveRanking + i * 4)

                    if pm.read_string(info + 0x10) != 'GOTV':
                        
                        print("[0x1]: "  + pm.read_string(info + 0x10) + "   -->   " + ranks[rank])
                        print("------------------------------------------------------------------------------------------")




 
def calc_distance(current_x, current_y, new_x, new_y):
    distancex = new_x - current_x
    if distancex < -89:
        distancex += 360
    elif distancex > 89:
        distancex -= 360
    if distancex < 0.0:
        distancex = -distancex
 
    distancey = new_y - current_y
    if distancey < -180:
        distancey += 360
    elif distancey > 180:
        distancey -= 360
    if distancey < 0.0:
        distancey = -distancey
    return distancex, distancey
 


def normalizeAngles(viewAngleX, viewAngleY):
    if viewAngleX > 89:
        viewAngleX -= 360
    if viewAngleX < -89:
        viewAngleX += 360
    if viewAngleY > 180:
        viewAngleY -= 360
    if viewAngleY < -180:
        viewAngleY += 360
    return viewAngleX, viewAngleY
 
 

def calcangle(localpos1, localpos2, localpos3, enemypos1, enemypos2, enemypos3):
    

    delta_x = localpos1 - enemypos1
    delta_y = localpos2 - enemypos2
    delta_z = localpos3 - enemypos3
    hyp = math.sqrt(delta_x * delta_x + delta_y * delta_y + delta_z * delta_z)
    x = math.atan(delta_z / hyp) * 180 / math.pi
    y = math.atan(delta_y / delta_x) * 180 / math.pi
                    
    if delta_x >= 0.0:
        y += 180.0
    return x,y
                
    

def aimbot():
    player = pm.read_int(client + dwLocalPlayer)
    localTeam = pm.read_int(player + m_iTeamNum)
    engine_pointer = pm.read_int(engine + dwClientState)

    target = None
    olddistx = 111111111111
    olddisty = 111111111111

    for i in range(1, 32):
        entity = pm.read_int(client + dwEntityList + i * 0x10)

        if entity:
            try:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_hp = pm.read_int(entity + m_iHealth)
                entity_dormant = pm.read_int(entity + m_bDormant)
                    
            except:
                print("no players...")
                    

            if localTeam != entity_team_id and entity_hp > 0:
                entity_bones = pm.read_int(entity + m_dwBoneMatrix)
                localpos_x_angles = pm.read_float(engine_pointer + dwClientState_ViewAngles)
                localpos_y_angles = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)
                localpos1 = pm.read_float(player + m_vecOrigin)
                localpos2 = pm.read_float(player + m_vecOrigin + 4)
                localpos_z_angles = pm.read_float(player + m_vecViewOffset + 0x8)
                localpos3 = pm.read_float(player + m_vecOrigin + 8) + localpos_z_angles
                
                entitypos_x = pm.read_float(entity_bones + 0x30 * 8 + 0xC)
                entitypos_y = pm.read_float(entity_bones + 0x30 * 8 + 0x1C)
                entitypos_z = pm.read_float(entity_bones + 0x30 * 8 + 0x2C)

                X, Y = calcangle(localpos1, localpos2, localpos3, entitypos_x, entitypos_y, entitypos_z)
                newdist_x, newdist_y = calc_distance(localpos_x_angles, localpos_y_angles, X, Y)
                if newdist_x < olddistx and newdist_y < olddisty and newdist_x <= aimfov and newdist_y <= aimfov:
                    olddistx, olddisty = newdist_x, newdist_y
                    target, target_hp, target_dormant = entity, entity_hp, entity_dormant
                    target_x, target_y, target_z = entitypos_x, entitypos_y, entitypos_z
            if keyboard.is_pressed("c") and player:
                if target and target_hp > 0 and not target_dormant:
                    x, y = calcangle(localpos1, localpos2, localpos3, target_x, target_y, target_z)
                    normalize_x, normalize_y = normalizeAngles(x, y)

                    pm.write_float(engine_pointer + dwClientState_ViewAngles, normalize_x)
                    pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4, normalize_y)






def main():

    global glowActive
    global chamsActive
    global rcsActive
    global aimActive
    global wireActive
    

    os.system("cls")
    print("Welcome to 0x1")
    print("Coded by: weakness#0054")
    print("\n \n Hotkeys:")
    print("----------[Hold]----------")
    print("Bhop: Space")
    print("TriggerBot: Alt")
    print("----------[Toggle]----------")
    print("Glow: F6")
    print("Chams visible: F7")
    print("RCS: F8")
    print("Aimbot: F9, C key to use")
    print("Wireframe: F10")
    print("\n----------[Extra]----------")
    print("press n for rank reveal")
    print("\n \nLogs:")




    while True:
       
        #manager
        if client and engine and pm:
            try:
                player = pm.read_int(client + dwLocalPlayer)
                engine_pointer = pm.read_int(engine + dwClientState)
                glow_manager = pm.read_int(client + dwGlowObjectManager) 
                crosshairID = pm.read_int(player + m_iCrosshairId) 
                getcrosshairTarget = pm.read_int(client + dwEntityList + (crosshairID - 1) * 0x10)
                immunitygunganme = pm.read_int(getcrosshairTarget + m_bGunGameImmunity)
                localTeam = pm.read_int(player + m_iTeamNum)
                crosshairTeam = pm.read_int(getcrosshairTarget + m_iTeamNum)
            except:
                print("[0x1]: on menu")
                time.sleep(1)
                continue
        
        # bhop
        if keyboard.is_pressed("space"):
                force_jump = client + dwForceJump
                player = pm.read_int(client + dwLocalPlayer)
                on_ground = pm.read_int(player + m_fFlags)
        

                if player and on_ground and on_ground == 257:
                    pm.write_int(force_jump, 5)
                    time.sleep(0.06)
                    pm.write_int(force_jump, 4)
        
        
        # Trigger

        if keyboard.is_pressed("alt"):
            player = pm.read_int(client + dwLocalPlayer)
            entity_id = pm.read_int(player + m_iCrosshairId)
            entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

            entity_team = pm.read_int(entity + m_iTeamNum)
            player_team = pm.read_int(player + m_iTeamNum)

            if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                pm.write_int(client + dwForceAttack, 6)

        
        # glow

        if keyboard.is_pressed("F6") and glowActive == False:
            glowActive = True
            print("[0x1]: glow active")
            time.sleep(0.2)
        elif keyboard.is_pressed("F6") and glowActive == True:
            glowActive = False
            print("[0x1]:glow no active")
            time.sleep(0.2)

        if(glowActive):
            glowManager = pm.read_int(client + dwGlowObjectManager)

            for i in range(1, 32):

                entity = pm.read_int(client + dwEntityList + i * 0x10)

                if entity:

                    entityTeamID = pm.read_int(entity + m_iTeamNum)
                    entityGlow = pm.read_int(entity + m_iGlowIndex)
                    player = pm.read_int(client + dwLocalPlayer)
                    playerTeam = pm.read_int(player + m_iTeamNum)

                    if entityTeamID != playerTeam:
                        pm.write_float(glowManager + entityGlow * 0x38 + 0x4, float(1))
                        pm.write_float(glowManager + entityGlow * 0x38 + 0x8, float(0))
                        pm.write_float(glowManager + entityGlow * 0x38 + 0xC, float(0))
                        pm.write_float(glowManager + entityGlow * 0x38 + 0x10, float(1))
                        pm.write_int(glowManager + entityGlow * 0x38 + 0x24, 1)
                    

            

        # RCS

        if keyboard.is_pressed("F8") and rcsActive == False:
            rcsActive = True
            print("[0x1]: rcs active")
            time.sleep(0.2)
        elif keyboard.is_pressed("F8") and rcsActive == True:
            rcsActive = False
            print("[0x1]: rcs no active")
            time.sleep(0.2)

        if (rcsActive):
            Punch_x = pm.read_float(player + m_aimPunchAngle)
            Punch_y = pm.read_float(player + m_aimPunchAngle + 0x4)
            ShotsFired = pm.read_int(player + m_iShotsFired)

            if ShotsFired >= 1:
                ClientState = pm.read_int(engine + dwClientState)
                curr_view_angles_x = pm.read_float(ClientState + dwClientState_ViewAngles)
                curr_view_angles_y = pm.read_float(ClientState + dwClientState_ViewAngles + 0x4)
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

                pm.write_float(ClientState + dwClientState_ViewAngles, new_view_angles_x)
                pm.write_float(ClientState + dwClientState_ViewAngles + 0x4, new_view_angles_y)
            else:
                old_aim_punch_x = old_aim_punch_y = 0
                time.sleep(0.001)


    
        #chams

        if keyboard.is_pressed("F7") and chamsActive == False:
            chamsActive = True
            print("[0x1]: chams active")
            time.sleep(0.2)
        elif keyboard.is_pressed("F7") and chamsActive == True:
            chamsActive = False
            print("[0x1]: chams no active")
            time.sleep(0.2)

        if(chamsActive):
            try:
                #time.sleep(0.001)
                for i in range(32):
                    entity = pm.read_int(client + dwEntityList + i * 0x10)

                    if entity:
                        entity_team_id = pm.read_int(entity + m_iTeamNum)
                        entityTeamID = pm.read_int(entity + m_iTeamNum)
                        entityGlow = pm.read_int(entity + m_iGlowIndex)
                        player = pm.read_int(client + dwLocalPlayer)
                        playerTeam = pm.read_int(player + m_iTeamNum)

                        if (entity_team_id != playerTeam):
                            pm.write_int(entity + m_clrRender, (rgbT[0]))
                            pm.write_int(entity + m_clrRender + 0x1, (rgbT[1]))
                            pm.write_int(entity + m_clrRender + 0x2, (rgbT[2]))
                        
                        
                    else:
                        pass
            except Exception as error:
                print(error)


        # Rank reveal
        if keyboard.is_pressed("n"):
            rankRevealer()

        # aimbot

        if keyboard.is_pressed("F9") and aimActive == False:
            aimActive = True
            print("[0x1]: Aimbot Active")
            time.sleep(0.2)
        elif keyboard.is_pressed("F9") and aimActive == True:
            aimActive = False
            print("[0x1]: Aimbot no active")
            time.sleep(0.2)

        if (aimActive):
            aimbot()

        
        # wireframe
        

        if keyboard.is_pressed("F10") and wireActive == False:
            wireActive = True
            client2 = pymem.process.module_from_name(pm.process_handle,'client.dll')
            clientModule = pm.read_bytes(client2.lpBaseOfDll, client2.SizeOfImage)
            address = client2.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F', clientModule).start() + 2
            pm.write_uchar(address, 1)
            print("[0x1]: Wireframe Active")
        elif keyboard.is_pressed("F10") and wireActive == True:
            wireActive = False
            client2 = pymem.process.module_from_name(pm.process_handle,'client.dll')
            clientModule = pm.read_bytes(client2.lpBaseOfDll, client2.SizeOfImage)
            address = client2.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F', clientModule).start() + 2
            pm.write_uchar(address, 2)
            print("[0x1]: Wireframe no active")



if __name__ == "__main__":
    main()