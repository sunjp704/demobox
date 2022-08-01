from time import time, sleep
from concurrent.futures import ThreadPoolExecutor


def haha1(counts, x):
    for _ in range(int(counts)):
        x[0] = 1


def haha2(counts, x):
    for _ in range(int(counts)):
        x[0] = 1


def haha3(counts, x):
    for _ in range(int(counts)):
        x[0] = 1


def haha4(counts, x):
    for _ in range(int(counts)):
        x[0] = 1


def main():
    a = [0, 0]
    b = [0, 0]
    c = [0, 0]
    d = [0, 0]
    start = time()
    with ThreadPoolExecutor(max_workers=4) as pool:
        pool.submit(haha1, 1E8, a)
        pool.submit(haha2, 1E8, b)
        pool.submit(haha3, 1E8, c)
        pool.submit(haha4, 1E8, d)
    end = time()
    print(f'总耗时: {end - start:.3f}秒.')


#    print(
#        a[0],
#        b[0],
#        c[0],
#        d[0],
#    )

if __name__ == '__main__':
    main()
