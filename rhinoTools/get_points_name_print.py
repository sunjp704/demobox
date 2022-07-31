import rhinoscriptsyntax as rs
points = rs.GetObjects("Pick some points")
if points:
    names=''
    for point in points:
        jointname=rs.ObjectName( point )
        names=names+jointname+'\t'
    print names