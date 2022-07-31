import os

import sys

import comtypes.client

import numpy as np

# set the following flag to True to attach to an existing instance of the program

# otherwise a new instance of the program will be started

AttachToInstance = False

# set the following flag to True to manually specify the path to SAP2000.exe

# this allows for a connection to a version of SAP2000 other than the latest installation

# otherwise the latest installed version of SAP2000 will be launched

SpecifyPath = True

# if the above flag is set to True, specify the path to SAP2000 below

ProgramPath = 'D:\\Computers and Structures\\SAP2000 23\\SAP2000.exe'

# full path to the model

# set it to the desired path of your model

APIPath = 'F:\\湖北襄阳体育场\\计算过程\\主体育场\\风振分析\\Models'

if not os.path.exists(APIPath):

    try:

        os.makedirs(APIPath)

    except OSError:

        pass

# create API helper object

helper = comtypes.client.CreateObject('SAP2000v1.Helper')

helper = helper.QueryInterface(comtypes.gen.SAP2000v1.cHelper)

if AttachToInstance:

    # attach to a running instance of SAP2000

    try:

        # get the active SapObject

        mySapObject = helper.GetObject("CSI.SAP2000.API.SapObject")

    except (OSError, comtypes.COMError):

        print("No running instance of the program found or failed to attach.")

        sys.exit(-1)

else:

    if SpecifyPath:

        try:

            # create an instance of the SAPObject from the specified path

            mySapObject = helper.CreateObject(ProgramPath)

        except (OSError, comtypes.COMError):

            print("Cannot start a new instance of the program from " +
                  ProgramPath)

            sys.exit(-1)

    else:

        try:

            # create an instance of the SAPObject from the latest installed SAP2000

            mySapObject = helper.CreateObjectProgID(
                "CSI.SAP2000.API.SapObject")

        except (OSError, comtypes.COMError):

            print("Cannot start a new instance of the program.")

            sys.exit(-1)

    # start SAP2000 application

    mySapObject.ApplicationStart()

# create SapModel object

SapModel = mySapObject.SapModel

f = open('F:\\湖北襄阳体育场\\计算过程\\主体育场\\inputs\\XM_id.txt', 'r')
XMid = f.read().splitlines()
f.close()
angle=0
print('Setting case...Angle=%d 300阶' % (angle*10))
# initialize model
SapModel.InitializeNewModel()
ModelPath = APIPath + os.sep + str(angle * 10) + '\\wind' + str(
    angle * 10) + '.sdb'
ret = SapModel.File.OpenFile(ModelPath)
ret = SapModel.LoadCases.ModalRitz.SetNumberModes('MODAL', 300, 1)
casename = 'WT_' + str(angle * 10)
ret = SapModel.LoadCases.ModHistLinear.SetCase(casename)
ret = SapModel.LoadCases.ModHistLinear.SetDampConstant(casename, 0.02)
MyLoadName = []
MyFunc = []
for i in range(1, 1192):
    funcname = str(angle * 10) + 'XM' + XMid[i - 1] + '_hist'
    filename = 'F:\\湖北襄阳体育场\\计算过程\\主体育场\\风振分析\\THfuncs\\' + funcname + '.txt'
    pattname = 'XM' + XMid[i - 1]
    ret = SapModel.Func.FuncTH.SetFromFile_1(funcname, filename, 0, 0, 1,
                                             2, True)
    ret = SapModel.LoadPatterns.Add(pattname, 6, 0, False)
    ret = SapModel.AreaObj.SetLoadUniform(XMid[i - 1], pattname, 1,
                                          3, False, "Local", 0)
    MyLoadName.append(pattname)
    MyFunc.append(funcname)
MyLoadType = ['Load'] * 1191
MySF = [1] * 1191
MyTF = [1] * 1191
MyAT = [0] * 1191
MyCSys = ['Global'] * 1191
MyAng = [0] * 1191
timesteps = 2400
delta_t = 0.2977
ret = SapModel.LoadCases.ModHistLinear.SetLoads(casename, 1191, MyLoadType,
                                                MyLoadName, MyFunc, MySF,
                                                MyTF, MyAT, MyCSys, MyAng)
