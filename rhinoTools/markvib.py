import rhinoscriptsyntax as rs

f=open('vib0.txt','r')
for line in f.readlines():
    info=list(map(str,line.split()))
    name=info[0]
    vib=float(info[1])
    vibtext=('%.2f' % vib)
    jointid=rs.ObjectsByName(name,True)
    loc=rs.PointCoordinates(jointid[0], point=None)
    lay=rs.ObjectLayer(jointid[0])
    textid=rs.AddText(vibtext,loc,height=0.5,font_style=0,justification=131072)
    rs.ObjectLayer(textid, lay)
f.close()