import rhinoscriptsyntax as rs

f=open('areajoints.txt','r')

for line in f.readlines():
    info=list(map(str,line.split()))
    name=info[0]
    x=float(info[1])/1000
    y=float(info[2])/1000
    z=float(info[3])/1000
    ptobj = rs.AddPoint( (x,y,z) )
    if ptobj:
        rs.ObjectName( ptobj, name )
f.close()
