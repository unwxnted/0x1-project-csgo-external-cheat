#dependencies
import os
import pymem
import pymem.process
import keyboard
import time
import random
import multiprocessing

# config
from config import *

#functions
from functions.manager import *
from functions.aimbot import *
from functions.bhop import *
from functions.triggerbot import *
from functions.glow import *
from functions.wireframe import *
from functions.chams import *
from functions.rcs import *
from functions.junkcode import *
from functions.fakelag import *

#offsets
from offsets.autoUpdater import *
from offsets.offsets import *

os.system("wmic process where processid=\""+str(os.getpid())+"\" CALL   setpriority \"high priority\"")

os.system("cls")
print("[0x1]: Generating new junkcode, if not initialize please try again...")
junkcode()

print("[0x1]: Updating offets...")
update()

glowActive = False
chamsActive = False
rcsActive = False
aimActive = False
wireActive = False
fakelagActive = False


def main():
    try:

        print("[0x1]: Finding csgo.exe ...")
        pm = pymem.Pymem("csgo.exe")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
        enginePointer = pm.read_uint(engine + dwClientState)

        print("[0x1]: Injected!")

        global glowActive
        global chamsActive
        global rcsActive
        global aimActive
        global wireActive
        global fakelagActive

        os.system("cls")
        print("Welcome to 0x1")
        print("Coded by: weakness#0054")
        print("\n \nHotkeys:")
        print("----------[Hold]----------")
        print("Bhop: Space")
        print("TriggerBot: Alt")
        print("----------[Toggle]----------")
        print("Glow: F6")
        print("Chams visible: F7")
        print("RCS: F8")
        print("Aimbot: F9, C key to use")
        print("Wireframe: F10")
        print("\n----------[Console]----------")
        print("\n \nLogs:")

        while True:
        
            if(manager(pm, client, engine, enginePointer)):
                bhop(pm, client, engine, enginePointer)
                trigger(pm, client, engine, enginePointer, triggerbotDelay)

                #fakelag 
                if keyboard.is_pressed("F11") and fakelagActive == False:
                    fakelagActive = True
                    print("[0x1]: glow active")
                    time.sleep(0.2)
                elif keyboard.is_pressed("F6") and fakelagActive == True:
                    fakelagActive = False
                    print("[0x1]:glow no active")
                    time.sleep(0.2)

                if(fakelagActive):
                    fakelag(fakelagActive, fakelagDelay,pm, client, engine, enginePointer)

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
                    glow(pm, client, engine, enginePointer)

                #rcs            
                if keyboard.is_pressed("F8") and rcsActive == False:
                    rcsActive = True
                    print("[0x1]: rcs active")
                    time.sleep(0.2)
                elif keyboard.is_pressed("F8") and rcsActive == True:
                    rcsActive = False
                    print("[0x1]: rcs no active")
                    time.sleep(0.2)

                if (rcsActive):
                    rcs(pm, client, engine, enginePointer)

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
                        chams(pm, client, engine, enginePointer, colorChams)
                    except Exception as error:
                        print(error)

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
                    aimbot(pm, client, engine, enginePointer, aimfov)

                # wireframe
                if keyboard.is_pressed("F10") and wireActive == False:
                    wireActive = True
                    wireframe(wireActive, pm, client, engine, enginePointer)
                    
                elif keyboard.is_pressed("F10") and wireActive == True:
                    wireActive = False
                    wireframe(wireActive, pm, client, engine, enginePointer)
    except Exception as error:
        main()

if __name__ == "__main__":
    main()


vac456=0.2118172651523269

vac545=0.8202805792655742

vac525=0.701494955500794

vac1079=0.9431364959644583

vac995=0.6074824617625642

vac1256=0.8681784185618354

vac791=0.8496866090149517

vac812=0.3043312629138025

vac546=0.6784273534695998

vac1240=0.29073776954579067

vac1273=0.18262997869358133

vac886=0.6409849697830389

vac1164=0.8047724696449409

vac878=0.8453390932902216

vac819=0.709347945598666

vac264=0.5896377613580323

vac693=0.12183208547101088

vac84=0.7843010021410629

