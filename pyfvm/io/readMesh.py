# dir being the direction of OpenFOAM mesh file
def from_OpenFOAM(dir):
    with open(dir+'faces','rb') as f:
        data=f.readlines()
        ftype=data[10].split()[-1]
        if ftype==b'ascii;':
            num_points=int(data[18].decode(encoding='utf-8'))
            points=[None]*num_points
            
        elif ftype==b'binary;':
            pass
    