import rhinoscriptsyntax as rs

for i in range(1,68):
    gname="C_outside_"+str(i).zfill(2)
    rs.AddGroup(gname)
    object_ids = rs.GetObjects("Select objects to add to group")
    if object_ids:
        rs.ObjectLayer(object_ids, "struc::XM::C::out")
        rs.AddObjectsToGroup(object_ids, gname)

