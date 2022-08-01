import rhinoscriptsyntax as rs
for i in range(1,68):
    gname='C_outside_'+str(i).zfill(2)
    jnames=''
    points = rs.GetObjects("Pick some points",rs.filter.point)
    if points:
        for p in points:
            jointname=rs.ObjectName( p )
            jnames=jnames+jointname+'\t'
    print gname+'\t'+jnames
