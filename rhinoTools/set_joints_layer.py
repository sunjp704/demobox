import rhinoscriptsyntax as rs

f=open('C_in_joints.txt','r')
for line in f.readlines():
    info=list(map(str,line.split()))
    name=info[0]
    jointid=rs.ObjectsByName(name,True)
    rs.ObjectLayer(jointid[0], 'struc::joints::C_in')
f.close()