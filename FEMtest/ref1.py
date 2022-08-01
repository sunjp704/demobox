from multiprocessing import shared_memory

b = shared_memory.ShareableList(range(5))
c = shared_memory.ShareableList(name=b.shm.name)
