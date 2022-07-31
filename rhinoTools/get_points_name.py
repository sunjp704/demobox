import rhinoscriptsyntax as rs
for block in range(0,2):
    f=open('massjoints'+str(block)+'.txt','w')
    points = rs.GetObjects("Pick some points")
    if points:
        for point in points:
            jointname=rs.ObjectName( point )
            f.write(str(jointname)+'\n')
    f.close()