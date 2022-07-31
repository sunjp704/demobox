import src.structure as struc
import src.load as load

test_frame = struc.StructureFactory2D.frame_from_file('test', ('nodes.txt', 0), ('connection.txt', 0))
load1 = load.ConcendratedForce2D()
a = 1