vac478=0.019044293230063958

vac8=0.6555242679624164

vac1086=0.014536531206693515

vac315=0.8688818179307343

vac60=0.28934429981171794

vac564=0.8471592552366675

vac695=0.6152012377361502

vac540=0.7444680187265091

vac1274=0.96716446301001

vac855=0.09233736622825484

vac607=0.38679273866955666

vac816=0.8325793925680202

vac123=0.4677301687378891

vac681=0.3049188257881743

vac54=0.06211202359259549

vac138=0.8475880211135337

vac1326=0.9516079398125386

vac611=0.7941958798862309

vac837=0.5231006567671578

vac870=0.48563541735840554

vac584=0.38642601470586313

vac113=1.1790506343256624e-05

vac88=0.2589887286361163

vac129=0.77077932160668

vac132=0.6449869042914109

vac88=0.1792828319461145

vac2=0.6628028479912725

vac878=0.3286855417754113

vac499=0.41611459347897917

vac327=0.5735394377297878

vac1322=0.7331521017786637

vac1016=0.263765204511182

vac1113=0.0635011444642275

vac1257=0.5720186966106595

vac1263=0.3629106655096618

vac265=0.8323957122316856

vac1214=0.06652438681231532

vac148=0.5130200797473315

vac498=0.426809951791826

vac111=0.34539563761868775

vac1142=0.9318422848218914

vac1027=0.03998180311463695

vac1147=0.5252435325501507

vac1166=0.20717050245176805

vac93=0.8371410950311051

vac1153=0.1998759503051868

vac44=0.8616149250871946

vac654=0.15089427672284483

vac1313=0.5364025717091073

vac254=0.5795383561025151

vac929=0.9623517935927873

vac1027=0.4051984606590464

vac1253=0.8850886469670143

vac117=0.5849191151206206

vac1265=0.9624850037650866

vac501=0.15197645717980623

vac1120=0.457140369371858

vac8=0.394366118862451

vac805=0.47631297553326424

vac1203=0.5386916994929778

vac642=0.7052841821857226

vac519=0.12792676266718306

vac972=0.4164246485674554

vac68=0.5552032538889914

vac427=0.5805328552883168

vac581=0.27042747592779226

vac1260=0.9900364052215697

vac1028=0.18228588345403185

vac544=0.8325198718576603

vac745=0.28449142654342907

vac390=0.271748326682002

vac934=0.24715902426480252

vac412=0.641950240785509

vac613=0.5373515545302242

vac181=0.09269507771734031

vac668=0.4384953752500951

vac280=0.7450197623407122

vac364=0.2663128901087486

vac228=0.9854676394592861

vac722=0.15201797653125348

vac429=0.11731305338353548

vac44=0.014345442667127117

vac444=0.8248064333125465

vac992=0.2226645990617847

vac553=0.38826987649070055

vac30=0.957487759400231

vac1315=0.4296109733523513

vac404=0.9857659503815945

vac174=0.7895776182135842

vac518=0.20263428964063068

vac423=0.00056085894117619

vac433=0.3132663754698294

vac977=0.8680687913411277

vac658=0.521068268160579

vac1118=0.26813987785538906

vac146=0.44337605923414236

vac71=0.158567881779486

vac759=0.3878705886812497

vac515=0.2655295129274293

vac256=0.8092146392961527

vac724=0.6622051086685129

vac584=0.7131275030876372

vac7=0.04090738289828

vac490=0.01824744866417105

vac490=0.45476256047748176

vac110=0.08313469930518413

vac673=0.032648206646905265

vac577=0.17383734822126862

vac82=0.139784943196693

vac340=0.7656812113647244

vac559=0.45628539947315405

vac111=0.17832901820370428

vac217=0.30574542642614444

vac975=0.32400066716585285

vac1022=0.4529072548850771

vac618=0.38921824421022133

vac719=0.26226995190663527

vac938=0.5528378549610872

vac1289=0.6569743195780936

vac543=0.49448062860517206

vac261=0.6075035301350917

vac350=0.750998720539963

vac506=0.6701525735619704

vac83=0.7360287790853851

