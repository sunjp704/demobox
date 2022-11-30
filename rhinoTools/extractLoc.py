import rhinoscriptsyntax as rs
points = rs.GetObjects("Select points")
for point in points:
    crd = rs.PointCoordinates( point )
    name = rs.ObjectName( point )
    print name+':'+str(crd)