ret = SapModel.LoadCases.ModHistLinear.SetTimeStep(casename, timesteps, delta_t)
ret = SapModel.Analyze.SetRunCaseFlag('PRESTRESS_径向索', True, False)
ret = SapModel.Analyze.SetRunCaseFlag('PRESTRESS_环向索', True, False)
ret = SapModel.Analyze.SetRunCaseFlag('MODAL', True, False)
ret = SapModel.Analyze.SetRunCaseFlag('DEAD', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('LIVE', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('LIVE_S', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('W01', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('W02', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('W03', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('W04', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('SNOW', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('T+', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('T-', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('EX', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('EY', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('EZ', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('WIND+X', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('WIND-X', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('WIND+Y', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('WIND-Y', False, False)
ret = SapModel.Analyze.SetRunCaseFlag('pres-xl', False, False)
ret = SapModel.Analyze.SetRunCaseFlag(casename, True, False)
ret = SapModel.File.Save(ModelPath)
print('Running case...Angle=%d 300阶' % (angle*10))
ret = SapModel.Analyze.RunAnalysis()
ret = SapModel.Results.Setup.SetOptionModalHist(2)
ret = SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
ret = SapModel.Results.Setup.SetCaseSelectedForOutput(casename, True)
print('Exporting results...Angle=%d 300阶' % (angle*10))
# Get LOADPOSITION group assignments
NumberItems = 0
ObjectType = []
ObjectName = []
[NumberItems, ObjectType, ObjectName,
 ret] = SapModel.GroupDef.GetAssignments('LOADPOSITION', NumberItems,
                                         ObjectType, ObjectName)
ObjectType = np.array(ObjectType, dtype=int)
ObjectName = np.array(ObjectName, dtype=str)
LOAD_areas = ObjectName[ObjectType == 5]
num_areas = np.size(LOAD_areas)

# Get joints connetted to areas
LOAD_joints = np.empty(0, dtype=str)
LOAD_joints_sep = np.empty(0, dtype=str)
area_num_joints = np.full(num_areas, np.nan, dtype=int)
for sequence in range(num_areas):
    area = LOAD_areas[sequence]
    NumberPoints = 0
    Point = []
    [NumberPoints, Point, ret] = SapModel.AreaObj.GetPoints(area, NumberPoints, Point)
    area_num_joints[sequence] = NumberPoints
    Point = np.array(Point, dtype=str)
    LOAD_joints = np.union1d(LOAD_joints, Point)
    LOAD_joints_sep = np.hstack((LOAD_joints_sep,Point))
num_joints = np.size(LOAD_joints)
#LOAD_joints = np.array(LOAD_joints, dtype=str)
ret = SapModel.GroupDef.SetGroup('LOADJOINTS',-1,True,False,False,False,False,False,False,False,False,False,False)
for joint in range(num_joints):
    ret = SapModel.PointObj.SetGroupAssign(LOAD_joints[joint], 'LOADJOINTS', False, 0)

# Get areas connetted to joints
connected_areas = []
for sequence in range(num_joints):
    joint = LOAD_joints[sequence]
    NumberItems = 0
    ObjectType = ObjectName = PointNumber = []
    [NumberItems, ObjectType, ObjectName, PointNumber,
     ret] = SapModel.PointObj.GetConnectivity(joint, NumberItems,
                                              ObjectType, ObjectName,
                                              PointNumber)
    ObjectType = np.array(ObjectType, dtype=int)
    ObjectName = np.array(ObjectName, dtype=str)
    connected_areas.append(ObjectName[ObjectType == 5])
# Get LOAD_joints results
print('  Getting joints\' acceleraions and displacements...')
# accel
NumberResults = 0
Obj = Elm = LoadCase = StepType = StepNum = U1 = U2 = U3 = R1 = R2 = R3 = []
[
    NumberResults, Obj, Elm, LoadCase, StepType, StepNum, U1, U2, U3,
    R1, R2, R3, ret
] = SapModel.Results.JointAccAbs('LOADJOINTS', 2, NumberResults, Obj, Elm,
                                 LoadCase, StepType, StepNum, U1, U2,
                                 U3, R1, R2, R3)
U1=np.array(U1)
U1=U1.reshape((num_joints,timesteps+1),order='F')[:,1:]
U2=np.array(U2)
U2=U2.reshape((num_joints,timesteps+1),order='F')[:,1:]
U3=np.array(U3)
U3=U3.reshape((num_joints,timesteps+1),order='F')[:,1:]
avg_acc=np.vstack((U1.mean(1),U2.mean(1),U3.mean(1))).T
std_acc=np.vstack((U1.std(1,ddof=1),U2.std(1,ddof=1),U3.std(1,ddof=1))).T
# disp
NumberResults = 0
Obj = Elm = LoadCase = StepType = StepNum = U1 = U2 = U3 = R1 = R2 = R3 = []
[
    NumberResults, Obj, Elm, LoadCase, StepType, StepNum, U1, U2, U3,
    R1, R2, R3, ret
] = SapModel.Results.JointDispAbs('LOADJOINTS', 2, NumberResults, Obj, Elm,
                                 LoadCase, StepType, StepNum, U1, U2,
                                 U3, R1, R2, R3)
U1=np.array(U1)
U1=U1.reshape((num_joints,timesteps+1),order='F')[:,1:]
U2=np.array(U2)
U2=U2.reshape((num_joints,timesteps+1),order='F')[:,1:]
U3=np.array(U3)
U3=U3.reshape((num_joints,timesteps+1),order='F')[:,1:]
disp_acc=np.vstack((U1.mean(1),U2.mean(1),U3.mean(1))).T
disp_acc=np.vstack((U1.std(1,ddof=1),U2.std(1,ddof=1),U3.std(1,ddof=1))).T

# Get distrubuted joint load
print('  Getting joints\' loads...')
avg_F = np.ones([num_joints, 3])
std_F = np.ones([num_joints, 3])
for seq in num_areas:
    area = LOAD_areas[seq]
    NumberResults = 0
    Obj = Elm = PointElm = LoadCase = StepType = StepNum = F1 = F2 = F3 = M1 = M2 = M3 = []
    [
        NumberResults, Obj, Elm, PointElm, LoadCase, StepType, StepNum,
        F1, F2, F3, M1, M2, M3, ret
    ] = SapModel.Results.AreaJointForceShell(area, 1, NumberResults,
                                             Obj, Elm, PointElm,
                                             LoadCase, StepType,
                                             StepNum, F1, F2, F3, M1,
                                             M2, M3)
    

for sequence in range(num_joints):
    joint = LOAD_joints[sequence]
    sum_F1 = np.zeros([2401])
    sum_F2 = np.zeros([2401])
    sum_F3 = np.zeros([2401])
    for area in connected_areas[sequence]:
        NumberResults = 0
        Obj = Elm = PointElm = LoadCase = StepType = StepNum = F1 = F2 = F3 = M1 = M2 = M3 = []
        [
            NumberResults, Obj, Elm, PointElm, LoadCase, StepType, StepNum,
            F1, F2, F3, M1, M2, M3, ret
        ] = SapModel.Results.AreaJointForceShell(area, 1, NumberResults,
                                                 Obj, Elm, PointElm,
                                                 LoadCase, StepType,
                                                 StepNum, F1, F2, F3, M1,
                                                 M2, M3)
        PointElm = np.array(PointElm, dtype=str)
        F1 = np.array(F1)
        F2 = np.array(F2)
        F3 = np.array(F3)
        sum_F1 = sum_F1 + F1[PointElm == joint]
        sum_F2 = sum_F2 + F2[PointElm == joint]
        sum_F3 = sum_F3 + F3[PointElm == joint]
    avg_F[sequence, 0] = sum_F1[1:].mean()
    std_F[sequence, 0] = sum_F1[1:].std(ddof=1)
    avg_F[sequence, 1] = sum_F2[1:].mean()
    std_F[sequence, 1] = sum_F2[1:].std(ddof=1)
    avg_F[sequence, 2] = sum_F3[1:].mean()
    std_F[sequence, 2] = sum_F3[1:].std(ddof=1)

# Get distrubuted joint load
NumberResults = 0
Obj = Elm = PointElm = LoadCase = StepType = StepNum = F1 = F2 = F3 = M1 = M2 = M3 = []
[
    NumberResults, Obj, Elm, PointElm, LoadCase, StepType, StepNum,
    F1, F2, F3, M1, M2, M3, ret
] = SapModel.Results.AreaJointForceShell('LOADPOSITION', 2, NumberResults,
                                         Obj, Elm, PointElm,
                                         LoadCase, StepType,
                                         StepNum, F1, F2, F3, M1,
                                         M2, M3)
F1=np.array(F1)
F2=np.array(F1)
F3=np.array(F1)
joint_count=0
data_count=0
jointF1_sep=np.full((np.sum(area_num_joints),timesteps+1),np.nan)
jointF2_sep=np.full((np.sum(area_num_joints),timesteps+1),np.nan)
jointF3_sep=np.full((np.sum(area_num_joints),timesteps+1),np.nan)
for seq in range(num_areas):
    n_j=area_num_joints[seq]
    for n in range(n_j):
        ind=np.arange(data_count+n,data_count+n_j*(timesteps+1),n_j)
        jointF1_sep[joint_count+n,:]=F1[ind]
        jointF2_sep[joint_count+n,:]=F2[ind]
        jointF3_sep[joint_count+n,:]=F3[ind]
    joint_count=joint_count+n_j
    data_count=data_count+n_j*(timesteps+1)

for seq in range(num_joints):
    ind=np.where(LOAD_joints==LOAD_joints_sep[seq])


jointF1=



for area in LOAD_areas:
    NumberResults = 0
    Obj = Elm = PointElm = LoadCase = StepType = StepNum = F1 = F2 = F3 = M1 = M2 = M3 = []
    [
        NumberResults, Obj, Elm, PointElm, LoadCase, StepType, StepNum,
        F1, F2, F3, M1, M2, M3, ret
    ] = SapModel.Results.AreaJointForceShell(area, 1, NumberResults,
                                             Obj, Elm, PointElm,
                                             LoadCase, StepType,
                                             StepNum, F1, F2, F3, M1,
                                             M2, M3)



ind1=np.arange(0,9601,4)
ind2=np.arange(9604,9604+9601,4)
F1=np.array(F1)
F1=np.vstack((F1[ind1],F1[ind2])).T

PointElm = np.array(PointElm, dtype=str)


# Get distrubuted joint load
print('  Getting joints\' loads...')
avg_F = np.ones([num_joints, 3])
std_F = np.ones([num_joints, 3])
for sequence in range(num_joints):
    joint = LOAD_joints[sequence]
    sum_F1 = np.zeros([2401])
    sum_F2 = np.zeros([2401])
    sum_F3 = np.zeros([2401])
    for area in connected_areas[sequence]:
        NumberResults = 0
        Obj = Elm = PointElm = LoadCase = StepType = StepNum = F1 = F2 = F3 = M1 = M2 = M3 = []
        [
            NumberResults, Obj, Elm, PointElm, LoadCase, StepType, StepNum,
            F1, F2, F3, M1, M2, M3, ret
        ] = SapModel.Results.AreaJointForceShell(area, 1, NumberResults,
                                                 Obj, Elm, PointElm,
                                                 LoadCase, StepType,
                                                 StepNum, F1, F2, F3, M1,
                                                 M2, M3)
        PointElm = np.array(PointElm, dtype=str)
        F1 = np.array(F1)
        F2 = np.array(F2)
        F3 = np.array(F3)
        sum_F1 = sum_F1 + F1[PointElm == joint]
        sum_F2 = sum_F2 + F2[PointElm == joint]
        sum_F3 = sum_F3 + F3[PointElm == joint]
    avg_F[sequence, 0] = sum_F1[1:].mean()
    std_F[sequence, 0] = sum_F1[1:].std(ddof=1)
    avg_F[sequence, 1] = sum_F2[1:].mean()
    std_F[sequence, 1] = sum_F2[1:].std(ddof=1)
    avg_F[sequence, 2] = sum_F3[1:].mean()
    std_F[sequence, 2] = sum_F3[1:].std(ddof=1)
# Get joint mass
print('  Getting joints\' mass...')
mass = np.ones([num_joints, 3])
for sequence in range(num_joints):
    joint = LOAD_joints[sequence]
    NumberResults = 0
    PointElm = MassSource = U1 = U2 = U3 = R1 = R2 = R3 = []
    [NumberResults, PointElm, MassSource, U1, U2, U3, R1, R2, R3,
     ret] = SapModel.Results.AssembledJointMass_1('MSSSRC1', joint, 0,
                                                  NumberResults, PointElm,
                                                  MassSource, U1, U2, U3,
                                                  R1, R2, R3)
    mass[sequence, 0] = U1[0]
    mass[sequence, 1] = U2[0]
    mass[sequence, 2] = U3[0]
print('  Writting to file...')
filesavedir = 'F:\\湖北襄阳体育场\\计算过程\\主体育场\\风振分析\\Results\\disp_accl\\'
savename = str(angle * 10) + 'out_300阶.txt'
jointsname = LOAD_joints.astype('int')[:, np.newaxis]
data = np.concatenate((jointsname, avg_acc, std_acc, avg_disp, std_disp, avg_F, std_F, mass), axis=1)
np.savetxt(
    filesavedir + savename,
    data,
    fmt=
    '%d,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f,%.15f',
    delimiter=',',
    newline='\n')

# close Sap2000
ret = mySapObject.ApplicationExit(False)
SapModel = None
mySapObject = None