vac1063=0.07250724861492441

vac781=0.04458279240182794

vac463=0.1673828817368157

vac176=0.30488076589771707

vac686=0.22128142408647444

vac475=0.21873780743554871

vac993=0.17351499742389953

vac23=0.09876280416331995

vac252=0.07049410356516261

vac309=0.1886497164836718

vac905=0.2803810019012585

vac301=0.3080567428618365

vac459=0.5069987091692489

vac951=0.5330170108003238

vac1230=0.9702839004324679

vac1184=0.1966116177551418

vac402=0.447463662960752

vac789=0.7669377874233674

vac1269=0.3038111048598199

vac793=0.2886826425069595

vac626=0.1743059896037764

vac823=0.13744078160649176

vac1256=0.3832070193533633

vac609=0.7252795345547477

vac352=0.11438460423344532

vac843=0.11910124180136361

vac391=0.8703772284332003

vac310=0.7175131615994336

vac1042=0.14865980559285485

vac222=0.5723398229950128

vac1221=0.7682047638946521

vac304=0.4965419796751289

vac261=0.6440656807967503

vac1104=0.3357160118742043

vac558=0.9473253010533961

vac1146=0.5036538523347226

vac462=0.08826732487352673

vac337=0.6647451813810181

vac410=0.7383352280332564

vac1032=0.4943848474340784

vac273=0.2393726575081453

vac626=0.5571835034632135

vac88=0.7102106862231026

vac1281=0.5391116078842643

vac125=0.558490869220404

vac1240=0.8964536747646543

vac465=0.21164436899716332

vac395=0.9482618855917906

vac274=0.47266445589582295

vac361=0.3390051261719206

vac46=0.6548571921253156

vac758=0.743654090867331

vac431=0.9257741342393362

vac759=0.263709996153497

vac821=0.3901428032933917

vac540=0.5379549293994259

vac421=0.5444694547443003

vac1014=0.32892581641882135

vac589=0.9823951018640442

vac996=0.16704832665408775

vac269=0.07787726532136408

vac1033=0.1953491343394682

vac652=0.8654878020760262

vac226=0.025405861226447835

vac88=0.499171173677466

vac1269=0.39661008817035115

vac220=0.4028449314867696

vac557=0.9509160142230701

vac592=0.06301749456981176

vac1241=0.964709023745346

vac1244=0.3350242335327259

vac215=0.02385109781364747

vac812=0.8360772671340635

vac13=0.7903063274542553

vac1181=0.7454492229507589

vac287=0.5706443047938302

vac833=0.1716160629764999

vac831=0.8323154333514667

vac217=0.07530801415064792

vac52=0.3478222922615042

vac300=0.7033665359460621

vac803=0.9509065087842412

vac139=0.5937964973914728

vac413=0.3045526708861137

vac890=0.9469666370713827

vac1290=0.9662059330082517

vac1036=0.026869880995044948

vac727=0.18604825963071936

vac551=0.4787724718788329

vac814=0.40738677280595637

vac1075=0.5572952068678193

vac186=0.6523494126594971

vac189=0.28832387866266507

vac243=0.37279971543902735

vac1285=0.9926953383910216

vac580=0.4211381209018732

vac54=0.5946724658888568

vac416=0.6191951307117848

vac1099=0.6184563957022873

vac807=0.04545017903753479

vac491=0.42879381025029384

vac842=0.6232714087607378

vac720=0.6451348864743914

vac358=0.9289756945067693

vac107=0.2268788278168935

vac840=0.5128766792644133

vac355=0.9870985543149582

vac1068=0.393731772257933

vac80=0.5432691443368225

vac23=0.5060828213372784

vac129=0.19155455306165792

vac561=0.7264865520035412

vac725=0.4335393720983939

vac712=0.7701869488274388

vac831=0.7204073296741524

vac753=0.3073800827407366

vac527=0.14359032883889478

vac523=0.003450074366911582

vac493=0.9718056218179034

vac867=0.18964246959964415

vac991=0.09337187697051585

vac858=0.7221808815382942

vac66=0.38755603380350323

vac969=0.8262883227579607
