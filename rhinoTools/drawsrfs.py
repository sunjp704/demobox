import rhinoscriptsyntax as rs

f=open('loadXM.txt','r')

for line in f.readlines():
    info=list(map(str,line.split()))
    name=info[0]
    num_joints=int(info[1])
    if num_joints==4:
        p1=rs.ObjectsByName(info[2])
        p2=rs.ObjectsByName(info[3])
        p3=rs.ObjectsByName(info[4])
        p4=rs.ObjectsByName(info[5])
        srfobj=rs.AddSrfPt(p1+p2+p3+p4)
        rs.ObjectName( srfobj, 'XM'+name )
    if num_joints==3:
        p1=rs.ObjectsByName(info[2])
        p2=rs.ObjectsByName(info[3])
        p3=rs.ObjectsByName(info[4])
        srfobj=rs.AddSrfPt(p1+p2+p3)
        rs.ObjectName( srfobj, 'XM'+name )
f.close()
