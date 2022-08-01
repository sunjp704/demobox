import rhinoscriptsyntax as rs
f=open('blocks.txt','r')
for line in f.readlines():
    names=''
    info=list(map(str,line.split()))
    gname=info[0]
    objs=rs.ObjectsByGroup( gname )
    for obj in objs:
        names=names+rs.ObjectName( obj )+'\t'
    print gname+'\t'+names
f.close()
