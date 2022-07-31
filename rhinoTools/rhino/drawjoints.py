import rhinoscriptsyntax as rs

f=open('coord.txt','r')

for line in f.readlines():
    info=list(map(str,line.split()))
    name=info[0]
    x=float(info[1])
    y=float(info[2])
    z=float(info[3])
    ptobj = rs.AddPoint( (x,y,z) )
    if ptobj:
        rs.ObjectName( ptobj, name )
f.close()
